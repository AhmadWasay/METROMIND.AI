import sqlite3
import uuid
import os
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import random
import json # For storing trip_plan as JSON

def generate_uuid():
    return str(uuid.uuid4())

# --- Database Connection ---
# Use absolute path so PythonAnywhere WSGI can find the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_FILE = os.path.join(BASE_DIR, 'metromind.db')

def get_db():
    """Helper to get a database connection with row_factory for dict-like rows."""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.execute("PRAGMA journal_mode=WAL;") # Enable Write-Ahead Logging for better concurrency
    conn.row_factory = sqlite3.Row # Allows accessing columns by name
    return conn

# --- Database Initialization ---
def init_db():
    """Initializes the database schema."""
    conn = get_db()
    c = conn.cursor()
    
    # Users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            full_name TEXT NOT NULL,
            phone TEXT,
            is_premium BOOLEAN DEFAULT FALSE,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            last_login TEXT,
            is_verified BOOLEAN DEFAULT FALSE,
            otp TEXT,
            otp_expires_at TEXT
        )
    ''')
    
    # Orders table
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            source TEXT NOT NULL,
            destination TEXT NOT NULL,
            trip_plan TEXT NOT NULL, -- Stored as JSON
            trip_date TEXT NOT NULL,
            booking_time TEXT DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'pending', -- pending, confirmed, in_transit, completed, cancelled
            rating INTEGER,
            review TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')
    
    # Transit Capacity table (simplified for demo)
    c.execute('''
        CREATE TABLE IF NOT EXISTS transit_capacity (
            route_code TEXT PRIMARY KEY,
            total_capacity INTEGER NOT NULL,
            available_seats INTEGER NOT NULL,
            booked_seats INTEGER NOT NULL
        )
    ''')
    
    # Notifications table (for queuing emails/SMS)
    c.execute('''
        CREATE TABLE IF NOT EXISTS notifications (
            notification_id TEXT PRIMARY KEY,
            order_id TEXT,
            user_id TEXT NOT NULL,
            type TEXT NOT NULL, -- email, sms
            event TEXT NOT NULL, -- booking_confirmation, status_update, alert
            message TEXT NOT NULL,
            status TEXT DEFAULT 'pending', -- pending, sent, failed
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            sent_at TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
    ''')

    # Admin Logs table
    c.execute('''
        CREATE TABLE IF NOT EXISTS admin_logs (
            log_id TEXT PRIMARY KEY,
            admin_id TEXT, -- Could be user_id of an admin
            action TEXT NOT NULL,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            details TEXT,
            FOREIGN KEY (admin_id) REFERENCES users(user_id)
        )
    ''')
    
    conn.commit()
    conn.close()

def init_transit_capacity():
    """Initializes dummy transit capacity for demo routes."""
    conn = get_db()
    c = conn.cursor()
    
    # Example routes and capacities
    # These should ideally come from transit_data.py or a config
    dummy_capacities = {
        'BRT_RED': 1500,
        'BRT_ORANGE': 1800,
        'FR_1': 60,
        'FR_2': 50,
        'FR_3A': 50,
        'FR_4': 70,
        'FR_4A': 40,
        'FR_6': 50,
        'FR_7': 60,
        'FR_8A': 50,
        'FR_8B': 50,
        'FR_8C': 50,
        'FR_9': 60,
        'FR_10_5': 50,
        'FR_11': 50,
        'FR_12': 50,
        'FR_13': 50,
        'FR_14': 60,
        'FR_14A': 40,
        'FR_15': 50,
        'EX_16': 50,
        'FR_17': 50,
    }
    
    for route_code, capacity in dummy_capacities.items():
        c.execute('''
            INSERT OR IGNORE INTO transit_capacity (route_code, total_capacity, available_seats, booked_seats)
            VALUES (?, ?, ?, ?)
        ''', (route_code, capacity, capacity, 0))
    
    conn.commit()
    conn.close()

# --- User Management ---
def create_user(email, password, full_name, phone=None):
    conn = get_db()
    c = conn.cursor()
    try:
        user_id = f"user_{uuid.uuid4().hex[:12]}"
        hashed_password = generate_password_hash(password)
        otp = str(random.randint(100000, 999999))
        otp_expires_at = (datetime.utcnow() + timedelta(minutes=10)).isoformat()
        
        c.execute('''
            INSERT INTO users (user_id, email, password_hash, full_name, phone, otp, otp_expires_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, email, hashed_password, full_name, phone, otp, otp_expires_at))
        conn.commit()
        return {"status": "success", "otp": otp, "message": "User registration initiated."}
    except sqlite3.IntegrityError:
        # If user exists but is not verified, resend OTP and update password
        c.execute('SELECT is_verified FROM users WHERE email = ?', (email,))
        user = c.fetchone()
        if user and not user['is_verified']:
            otp = str(random.randint(100000, 999999))
            otp_expires_at = (datetime.utcnow() + timedelta(minutes=10)).isoformat()
            # Also update the password hash, in case the user forgot and is re-signing up
            hashed_password = generate_password_hash(password)
            c.execute('UPDATE users SET password_hash = ?, otp = ?, otp_expires_at = ? WHERE email = ?', (hashed_password, otp, otp_expires_at, email))
            conn.commit()
            return {"status": "resent_otp", "otp": otp, "message": "User already exists but is not verified. A new OTP has been sent."}
        return {"status": "error", "message": "Email already registered and verified"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()

def authenticate_user(email, password):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = c.fetchone()
        
        if not user:
            return {"status": "error", "message": "Invalid email or password"}

        if not user['is_verified']:
            return {"status": "error", "message": "Account not verified. Please check your email for an OTP."}

        if check_password_hash(user['password_hash'], password):
                # Update last login
                c.execute('UPDATE users SET last_login = ? WHERE user_id = ?', (datetime.utcnow().isoformat(), user['user_id']))
                conn.commit()
                return {
                    "status": "success",
                    "user_id": user['user_id'],
                    "email": user['email'],
                    "full_name": user['full_name'],
                    "is_premium": bool(user['is_premium']),
                    "message": "Login successful"
                }
        return {"status": "error", "message": "Invalid email or password"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()

def get_user(user_id):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        user = c.fetchone()
        return dict(user) if user else None
    finally:
        conn.close()

def upgrade_to_premium(user_id):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('UPDATE users SET is_premium = TRUE WHERE user_id = ?', (user_id,))
        conn.commit()
        return {"status": "success", "message": "User upgraded to premium"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()

def verify_user_otp(email, otp):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = c.fetchone()

        if not user:
            return {"status": "error", "message": "User not found."}
        
        if user['is_verified']:
            return {"status": "error", "message": "Account already verified."}
        
        otp_expires_at = datetime.fromisoformat(user['otp_expires_at'])
        if user['otp'] != otp or otp_expires_at < datetime.utcnow():
            return {"status": "error", "message": "Invalid or expired OTP."}
        
        c.execute('''
            UPDATE users 
            SET is_verified = TRUE, otp = NULL, otp_expires_at = NULL 
            WHERE email = ?
        ''', (email,))
        conn.commit()
        return {"status": "success", "message": "Account verified successfully. You can now log in."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()

def initiate_password_reset(email):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = c.fetchone()

        # To prevent email enumeration, don't reveal if user exists or not.
        # Only proceed if user exists and is verified.
        if user and user['is_verified']:
            otp = str(random.randint(100000, 999999))
            otp_expires_at = (datetime.utcnow() + timedelta(minutes=10)).isoformat()
            c.execute('UPDATE users SET otp = ?, otp_expires_at = ? WHERE email = ?', (otp, otp_expires_at, email))
            conn.commit()
            return {"status": "success", "otp": otp}
        
        # If user doesn't exist or isn't verified, do nothing but return a generic success status
        # so the API layer can send a generic message.
        return {"status": "success_generic"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()

def reset_password_with_otp(email, otp, new_password):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = c.fetchone()

        if not user:
            return {"status": "error", "message": "Invalid OTP or email."}

        if not user['otp'] or not user['otp_expires_at']:
             return {"status": "error", "message": "No password reset initiated."}

        otp_expires_at = datetime.fromisoformat(user['otp_expires_at'])
        if user['otp'] != otp or otp_expires_at < datetime.utcnow():
            return {"status": "error", "message": "Invalid or expired OTP."}
        
        # OTP is valid, reset the password
        hashed_password = generate_password_hash(new_password)
        c.execute('''
            UPDATE users 
            SET password_hash = ?, otp = NULL, otp_expires_at = NULL 
            WHERE email = ?
        ''', (hashed_password, email))
        conn.commit()
        
        return {
            "status": "success",
            "message": "Password has been reset successfully. You can now log in with your new password."
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()

# --- Order Management ---
def create_order(user_id, source, destination, trip_plan, trip_date):
    conn = get_db()
    c = conn.cursor()
    try:
        order_id = f"ORD_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:4]}"
        
        # Assume trip_plan is a dict/JSON object
        trip_plan_json = json.dumps(trip_plan)
        
        c.execute('''
            INSERT INTO orders (order_id, user_id, source, destination, trip_plan, trip_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (order_id, user_id, source, destination, trip_plan_json, trip_date, 'pending'))
        conn.commit()
        
        # Deduct from transit capacity (simplified: assume one seat per order)
        # This needs to be more sophisticated, based on actual route segments
        # For now, just deduct from a dummy route if trip_plan contains one
        if trip_plan and 'packages' in trip_plan and trip_plan['packages']:
            first_package = trip_plan['packages'][0]
            if 'journey_segments' in first_package:
                for segment in first_package['journey_segments']:
                    if segment['type'] == 'bus' or segment['type'] == 'metro':
                        route_code = segment.get('route') or segment.get('line')
                        if route_code:
                            c.execute('''
                                UPDATE transit_capacity
                                SET available_seats = available_seats - 1,
                                    booked_seats = booked_seats + 1
                                WHERE route_code = ? AND available_seats > 0
                            ''', (route_code,))
                            conn.commit()
                            # If no rows updated, it means capacity was 0
                            if c.rowcount == 0:
                                conn.rollback() # Rollback order creation too
                                return {"status": "error", "message": f"No seats available on {route_code}"}
        
        return {"status": "success", "order_id": order_id, "message": "Order created successfully"}
    except Exception as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()

def get_order(order_id):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM orders WHERE order_id = ?', (order_id,))
        order = c.fetchone()
        if order:
            order_dict = dict(order)
            order_dict['trip_plan'] = json.loads(order_dict['trip_plan']) # Deserialize JSON
            order_dict['total_fare'] = order_dict['trip_plan'].get('estimated_cost', 0)
            return order_dict
        return None
    finally:
        conn.close()

def get_user_orders(user_id, status_filter=None):
    conn = get_db()
    c = conn.cursor()
    try:
        if status_filter:
            c.execute('SELECT * FROM orders WHERE user_id = ? AND status = ? ORDER BY booking_time DESC', (user_id, status_filter))
        else:
            c.execute('SELECT * FROM orders WHERE user_id = ? ORDER BY booking_time DESC', (user_id,))
        orders = [dict(row) for row in c.fetchall()]
        for order in orders:
            order['trip_plan'] = json.loads(order['trip_plan'])
            order['total_fare'] = order['trip_plan'].get('estimated_cost', 0)
        return orders
    finally:
        conn.close()

def cancel_order(order_id, reason=""):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('UPDATE orders SET status = ?, review = ? WHERE order_id = ?', ('cancelled', reason, order_id))
        conn.commit()
        
        # Refund capacity (simplified)
        order = get_order(order_id)
        if order and 'trip_plan' in order and 'packages' in order['trip_plan'] and order['trip_plan']['packages']:
            first_package = order['trip_plan']['packages'][0]
            if 'journey_segments' in first_package:
                for segment in first_package['journey_segments']:
                    if segment['type'] == 'bus' or segment['type'] == 'metro':
                        route_code = segment.get('route') or segment.get('line')
                        if route_code:
                            c.execute('''
                                UPDATE transit_capacity
                                SET available_seats = available_seats + 1,
                                    booked_seats = booked_seats - 1
                                WHERE route_code = ?
                            ''', (route_code,))
                            conn.commit()
        
        return {"status": "success", "message": "Order cancelled successfully"}
    except Exception as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()

def rate_order(order_id, rating, review):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('UPDATE orders SET rating = ?, review = ?, status = ? WHERE order_id = ?', (rating, review, 'completed', order_id))
        conn.commit()
        return {"status": "success", "message": "Order rated successfully"}
    except Exception as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()

def update_order_status(order_id, status):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('UPDATE orders SET status = ? WHERE order_id = ?', (status, order_id))
        conn.commit()
        return {"status": "success", "message": f"Order {order_id} status updated to {status}"}
    except Exception as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()

# --- Admin Functions ---
def get_admin_dashboard_stats():
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('SELECT COUNT(*) FROM users')
        total_users = c.fetchone()[0]
        
        c.execute('SELECT COUNT(*) FROM orders WHERE status = "completed"')
        completed_orders = c.fetchone()[0]
        
        c.execute('SELECT SUM(booked_seats) FROM transit_capacity')
        total_booked_seats = c.fetchone()[0] or 0
        
        # Example network capacity usage (simplified)
        network_capacity_usage = {
            'Red_Line': '78%',
            'Green_Line': '65%',
            'Blue_Line': '82%'
        }
        
        return {
            "total_users": total_users,
            "completed_orders": completed_orders,
            "total_booked_seats": total_booked_seats,
            "network_capacity_usage": network_capacity_usage
        }
    finally:
        conn.close()

def get_top_routes(limit=5):
    conn = get_db()
    c = conn.cursor()
    try:
        # This is a simplified approach. A real implementation would parse trip_plan JSON
        # to extract individual route segments and count them.
        c.execute('''
            SELECT source, destination, COUNT(*) as count
            FROM orders
            GROUP BY source, destination
            ORDER BY count DESC
            LIMIT ?
        ''', (limit,))
        return [dict(row) for row in c.fetchall()]
    finally:
        conn.close()

def get_pending_notifications():
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM notifications WHERE status = "pending" ORDER BY created_at ASC')
        return [dict(row) for row in c.fetchall()]
    finally:
        conn.close()

def queue_notification(order_id, user_id, event_type, notification_type, message):
    conn = get_db()
    c = conn.cursor()
    try:
        notification_id = f"NOTIF_{uuid.uuid4().hex[:12]}"
        c.execute('''
            INSERT INTO notifications (notification_id, order_id, user_id, type, event, message)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (notification_id, order_id, user_id, notification_type, event_type, message))
        conn.commit()
        return {"status": "success", "notification_id": notification_id}
    except Exception as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()

# --- Transit Capacity ---
def get_route_availability(route_code, service_time):
    conn = get_db()
    c = conn.cursor()
    try:
        # service_time is ignored for this simplified capacity model
        c.execute('SELECT * FROM transit_capacity WHERE route_code = ?', (route_code,))
        capacity = c.fetchone()
        return dict(capacity) if capacity else None
    finally:
        conn.close()
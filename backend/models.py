"""
Database Models for MetroMind AI
Manages Users, Orders, Cancellations, and Notifications
"""
import sqlite3
import json
from datetime import datetime, timedelta
from hashlib import sha256
import secrets

DATABASE_PATH = "metromind.db"

def init_db():
    """Initialize database schema"""
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        password_hash TEXT NOT NULL,
        full_name TEXT,
        is_premium BOOLEAN DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP
    )''')
    
    # Orders table
    c.execute('''CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        user_id TEXT NOT NULL,
        source TEXT NOT NULL,
        destination TEXT NOT NULL,
        trip_date TEXT NOT NULL,
        trip_plan TEXT NOT NULL,
        total_fare REAL,
        status TEXT DEFAULT 'pending',
        booking_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        travel_time TIMESTAMP,
        completion_time TIMESTAMP,
        cancelled_at TIMESTAMP,
        cancellation_reason TEXT,
        rating REAL,
        review TEXT,
        email_sent BOOLEAN DEFAULT 0,
        sms_sent BOOLEAN DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )''')
    
    # Transit Inventory (Capacity Management)
    c.execute('''CREATE TABLE IF NOT EXISTS transit_capacity (
        capacity_id TEXT PRIMARY KEY,
        route_code TEXT NOT NULL,
        service_time TEXT NOT NULL,
        total_capacity INTEGER DEFAULT 100,
        booked_seats INTEGER DEFAULT 0,
        available_seats INTEGER,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Admin Logs
    c.execute('''CREATE TABLE IF NOT EXISTS admin_logs (
        log_id TEXT PRIMARY KEY,
        admin_id TEXT,
        action TEXT,
        target_order_id TEXT,
        details TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Notifications Queue
    c.execute('''CREATE TABLE IF NOT EXISTS notifications (
        notification_id TEXT PRIMARY KEY,
        order_id TEXT NOT NULL,
        user_id TEXT NOT NULL,
        notification_type TEXT,
        channel TEXT,
        message TEXT,
        status TEXT DEFAULT 'pending',
        sent_at TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )''')
    
    # Settings table
    c.execute('''CREATE TABLE IF NOT EXISTS settings (
        setting_key TEXT PRIMARY KEY,
        setting_value TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    conn.commit()
    conn.close()

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# =================== USER OPERATIONS ===================

def create_user(email, password, full_name, phone=None):
    """Create new user account"""
    conn = get_db()
    c = conn.cursor()
    
    user_id = f"user_{secrets.token_hex(8)}"
    password_hash = sha256(password.encode()).hexdigest()
    
    try:
        c.execute('''INSERT INTO users (user_id, email, password_hash, full_name, phone)
                     VALUES (?, ?, ?, ?, ?)''',
                  (user_id, email, password_hash, full_name, phone))
        conn.commit()
        return {"status": "success", "user_id": user_id, "message": "Account created successfully"}
    except sqlite3.IntegrityError:
        return {"status": "error", "message": "Email already exists"}
    finally:
        conn.close()

def authenticate_user(email, password):
    """Authenticate user and return user_id"""
    conn = get_db()
    c = conn.cursor()
    
    password_hash = sha256(password.encode()).hexdigest()
    
    c.execute('SELECT user_id, is_premium FROM users WHERE email = ? AND password_hash = ?',
              (email, password_hash))
    user = c.fetchone()
    
    if user:
        # Update last login
        c.execute('UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE user_id = ?',
                  (user['user_id'],))
        conn.commit()
        return {"status": "success", "user_id": user['user_id'], "is_premium": user['is_premium']}
    
    conn.close()
    return {"status": "error", "message": "Invalid credentials"}

def get_user(user_id):
    """Get user details"""
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = c.fetchone()
    conn.close()
    
    if user:
        return dict(user)
    return None

def upgrade_to_premium(user_id):
    """Upgrade user to premium tier"""
    conn = get_db()
    c = conn.cursor()
    
    c.execute('UPDATE users SET is_premium = 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Upgraded to premium"}

# =================== ORDER OPERATIONS ===================

def create_order(user_id, source, destination, trip_plan, trip_date):
    """Create new booking order"""
    conn = get_db()
    c = conn.cursor()
    
    order_id = f"order_{secrets.token_hex(8)}"
    trip_plan_json = json.dumps(trip_plan) if isinstance(trip_plan, dict) else trip_plan
    
    # Calculate total fare from trip plan
    total_fare = 0
    if isinstance(trip_plan, dict) and 'segments' in trip_plan:
        for segment in trip_plan['segments']:
            if 'fare' in segment:
                total_fare += segment['fare']
    
    try:
        c.execute('''INSERT INTO orders 
                    (order_id, user_id, source, destination, trip_plan, trip_date, total_fare, status)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (order_id, user_id, source, destination, trip_plan_json, trip_date, total_fare, 'pending'))
        conn.commit()
        conn.close()
        return {"status": "success", "order_id": order_id, "message": "Order created successfully"}
    except Exception as e:
        conn.close()
        return {"status": "error", "message": str(e)}

def get_order(order_id):
    """Get order details"""
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT * FROM orders WHERE order_id = ?', (order_id,))
    order = c.fetchone()
    conn.close()
    
    if order:
        order_dict = dict(order)
        try:
            order_dict['trip_plan'] = json.loads(order_dict['trip_plan'])
        except:
            pass
        return order_dict
    return None

def get_user_orders(user_id, status=None):
    """Get all orders for a user"""
    conn = get_db()
    c = conn.cursor()
    
    if status:
        c.execute('SELECT * FROM orders WHERE user_id = ? AND status = ? ORDER BY booking_time DESC',
                  (user_id, status))
    else:
        c.execute('SELECT * FROM orders WHERE user_id = ? ORDER BY booking_time DESC', (user_id,))
    
    orders = c.fetchall()
    conn.close()
    
    result = []
    for order in orders:
        order_dict = dict(order)
        try:
            order_dict['trip_plan'] = json.loads(order_dict['trip_plan'])
        except:
            pass
        result.append(order_dict)
    
    return result

def update_order_status(order_id, status):
    """Update order status"""
    conn = get_db()
    c = conn.cursor()
    
    c.execute('UPDATE orders SET status = ? WHERE order_id = ?', (status, order_id))
    conn.commit()
    conn.close()
    
    return {"status": "success", "message": f"Order status updated to {status}"}

def cancel_order(order_id, reason="User requested"):
    """Cancel an order"""
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''UPDATE orders SET status = ?, cancelled_at = CURRENT_TIMESTAMP, cancellation_reason = ? 
                 WHERE order_id = ?''',
              ('cancelled', reason, order_id))
    conn.commit()
    conn.close()
    
    return {"status": "success", "message": "Order cancelled successfully"}

def rate_order(order_id, rating, review=None):
    """Rate a completed order"""
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''UPDATE orders SET rating = ?, review = ? WHERE order_id = ?''',
              (rating, review, order_id))
    conn.commit()
    conn.close()
    
    return {"status": "success", "message": "Thank you for your feedback!"}

# =================== TRANSIT CAPACITY ===================

def init_transit_capacity():
    """Initialize transit capacity for all routes"""
    from transit_data import BUS_ROUTES
    
    conn = get_db()
    c = conn.cursor()
    
    for route in BUS_ROUTES:
        for hour in range(6, 23):  # 6 AM to 10 PM
            service_time = f"{hour:02d}:00"
            capacity_id = f"cap_{route['code']}_{service_time}"
            
            c.execute('''INSERT OR REPLACE INTO transit_capacity 
                        (capacity_id, route_code, service_time, total_capacity, booked_seats, available_seats)
                        VALUES (?, ?, ?, ?, ?, ?)''',
                      (capacity_id, route['code'], service_time, 80, 0, 80))
    
    conn.commit()
    conn.close()

def book_seat(route_code, service_time):
    """Book a seat on a route at specified time"""
    conn = get_db()
    c = conn.cursor()
    
    capacity_id = f"cap_{route_code}_{service_time}"
    
    c.execute('''SELECT booked_seats, available_seats FROM transit_capacity 
                 WHERE capacity_id = ?''', (capacity_id,))
    capacity = c.fetchone()
    
    if not capacity or capacity['available_seats'] <= 0:
        conn.close()
        return {"status": "error", "message": "No seats available"}
    
    c.execute('''UPDATE transit_capacity SET booked_seats = booked_seats + 1, available_seats = available_seats - 1 
                 WHERE capacity_id = ?''', (capacity_id,))
    conn.commit()
    conn.close()
    
    return {"status": "success", "message": "Seat booked successfully"}

def release_seat(route_code, service_time):
    """Release a booked seat (for cancellations)"""
    conn = get_db()
    c = conn.cursor()
    
    capacity_id = f"cap_{route_code}_{service_time}"
    
    c.execute('''UPDATE transit_capacity SET booked_seats = booked_seats - 1, available_seats = available_seats + 1 
                 WHERE capacity_id = ? AND booked_seats > 0''', (capacity_id,))
    conn.commit()
    conn.close()
    
    return {"status": "success", "message": "Seat released"}

def get_route_availability(route_code, service_time):
    """Check availability for a route at given time"""
    conn = get_db()
    c = conn.cursor()
    
    capacity_id = f"cap_{route_code}_{service_time}"
    c.execute('SELECT * FROM transit_capacity WHERE capacity_id = ?', (capacity_id,))
    
    result = c.fetchone()
    conn.close()
    
    if result:
        return dict(result)
    return None

# =================== NOTIFICATIONS ===================

def queue_notification(order_id, user_id, notification_type, channel, message):
    """Queue a notification (email/SMS)"""
    conn = get_db()
    c = conn.cursor()
    
    notification_id = f"notif_{secrets.token_hex(8)}"
    
    c.execute('''INSERT INTO notifications 
                (notification_id, order_id, user_id, notification_type, channel, message)
                VALUES (?, ?, ?, ?, ?, ?)''',
              (notification_id, order_id, user_id, notification_type, channel, message))
    conn.commit()
    conn.close()
    
    return notification_id

def get_pending_notifications(channel=None):
    """Get pending notifications to send"""
    conn = get_db()
    c = conn.cursor()
    
    if channel:
        c.execute('SELECT * FROM notifications WHERE status = ? AND channel = ?',
                  ('pending', channel))
    else:
        c.execute('SELECT * FROM notifications WHERE status = ?', ('pending',))
    
    notifications = c.fetchall()
    conn.close()
    
    return [dict(notif) for notif in notifications]

def mark_notification_sent(notification_id):
    """Mark notification as sent"""
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''UPDATE notifications SET status = ?, sent_at = CURRENT_TIMESTAMP 
                 WHERE notification_id = ?''', ('sent', notification_id))
    conn.commit()
    conn.close()

# =================== ANALYTICS ===================

def get_admin_dashboard_stats():
    """Get dashboard statistics for admin"""
    conn = get_db()
    c = conn.cursor()
    
    stats = {}
    
    # Total orders
    c.execute('SELECT COUNT(*) as count FROM orders')
    stats['total_orders'] = c.fetchone()['count']
    
    # Orders by status
    c.execute('''SELECT status, COUNT(*) as count FROM orders GROUP BY status''')
    stats['orders_by_status'] = {row['status']: row['count'] for row in c.fetchall()}
    
    # Total revenue
    c.execute('SELECT SUM(total_fare) as revenue FROM orders WHERE status != ?', ('cancelled',))
    stats['total_revenue'] = c.fetchone()['revenue'] or 0
    
    # Average rating
    c.execute('SELECT AVG(rating) as avg_rating FROM orders WHERE rating IS NOT NULL')
    stats['average_rating'] = c.fetchone()['avg_rating'] or 0
    
    # Total users
    c.execute('SELECT COUNT(*) as count FROM users')
    stats['total_users'] = c.fetchone()['count']
    
    # Premium users
    c.execute('SELECT COUNT(*) as count FROM users WHERE is_premium = 1')
    stats['premium_users'] = c.fetchone()['count']
    
    conn.close()
    return stats

def get_top_routes():
    """Get most popular routes"""
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''SELECT source, destination, COUNT(*) as bookings FROM orders 
                 WHERE status != 'cancelled' GROUP BY source, destination 
                 ORDER BY bookings DESC LIMIT 10''')
    
    routes = [dict(row) for row in c.fetchall()]
    conn.close()
    
    return routes

# Initialize database on import
try:
    init_db()
except:
    pass

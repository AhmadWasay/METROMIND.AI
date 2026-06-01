"""
Extended MetroMind API - User Authentication, Booking, Admin, and Notifications
This file extends the main.py with business process endpoints
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import *
from notifications import *
import json
from datetime import datetime, timedelta
from functools import wraps

# Import existing app from main
from main import app

# =================== AUTHENTICATION MIDDLEWARE ===================

def token_required(f):
    """Decorator to check if user_id is provided"""
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = request.headers.get('X-User-ID') or request.args.get('user_id')
        if not user_id:
            return jsonify({"error": "User authentication required"}), 401
        return f(user_id, *args, **kwargs)
    return decorated

# =================== USER AUTHENTICATION ENDPOINTS ===================

@app.route("/api/auth/signup", methods=["POST"])
def signup():
    """User registration endpoint"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        full_name = data.get('full_name')
        phone = data.get('phone')
        
        if not email or not password or not full_name:
            return jsonify({"error": "Email, password, and name required"}), 400
        
        result = create_user(email, password, full_name, phone)
        return jsonify(result), 201 if result['status'] == 'success' else 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/auth/login", methods=["POST"])
def login():
    """User login endpoint"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400
        
        result = authenticate_user(email, password)
        return jsonify(result), 200 if result['status'] == 'success' else 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/auth/profile", methods=["GET"])
@token_required
def get_profile(user_id):
    """Get user profile"""
    try:
        user = get_user(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        # Remove sensitive data
        user.pop('password_hash', None)
        return jsonify({"status": "success", "user": user}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/auth/upgrade-premium", methods=["POST"])
@token_required
def upgrade_premium(user_id):
    """Upgrade user to premium tier"""
    try:
        result = upgrade_to_premium(user_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =================== TRIP BOOKING ENDPOINTS ===================

@app.route("/api/orders/create", methods=["POST"])
@token_required
def create_booking(user_id):
    """Create new trip booking/order"""
    try:
        data = request.get_json()
        source = data.get('source')
        destination = data.get('destination')
        trip_plan = data.get('trip_plan')
        trip_date = data.get('trip_date')
        
        if not all([source, destination, trip_plan, trip_date]):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create order in database
        result = create_order(user_id, source, destination, trip_plan, trip_date)
        
        if result['status'] == 'success':
            order_id = result['order_id']
            
            # Get user details for notifications
            user = get_user(user_id)
            total_fare = data.get('total_fare', 0)
            
            # Send confirmation email
            email_result = send_order_confirmation_email(
                user['email'], 
                user['full_name'], 
                order_id, 
                trip_plan, 
                total_fare, 
                trip_date
            )
            
            # Send SMS if premium user
            if user['is_premium'] and user.get('phone'):
                sms_result = send_trip_confirmation_sms(
                    user['phone'], 
                    order_id, 
                    trip_date
                )
            
            # Queue notifications in database
            queue_notification(
                order_id, 
                user_id, 
                'booking_confirmation', 
                'email', 
                f"Your trip from {source} to {destination} has been confirmed"
            )
            
            return jsonify({
                "status": "success",
                "order_id": order_id,
                "message": "Booking confirmed! Check your email for details.",
                "email_sent": email_result['status'] == 'success'
            }), 201
        
        return jsonify(result), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/orders/<order_id>", methods=["GET"])
@token_required
def get_order_details(user_id, order_id):
    """Get order details"""
    try:
        order = get_order(order_id)
        if not order:
            return jsonify({"error": "Order not found"}), 404
        
        if order['user_id'] != user_id:
            return jsonify({"error": "Unauthorized"}), 403
        
        return jsonify({"status": "success", "order": order}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/orders/user/<user_id>", methods=["GET"])
@token_required
def list_user_orders(user_id):
    """Get all orders for logged-in user"""
    try:
        status_filter = request.args.get('status')
        orders = get_user_orders(user_id, status_filter)
        
        return jsonify({
            "status": "success",
            "orders": orders,
            "count": len(orders)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/orders/<order_id>/cancel", methods=["POST"])
@token_required
def cancel_order_endpoint(user_id, order_id):
    """Cancel a booking"""
    try:
        order = get_order(order_id)
        if not order:
            return jsonify({"error": "Order not found"}), 404
        
        if order['user_id'] != user_id:
            return jsonify({"error": "Unauthorized"}), 403
        
        if order['status'] == 'cancelled':
            return jsonify({"error": "Order already cancelled"}), 400
        
        # Check if cancellation is within allowed time (30 mins before travel)
        data = request.get_json() or {}
        reason = data.get('reason', 'User requested')
        
        # Cancel order
        cancel_result = cancel_order(order_id, reason)
        
        # Send cancellation email
        user = get_user(user_id)
        send_order_cancelled_email(user['email'], user['full_name'], order_id, reason)
        
        # Queue notification
        queue_notification(
            order_id,
            user_id,
            'order_cancelled',
            'email',
            f"Your trip order {order_id} has been cancelled"
        )
        
        return jsonify(cancel_result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/orders/<order_id>/rate", methods=["POST"])
@token_required
def rate_order_endpoint(user_id, order_id):
    """Rate a completed trip"""
    try:
        order = get_order(order_id)
        if not order:
            return jsonify({"error": "Order not found"}), 404
        
        if order['user_id'] != user_id:
            return jsonify({"error": "Unauthorized"}), 403
        
        data = request.get_json()
        rating = data.get('rating')
        review = data.get('review')
        
        if not rating or rating < 1 or rating > 5:
            return jsonify({"error": "Rating must be between 1 and 5"}), 400
        
        result = rate_order(order_id, rating, review)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =================== ORDER STATUS & TRACKING ===================

@app.route("/api/orders/<order_id>/status", methods=["GET"])
@token_required
def get_status(user_id, order_id):
    """Get real-time trip status"""
    try:
        order = get_order(order_id)
        if not order:
            return jsonify({"error": "Order not found"}), 404
        
        if order['user_id'] != user_id:
            return jsonify({"error": "Unauthorized"}), 403
        
        statuses = [
            "Awaiting Transport",
            "Boarded First Bus",
            "Transferring at Hub",
            "On Final Leg",
            "Destination Reached"
        ]
        
        return jsonify({
            "status": "success",
            "order_id": order_id,
            "current_status": order['status'],
            "trip_status": statuses[min(3, len(statuses)-1)],
            "progress_percentage": 60,
            "next_milestone": "Approaching Hub Station",
            "estimated_arrival": "08:35 AM",
            "current_location": {
                "lat": 33.7456,
                "lng": 73.1756,
                "description": "On Transit Route"
            }
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/orders/<order_id>/update-status", methods=["PUT"])
def update_order_status_endpoint(order_id):
    """Admin endpoint to update order status"""
    try:
        # Check admin authentication
        admin_token = request.headers.get('X-Admin-Token')
        if admin_token != 'admin_secret':  # In production, use proper JWT
            return jsonify({"error": "Admin authorization required"}), 403
        
        data = request.get_json()
        status = data.get('status')
        message = data.get('message', '')
        
        if status not in ['pending', 'confirmed', 'in_transit', 'completed', 'cancelled']:
            return jsonify({"error": "Invalid status"}), 400
        
        # Update status
        result = update_order_status(order_id, status)
        
        # Send email notification
        order = get_order(order_id)
        if order:
            user = get_user(order['user_id'])
            send_status_update_email(
                user['email'],
                user['full_name'],
                order_id,
                status,
                message or f"Your trip status is now: {status}"
            )
        
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =================== ADMIN DASHBOARD ENDPOINTS ===================

@app.route("/api/admin/dashboard", methods=["GET"])
def admin_dashboard():
    """Admin dashboard with statistics"""
    try:
        admin_token = request.headers.get('X-Admin-Token')
        if admin_token != 'admin_secret':
            return jsonify({"error": "Admin authorization required"}), 403
        
        stats = get_admin_dashboard_stats()
        top_routes = get_top_routes()
        
        return jsonify({
            "status": "success",
            "statistics": stats,
            "top_routes": top_routes,
            "timestamp": datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/admin/orders", methods=["GET"])
def admin_view_all_orders():
    """Admin endpoint to view all orders"""
    try:
        admin_token = request.headers.get('X-Admin-Token')
        if admin_token != 'admin_secret':
            return jsonify({"error": "Admin authorization required"}), 403
        
        conn = get_db()
        c = conn.cursor()
        
        status_filter = request.args.get('status')
        if status_filter:
            c.execute('SELECT * FROM orders WHERE status = ? ORDER BY booking_time DESC', (status_filter,))
        else:
            c.execute('SELECT * FROM orders ORDER BY booking_time DESC')
        
        orders = [dict(row) for row in c.fetchall()]
        conn.close()
        
        return jsonify({
            "status": "success",
            "orders": orders,
            "count": len(orders)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/admin/users", methods=["GET"])
def admin_view_users():
    """Admin endpoint to view all users"""
    try:
        admin_token = request.headers.get('X-Admin-Token')
        if admin_token != 'admin_secret':
            return jsonify({"error": "Admin authorization required"}), 403
        
        conn = get_db()
        c = conn.cursor()
        c.execute('''SELECT user_id, email, full_name, phone, is_premium, created_at, last_login 
                     FROM users ORDER BY created_at DESC''')
        
        users = [dict(row) for row in c.fetchall()]
        conn.close()
        
        return jsonify({
            "status": "success",
            "users": users,
            "count": len(users)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/admin/notifications", methods=["GET"])
def admin_view_notifications():
    """Admin endpoint to view pending notifications"""
    try:
        admin_token = request.headers.get('X-Admin-Token')
        if admin_token != 'admin_secret':
            return jsonify({"error": "Admin authorization required"}), 403
        
        notifications = get_pending_notifications()
        
        return jsonify({
            "status": "success",
            "pending_notifications": notifications,
            "count": len(notifications)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/admin/send-alerts", methods=["POST"])
def admin_send_alerts():
    """Admin endpoint to send manual alerts to users"""
    try:
        admin_token = request.headers.get('X-Admin-Token')
        if admin_token != 'admin_secret':
            return jsonify({"error": "Admin authorization required"}), 403
        
        data = request.get_json()
        user_ids = data.get('user_ids', [])
        message = data.get('message', '')
        alert_type = data.get('type', 'info')  # info, warning, alert
        
        if not message:
            return jsonify({"error": "Message required"}), 400
        
        sent_count = 0
        for user_id in user_ids:
            user = get_user(user_id)
            if user and user.get('is_premium') and user.get('phone'):
                result = send_trip_alert_sms(user['phone'], message)
                if result['status'] == 'success':
                    sent_count += 1
        
        return jsonify({
            "status": "success",
            "message": "Alerts sent",
            "sent_count": sent_count
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =================== TRANSIT CAPACITY MANAGEMENT ===================

@app.route("/api/capacity/<route_code>/<service_time>", methods=["GET"])
def get_availability(route_code, service_time):
    """Check seat availability for a route"""
    try:
        availability = get_route_availability(route_code, service_time)
        
        if not availability:
            return jsonify({"error": "Route/time not found"}), 404
        
        return jsonify({
            "status": "success",
            "route_code": route_code,
            "service_time": service_time,
            "total_capacity": availability['total_capacity'],
            "available_seats": availability['available_seats'],
            "booked_seats": availability['booked_seats'],
            "occupancy_percentage": (availability['booked_seats'] / availability['total_capacity']) * 100
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =================== PAYMENT SIMULATION (Dummy) ===================

@app.route("/api/payment/process", methods=["POST"])
@token_required
def process_payment(user_id):
    """Process dummy payment for order"""
    try:
        data = request.get_json()
        order_id = data.get('order_id')
        amount = data.get('amount')
        card_last_4 = data.get('card_last_4', '****')
        
        # Simulate payment processing
        # In production, integrate with Stripe, PayPal, etc.
        
        order = get_order(order_id)
        if not order:
            return jsonify({"error": "Order not found"}), 404
        
        if order['user_id'] != user_id:
            return jsonify({"error": "Unauthorized"}), 403
        
        # Update order status to confirmed
        update_order_status(order_id, 'confirmed')
        
        return jsonify({
            "status": "success",
            "transaction_id": f"TXN_{secrets.token_hex(8)}",
            "amount": amount,
            "card_last_4": card_last_4,
            "message": "Payment processed successfully",
            "order_status": "confirmed"
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =================== SHOPPING CART (Trip Cart) ===================

@app.route("/api/cart", methods=["GET"])
@token_required
def get_cart(user_id):
    """Get user's trip cart/pending bookings"""
    try:
        pending_orders = get_user_orders(user_id, 'pending')
        
        total_fare = sum(order.get('total_fare', 0) for order in pending_orders)
        
        return jsonify({
            "status": "success",
            "cart_items": pending_orders,
            "item_count": len(pending_orders),
            "total_fare": total_fare
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/cart/<order_id>/remove", methods=["DELETE"])
@token_required
def remove_from_cart(user_id, order_id):
    """Remove trip from cart"""
    try:
        order = get_order(order_id)
        if not order:
            return jsonify({"error": "Order not found"}), 404
        
        if order['user_id'] != user_id:
            return jsonify({"error": "Unauthorized"}), 403
        
        cancel_order(order_id, "Removed from cart")
        
        return jsonify({
            "status": "success",
            "message": "Trip removed from cart"
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =================== PREMIUM FEATURES ===================

@app.route("/api/premium/sms-status", methods=["POST"])
@token_required
def sms_status_update(user_id):
    """Premium feature: Get real-time SMS status updates"""
    try:
        user = get_user(user_id)
        if not user['is_premium']:
            return jsonify({"error": "Premium membership required"}), 403
        
        data = request.get_json()
        order_id = data.get('order_id')
        
        order = get_order(order_id)
        if not order or order['user_id'] != user_id:
            return jsonify({"error": "Order not found"}), 404
        
        # Send SMS update
        if user.get('phone'):
            result = send_trip_status_sms(user['phone'], order_id, "Your trip is on schedule")
            return jsonify({
                "status": "success",
                "message": "SMS sent successfully",
                "sms_result": result
            }), 200
        
        return jsonify({"error": "No phone number on file"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/premium/alerts-subscribe", methods=["POST"])
@token_required
def subscribe_alerts(user_id):
    """Premium feature: Subscribe to SMS alerts"""
    try:
        user = get_user(user_id)
        data = request.get_json()
        alert_types = data.get('alert_types', ['delay', 'disruption', 'promotion'])
        
        # Store alert preferences
        # This would be stored in a preferences table in production
        
        return jsonify({
            "status": "success",
            "message": "Alert subscription updated",
            "subscribed_to": alert_types
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Initialize transit capacity on startup
    init_db()
    init_transit_capacity()
    app.run(debug=True, port=5000)

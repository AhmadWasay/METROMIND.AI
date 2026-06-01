"""
Email and SMS Notification Service for MetroMind AI
Handles confirmation emails and SMS alerts
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Email Configuration
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS", "your-email@gmail.com")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "your-app-password")

# SMS Configuration - Using Twilio Free Trial
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_PHONE = os.getenv("TWILIO_PHONE_NUMBER", "")

# Alternative Free SMS service - Africa's Talking (has free tier)
AFRICASTALKING_API_KEY = os.getenv("AFRICASTALKING_API_KEY", "")
AFRICASTALKING_USERNAME = os.getenv("AFRICASTALKING_USERNAME", "")

def send_order_confirmation_email(user_email, user_name, order_id, trip_plan, total_fare, trip_date):
    """Send order confirmation email"""
    try:
        subject = f"Trip Booking Confirmed - Order #{order_id}"
        
        # Build email body
        segments_html = ""
        if isinstance(trip_plan, dict) and 'segments' in trip_plan:
            for i, segment in enumerate(trip_plan['segments'], 1):
                transit_type = segment.get('type', 'unknown').upper()
                segments_html += f"""
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #ddd;">
                        <strong>Leg {i}: {transit_type}</strong><br>
                        From: {segment.get('from_name', '')} → To: {segment.get('to_name', '')}<br>
                        Duration: {segment.get('duration_mins', 'N/A')} mins | Fare: Rs. {segment.get('fare', '0')}
                    </td>
                </tr>
                """
        
        html_body = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; background-color: #f5f5f5; }}
                    .container {{ max-width: 600px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 8px; }}
                    .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px 8px 0 0; text-align: center; }}
                    .content {{ padding: 20px; }}
                    .order-info {{ background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 15px 0; }}
                    .fare-summary {{ background-color: #e3f2fd; padding: 15px; border-radius: 5px; margin: 15px 0; text-align: center; }}
                    .fare-summary h3 {{ color: #1976d2; margin: 0; }}
                    table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
                    .footer {{ text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; color: #666; font-size: 12px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🚌 MetroMind AI</h1>
                        <p>Your Trip is Confirmed!</p>
                    </div>
                    
                    <div class="content">
                        <p>Hi {user_name},</p>
                        
                        <p>Your trip booking has been confirmed! Here are your trip details:</p>
                        
                        <div class="order-info">
                            <p><strong>Order ID:</strong> {order_id}</p>
                            <p><strong>Trip Date:</strong> {trip_date}</p>
                            <p><strong>Booking Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                        </div>
                        
                        <h3>Journey Segments:</h3>
                        <table>
                            {segments_html}
                        </table>
                        
                        <div class="fare-summary">
                            <h3>Total Fare: Rs. {total_fare}</h3>
                            <p style="margin: 0; color: #666;">You can cancel this trip up to 30 minutes before departure</p>
                        </div>
                        
                        <p><strong>Next Steps:</strong></p>
                        <ul>
                            <li>Check your itinerary in the app</li>
                            <li>Arrive 5 minutes early at your first stop</li>
                            <li>Have your order ID ready for reference</li>
                            <li>If you have a premium account, you'll receive SMS updates</li>
                        </ul>
                        
                        <p>Thank you for using MetroMind AI! 🎉</p>
                    </div>
                    
                    <div class="footer">
                        <p>© 2024 MetroMind AI - Intelligent Transit Planner for Islamabad-Rawalpindi</p>
                        <p>Questions? Reply to this email or check our app for support.</p>
                    </div>
                </div>
            </body>
        </html>
        """
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = GMAIL_ADDRESS
        msg['To'] = user_email
        
        msg.attach(MIMEText(html_body, 'html'))
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            server.send_message(msg)
        
        return {"status": "success", "message": "Confirmation email sent"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def send_order_cancelled_email(user_email, user_name, order_id, cancellation_reason):
    """Send order cancellation email"""
    try:
        subject = f"Order Cancelled - Order #{order_id}"
        
        html_body = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; background-color: #f5f5f5; }}
                    .container {{ max-width: 600px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 8px; }}
                    .header {{ background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 20px; border-radius: 8px 8px 0 0; text-align: center; }}
                    .content {{ padding: 20px; }}
                    .cancel-info {{ background-color: #ffebee; padding: 15px; border-radius: 5px; margin: 15px 0; border-left: 4px solid #f5576c; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Order Cancelled</h1>
                    </div>
                    
                    <div class="content">
                        <p>Hi {user_name},</p>
                        
                        <p>Your trip order has been cancelled.</p>
                        
                        <div class="cancel-info">
                            <p><strong>Order ID:</strong> {order_id}</p>
                            <p><strong>Cancellation Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                            <p><strong>Reason:</strong> {cancellation_reason}</p>
                        </div>
                        
                        <p>Your seat has been released and made available for other commuters. If you need to book another trip, you can do so anytime through the MetroMind AI app.</p>
                        
                        <p>Thank you for using MetroMind AI!</p>
                    </div>
                </div>
            </body>
        </html>
        """
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = GMAIL_ADDRESS
        msg['To'] = user_email
        
        msg.attach(MIMEText(html_body, 'html'))
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            server.send_message(msg)
        
        return {"status": "success", "message": "Cancellation email sent"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def send_status_update_email(user_email, user_name, order_id, status, message):
    """Send trip status update email"""
    try:
        subject = f"Trip Update - Order #{order_id}: {status.upper()}"
        
        html_body = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; background-color: #f5f5f5; }}
                    .container {{ max-width: 600px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 8px; }}
                    .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px 8px 0 0; text-align: center; }}
                    .content {{ padding: 20px; }}
                    .status-badge {{ display: inline-block; background-color: #4caf50; color: white; padding: 10px 15px; border-radius: 5px; font-weight: bold; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🚌 Trip Status Update</h1>
                    </div>
                    
                    <div class="content">
                        <p>Hi {user_name},</p>
                        
                        <p>Your trip (Order #{order_id}) has been updated:</p>
                        
                        <p><span class="status-badge">{status.upper()}</span></p>
                        
                        <p>{message}</p>
                        
                        <p>Check the MetroMind AI app for live tracking and more details.</p>
                    </div>
                </div>
            </body>
        </html>
        """
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = GMAIL_ADDRESS
        msg['To'] = user_email
        
        msg.attach(MIMEText(html_body, 'html'))
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            server.send_message(msg)
        
        return {"status": "success", "message": "Status update email sent"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# =================== SMS NOTIFICATIONS ===================

def send_sms_via_twilio(phone_number, message):
    """Send SMS using Twilio (Free tier includes credits)"""
    try:
        if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
            return {"status": "error", "message": "Twilio not configured"}
        
        from twilio.rest import Client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=phone_number
        )
        
        return {"status": "success", "message_sid": message.sid}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def send_sms_via_africastalking(phone_number, message):
    """Send SMS using Africa's Talking (Free tier available for Pakistan)"""
    try:
        if not AFRICASTALKING_API_KEY or not AFRICASTALKING_USERNAME:
            return {"status": "error", "message": "Africa's Talking not configured"}
        
        url = "https://api.sandbox.africastalking.com/version1/messaging"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            "ApiKey": AFRICASTALKING_API_KEY
        }
        
        data = {
            "username": AFRICASTALKING_USERNAME,
            "message": message,
            "recipients": phone_number
        }
        
        response = requests.post(url, headers=headers, data=data)
        return {"status": "success" if response.status_code == 200 else "error", "response": response.json()}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

def send_trip_confirmation_sms(phone_number, order_id, trip_date):
    """Send SMS confirmation for premium users"""
    message = f"MetroMind: Your trip (Order #{order_id}) is confirmed for {trip_date}. Track live in the app!"
    
    # Try Twilio first, then Africa's Talking
    result = send_sms_via_twilio(phone_number, message)
    if result["status"] == "error":
        result = send_sms_via_africastalking(phone_number, message)
    
    return result

def send_trip_status_sms(phone_number, order_id, status_message):
    """Send SMS status update for premium users"""
    message = f"MetroMind: {status_message} (Order #{order_id})"
    
    result = send_sms_via_twilio(phone_number, message)
    if result["status"] == "error":
        result = send_sms_via_africastalking(phone_number, message)
    
    return result

def send_trip_alert_sms(phone_number, alert_message):
    """Send urgent SMS alerts (premium feature)"""
    message = f"🚨 MetroMind Alert: {alert_message}"
    
    result = send_sms_via_twilio(phone_number, message)
    if result["status"] == "error":
        result = send_sms_via_africastalking(phone_number, message)
    
    return result

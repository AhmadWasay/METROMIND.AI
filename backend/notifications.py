import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import twilio.rest
import africastalking
import json # For trip_plan in email

# Force python-dotenv to look in the exact backend directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

# Twilio Configuration
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER") # Your Twilio phone number

# Africa's Talking Configuration
AFRICASTALKING_API_KEY = os.getenv("AFRICASTALKING_API_KEY")
AFRICASTALKING_USERNAME = os.getenv("AFRICASTALKING_USERNAME")

# Initialize Twilio client
twilio_client = None
if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
    try:
        twilio_client = twilio.rest.Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    except Exception as e:
        print(f"WARNING: Could not initialize Twilio client: {e}")

# Initialize Africa's Talking client
africastalking_sms = None
if AFRICASTALKING_API_KEY and AFRICASTALKING_USERNAME:
    try:
        africastalking.initialize(AFRICASTALKING_USERNAME, AFRICASTALKING_API_KEY)
        africastalking_sms = africastalking.SMS
    except Exception as e:
        print(f"WARNING: Could not initialize Africa's Talking client: {e}")

def _send_email(recipient_email, subject, text_content, html_content):
    if not GMAIL_ADDRESS or not GMAIL_APP_PASSWORD:
        print("CRITICAL ERROR: Gmail credentials not found in .env file. Email sending disabled.")
        return {"status": "error", "message": "Email service not configured."}

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = f"MetroMind AI <{GMAIL_ADDRESS}>"
    message["To"] = recipient_email

    message.attach(MIMEText(text_content, "plain"))
    message.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            server.sendmail(GMAIL_ADDRESS, recipient_email, message.as_string())
        return {"status": "success", "message": "Email sent successfully."}
    except Exception as e:
        print(f"ERROR: Failed to send email to {recipient_email}. Error: {e}")
        return {"status": "error", "message": f"Failed to send email: {e}"}

def send_otp_email(recipient_email: str, otp: str):
    subject = f"Your MetroMind AI Verification Code: {otp}"
    text = f"Hi,\n\nYour verification code is: {otp}\nThis code will expire in 10 minutes.\n\nThanks,\nThe MetroMind AI Team"
    html = f"""
    <html>
        <body>
            <h3>Your MetroMind AI Verification Code is: <strong>{otp}</strong></h3>
            <p>This code will expire in 10 minutes.</p>
            <p>If you did not request this, please ignore this email.</p>
        </body>
    </html>
    """
    return _send_email(recipient_email, subject, text, html)

def send_order_confirmation_email(recipient_email, full_name, order_id, trip_plan, total_fare, trip_date):
    # Format the trip details to be human-readable instead of raw JSON
    route_name = trip_plan.get('name', 'Your Route')
    route_desc = trip_plan.get('description', '')
    est_time = trip_plan.get('estimated_time_minutes', 0)
    
    # Build a plain text list of segments
    segments_text = ""
    # Build an HTML list of segments
    segments_html = "<ul>"
    
    for seg in trip_plan.get('journey_segments', []):
        line = seg.get('line') or seg.get('route') or seg.get('type', 'transit').capitalize()
        segments_text += f"  - {seg.get('from')} to {seg.get('to')} via {line} ({seg.get('time_mins')} mins)\n"
        segments_html += f"<li><strong>{seg.get('from')}</strong> to <strong>{seg.get('to')}</strong> via {line} ({seg.get('time_mins')} mins)</li>"
        
    segments_html += "</ul>"
    
    trip_details_html = f"""
    <p><strong>Route:</strong> {route_name}<br>
    <strong>Time:</strong> {est_time} mins<br>
    <strong>Details:</strong> {route_desc}</p>
    <p><strong>Segments:</strong></p>
    {segments_html}
    """

    subject = f"MetroMind AI: Your Trip Booking #{order_id} is Confirmed!"
    text = f"""
    Dear {full_name},

    Your trip booking with MetroMind AI has been confirmed!

    Order ID: {order_id}
    Trip Date: {trip_date}
    Total Fare: PKR {total_fare}

    Trip Details:
    Route: {route_name}
    Time: {est_time} mins
    Details: {route_desc}
    
    Segments:
{segments_text}

    Thank you for choosing MetroMind AI!

    Best regards,
    The MetroMind AI Team
    """
    html = f"""
    <html>
        <body>
            <p>Dear {full_name},</p>
            <p>Your trip booking with MetroMind AI has been confirmed!</p>
            <p><strong>Order ID:</strong> {order_id}</p>
            <p><strong>Trip Date:</strong> {trip_date}</p>
            <p><strong>Total Fare:</strong> PKR {total_fare}</p>
            <h3>Trip Details:</h3>
            {trip_details_html}
            <p>Thank you for choosing MetroMind AI!</p>
            <p>Best regards,<br>The MetroMind AI Team</p>
        </body>
    </html>
    """
    return _send_email(recipient_email, subject, text, html)

def send_order_cancelled_email(recipient_email, full_name, order_id, reason):
    subject = f"MetroMind AI: Your Trip Booking #{order_id} has been Cancelled"
    text = f"""
    Dear {full_name},

    Your trip booking #{order_id} with MetroMind AI has been cancelled.

    Reason: {reason}

    If you have any questions, please contact support.

    Best regards,
    The MetroMind AI Team
    """
    html = f"""
    <html>
        <body>
            <p>Dear {full_name},</p>
            <p>Your trip booking <strong>#{order_id}</strong> with MetroMind AI has been cancelled.</p>
            <p><strong>Reason:</strong> {reason}</p>
            <p>If you have any questions, please contact support.</p>
            <p>Best regards,<br>The MetroMind AI Team</p>
        </body>
    </html>
    """
    return _send_email(recipient_email, subject, text, html)

def send_status_update_email(recipient_email, full_name, order_id, new_status, message):
    subject = f"MetroMind AI: Update for Trip Booking #{order_id} - {new_status.capitalize()}"
    text = f"""
    Dear {full_name},

    There's an update for your trip booking #{order_id}.

    New Status: {new_status.capitalize()}
    Message: {message}

    Thank you for choosing MetroMind AI!

    Best regards,
    The MetroMind AI Team
    """
    html = f"""
    <html>
        <body>
            <p>Dear {full_name},</p>
            <p>There's an update for your trip booking <strong>#{order_id}</strong>.</p>
            <p><strong>New Status:</strong> {new_status.capitalize()}</p>
            <p><strong>Message:</strong> {message}</p>
            <p>Thank you for choosing MetroMind AI!</p>
            <p>Best regards,<br>The MetroMind AI Team</p>
        </body>
    </html>
    """
    return _send_email(recipient_email, subject, text, html)

def _send_sms_via_twilio(to_number, message):
    if not twilio_client or not TWILIO_PHONE_NUMBER:
        print("WARNING: Twilio not configured. Cannot send SMS.")
        return {"status": "error", "message": "Twilio not configured."}
    try:
        message_obj = twilio_client.messages.create(
            to=to_number,
            from_=TWILIO_PHONE_NUMBER,
            body=message
        )
        return {"status": "success", "message_sid": message_obj.sid}
    except Exception as e:
        print(f"ERROR: Twilio SMS failed to {to_number}: {e}")
        return {"status": "error", "message": str(e)}

def _send_sms_via_africastalking(to_number, message):
    if not africastalking_sms:
        print("WARNING: Africa's Talking not configured. Cannot send SMS.")
        return {"status": "error", "message": "Africa's Talking not configured."}
    try:
        # Africa's Talking expects numbers in international format without '+'
        if to_number.startswith('+'):
            to_number = to_number[1:]
        response = africastalking_sms.send(message, [to_number])
        # Check response for success/failure
        if response and response['SMSMessageData']['Recipients'][0]['status'] == 'Success':
            return {"status": "success", "message_id": response['SMSMessageData']['Recipients'][0]['messageId']}
        else:
            print(f"ERROR: Africa's Talking SMS failed to {to_number}: {response}")
            return {"status": "error", "message": response}
    except Exception as e:
        print(f"ERROR: Africa's Talking SMS failed to {to_number}: {e}")
        return {"status": "error", "message": str(e)}

def send_sms(to_number, message):
    """Attempt to send SMS via Twilio, fallback to Africa's Talking."""
    if not to_number:
        return {"status": "error", "message": "No phone number provided."}
    
    # Try Twilio first
    twilio_result = _send_sms_via_twilio(to_number, message)
    if twilio_result['status'] == 'success':
        return twilio_result
    
    print("INFO: Twilio failed, attempting Africa's Talking fallback.")
    # Fallback to Africa's Talking
    africastalking_result = _send_sms_via_africastalking(to_number, message)
    if africastalking_result['status'] == 'success':
        return africastalking_result
    
    return {"status": "error", "message": "All SMS providers failed."}

def send_trip_confirmation_sms(phone, order_id, trip_date):
    message = f"MetroMind AI: Your trip #{order_id} on {trip_date} is confirmed. Thank you!"
    return send_sms(phone, message)

def send_trip_status_sms(phone, order_id, status):
    message = f"MetroMind AI: Update for trip #{order_id}. Status: {status}. Track in app."
    return send_sms(phone, message)

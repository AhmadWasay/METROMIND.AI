#!/usr/bin/env python3
"""
Setup and verification script for MetroMind AI backend
"""

import os
import sys

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    print("=" * 60)
    print("🚀 MetroMind AI - Backend Setup & Verification")
    print("=" * 60)
    
    # Initialize database
    print("\n1️⃣  Initializing database...")
    from models import init_db, init_transit_capacity, create_user, get_db
    init_db()
    print("   ✅ Database initialized")
    
    # Initialize transit capacity
    print("\n2️⃣  Initializing transit capacity...")
    init_transit_capacity()
    print("   ✅ Transit capacity initialized")
    
    # Create demo users
    print("\n3️⃣  Creating demo users...")
    
    demo_users = [
        {
            "email": "demo@metromind.com",
            "password": "demo123",
            "full_name": "Demo User",
            "phone": "03001234567"
        },
        {
            "email": "admin@metromind.com",
            "password": "admin123",
            "full_name": "Admin User",
            "phone": "03009876543"
        },
        {
            "email": "premium@metromind.com",
            "password": "premium123",
            "full_name": "Premium User",
            "phone": "03005555555"
        }
    ]
    
    for user_data in demo_users:
        result = create_user(
            user_data["email"],
            user_data["password"],
            user_data["full_name"],
            user_data["phone"]
        )
        if result['status'] == 'success':
            print(f"   ✅ Created: {user_data['email']}")
        else:
            print(f"   ℹ️  {user_data['email']}: {result.get('message', 'Already exists')}")
    
    # Upgrade one user to premium
    from models import get_user, upgrade_to_premium
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT user_id FROM users WHERE email = ?', ('premium@metromind.com',))
    user_row = c.fetchone()
    if user_row:
        upgrade_to_premium(user_row['user_id'])
        print("   ✅ Upgraded premium@metromind.com to premium tier")
    conn.close()
    
    # Check email configuration
    print("\n4️⃣  Checking email configuration...")
    from dotenv import load_dotenv
    load_dotenv()
    
    gmail_addr = os.getenv('GMAIL_ADDRESS', '')
    gmail_pass = os.getenv('GMAIL_APP_PASSWORD', '')
    
    if gmail_addr and gmail_pass:
        print(f"   ✅ Gmail configured: {gmail_addr}")
        print("   📧 Email confirmations will be sent")
    else:
        print("   ⚠️  Gmail not configured")
        print("   📧 Email confirmations will NOT be sent")
        print("   💡 Setup: See .env.example for instructions")
    
    # Check SMS configuration
    print("\n5️⃣  Checking SMS configuration...")
    
    twilio_sid = os.getenv('TWILIO_ACCOUNT_SID', '')
    africastalking_key = os.getenv('AFRICASTALKING_API_KEY', '')
    
    if twilio_sid:
        print("   ✅ Twilio configured")
        print("   📱 SMS alerts will be sent to premium users")
    elif africastalking_key:
        print("   ✅ Africa's Talking configured")
        print("   📱 SMS alerts will be sent to premium users")
    else:
        print("   ℹ️  SMS not configured (optional)")
        print("   💡 Setup: See .env.example for instructions")
    
    # Print summary
    print("\n" + "=" * 60)
    print("✨ Backend Setup Complete!")
    print("=" * 60)
    
    print("\n📊 Demo Credentials:")
    print("   Regular User: demo@metromind.com / demo123")
    print("   Admin User: admin@metromind.com / admin123")
    print("   Premium User: premium@metromind.com / premium123")
    
    print("\n🔧 Admin Token: admin_secret (change in .env for production)")
    
    print("\n🚀 To start the backend server:")
    print("   python main.py")
    print("\n📚 API will be available at: http://localhost:5000")
    print("   Documentation: http://localhost:5000/")
    
    print("\n" + "=" * 60)
    print("✅ All systems ready!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

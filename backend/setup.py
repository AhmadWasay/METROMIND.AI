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
    from models import init_db, init_transit_capacity
    init_db()
    print("   ✅ Database initialized")
    
    # Initialize transit capacity
    print("\n2️⃣  Initializing transit capacity...")
    init_transit_capacity()
    print("   ✅ Transit capacity initialized")
    
    # Check email configuration
    print("\n3️⃣  Checking email configuration...")
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
    print("\n4️⃣  Checking SMS configuration...")
    
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

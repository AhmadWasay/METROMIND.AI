# MetroMind AI - Quick Start & Testing Guide

## 🚀 Quick Setup (5 Minutes)

### Backend Setup

```bash
# 1. Navigate to backend
cd backend

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
copy .env.example .env  # Windows
cp .env.example .env    # Mac/Linux

# 5. Configure .env (IMPORTANT)
# Edit .env and add:
GMAIL_ADDRESS=your-email@gmail.com
GMAIL_APP_PASSWORD=your-app-password
# Leave SMS empty for now (optional)

# 6. Run backend
python main.py
# API running at http://localhost:5000
```

### Frontend Setup

```bash
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Create .env.local
echo REACT_APP_API_URL=http://localhost:5000 > .env.local

# 4. Start development server
npm start
# App running at http://localhost:3000
```

---

## 📋 Testing Checklist

### Test 1: User Registration & Authentication
```
1. Go to http://localhost:3000
2. Click "Login" button (look for auth modal)
3. Click "Sign Up" tab
4. Fill in:
   - Email: testuser@example.com
   - Password: test123
   - Full Name: Test User
   - Phone: 03001234567
5. Click Sign Up
✅ Should see success and user_id in console
```

### Test 2: User Login
```
1. Logout (if signed up)
2. Click Login
3. Enter:
   - Email: testuser@example.com
   - Password: test123
4. Click Login
✅ Should see success and get user_id
```

### Test 3: Trip Booking & Cart
```
1. Login as user
2. Search for trip (e.g., Red_Sector_G7 → Blue_Adiala_Road)
3. Click "Book Trip"
4. View cart (should see trip with fare)
5. Click "Proceed to Payment"
✅ Should see payment confirmation
✅ Check email for confirmation (spam folder)
```

### Test 4: Order Confirmation Email
```
1. Complete booking
2. Check your email
✅ Should receive HTML email with:
   - Order ID
   - Journey details
   - Total fare
   - Next steps
```

### Test 5: View My Orders
```
1. Login as user
2. Click "My Orders" or "Bookings"
3. View all orders with statuses
✅ Should see the trip you just booked as "pending"
```

### Test 6: Order Status & Tracking
```
1. Click on an order
2. Click "Track Live"
✅ Should see:
   - Current status
   - Live location
   - Estimated arrival
   - Progress bar
```

### Test 7: Rate a Trip
```
1. View a completed trip
2. Click "Rate Trip"
3. Select 4-5 stars
4. Add review
5. Submit
✅ Should see confirmation
✅ Order updated with rating
```

### Test 8: Cancel Booking
```
1. View a pending trip
2. Click "Cancel Booking"
3. Confirm cancellation
✅ Should see status changed to "cancelled"
✅ Check email for cancellation notice
```

### Test 9: Admin Dashboard
```
1. Go to http://localhost:3000/admin
2. Click "Admin Login"
3. Enter token: admin_secret
✅ Should see admin dashboard

4. Click "Overview" tab
✅ Should see statistics (total orders, revenue, etc.)

5. Click "Orders" tab
✅ Should see all orders with status indicators
✅ Can change status from dropdown

6. Click "Users" tab
✅ Should see all registered users with details

7. Click "Notifications" tab
✅ Should see pending email/SMS notifications
```

### Test 10: Stock/Capacity Management
```
1. API Call (Postman/curl):
   GET http://localhost:5000/api/capacity/R-2/08:00
   
✅ Should return:
{
    "available_seats": 80,
    "booked_seats": 0,
    "occupancy_percentage": 0
}

2. After booking, check again
✅ available_seats should decrease
```

### Test 11: Premium SMS Feature (Optional)
```
1. Setup Twilio account (free $10-20 credits)
2. Add credentials to .env:
   TWILIO_ACCOUNT_SID=...
   TWILIO_AUTH_TOKEN=...
   TWILIO_PHONE_NUMBER=...

3. Upgrade user to premium:
   POST http://localhost:5000/api/auth/upgrade-premium
   Header: X-User-ID=your_user_id

4. Book a trip with phone number on file
✅ Should receive SMS confirmation
```

---

## 🔍 API Testing (Postman/cURL)

### Create User (Signup)
```bash
curl -X POST http://localhost:5000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@test.com",
    "password": "pass123",
    "full_name": "Test User",
    "phone": "03001234567"
  }'
```

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@test.com",
    "password": "pass123"
  }'
# Returns: {"user_id": "user_xxx", "is_premium": false}
```

### Create Order
```bash
curl -X POST http://localhost:5000/api/orders/create \
  -H "Content-Type: application/json" \
  -H "X-User-ID: user_xxx" \
  -d '{
    "source": "Red_Sector_G7",
    "destination": "Blue_Adiala_Road",
    "trip_plan": {"segments": [{"from_name": "G7", "to_name": "Adiala", "fare": 30, "duration_mins": 20}]},
    "trip_date": "2024-06-15",
    "total_fare": 30
  }'
```

### Get User Orders
```bash
curl -X GET http://localhost:5000/api/orders/user/user_xxx \
  -H "X-User-ID: user_xxx"
```

### Admin Dashboard
```bash
curl -X GET http://localhost:5000/api/admin/dashboard \
  -H "X-Admin-Token: admin_secret"
```

### View All Orders (Admin)
```bash
curl -X GET http://localhost:5000/api/admin/orders \
  -H "X-Admin-Token: admin_secret"
```

### Update Order Status (Admin)
```bash
curl -X PUT http://localhost:5000/api/orders/order_xxx/update-status \
  -H "Content-Type: application/json" \
  -H "X-Admin-Token: admin_secret" \
  -d '{
    "status": "in_transit",
    "message": "Your trip has started"
  }'
```

---

## 📧 Testing Email Manually

### Using Gmail Test
```python
from notifications import send_order_confirmation_email

result = send_order_confirmation_email(
    user_email="your-email@gmail.com",
    user_name="Test User",
    order_id="test_order_123",
    trip_plan={"segments": [
        {"from_name": "Location A", "to_name": "Location B", "fare": 30, "duration_mins": 20}
    ]},
    total_fare=30,
    trip_date="2024-06-15"
)
print(result)
```

### Check Spam Folder
- First email test might land in spam
- Mark as "Not Spam" to improve delivery
- Future emails will go to inbox

---

## 🔧 Troubleshooting

### "Gmail authentication failed"
```
1. Verify 2FA enabled: myaccount.google.com/security
2. Generate app password: myaccount.google.com/apppasswords
3. Copy 16-char password (remove spaces)
4. Update .env: GMAIL_APP_PASSWORD=abcdefghijklmnop
```

### "SMS not sending"
```
1. Check Twilio/Africa's Talking account balance
2. Verify phone number format: +923001234567
3. Check credentials in .env
4. Ensure premium user (is_premium=1 in DB)
```

### "CORS error"
```
1. Make sure backend is running on http://localhost:5000
2. Add to main.py: CORS(app, origins=['http://localhost:3000'])
3. Verify REACT_APP_API_URL in frontend .env.local
```

### "Database locked"
```
1. Delete metromind.db
2. Backend will recreate on next run
3. Re-initialize capacity: init_transit_capacity()
```

---

## 📱 Demo Flow (Complete End-to-End)

### Scenario: User books and receives notifications

```
1. [USER] Signs up
   → Gets user_id
   
2. [USER] Plans trip
   → Sees options
   → Selects one
   
3. [USER] Confirms booking
   → Order created in DB
   → Seat allocated
   
4. [SYSTEM] Sends email confirmation
   → HTML email with details
   → Order ID, fare, journey
   
5. [ADMIN] Views dashboard
   → Sees new order in stats
   → Can update status
   
6. [ADMIN] Updates status to "in_transit"
   → System sends email notification
   → If premium + phone: SMS sent
   
7. [USER] Checks "My Orders"
   → Sees booking with status
   → Can track live location
   
8. [ADMIN] Updates status to "completed"
   
9. [USER] Rates trip
   → Adds 5-star rating + review
   → Saved to database
   
10. [USER] Cancels another trip
    → Seat released
    → Cancellation email sent
```

---

## ✅ Verification Checklist

Before submission, verify:

- [ ] Backend running without errors
- [ ] Frontend connects to backend
- [ ] User signup/login works
- [ ] Can book a trip
- [ ] Confirmation email received
- [ ] Admin can login
- [ ] Admin can view orders/users
- [ ] Order status can be updated
- [ ] Notifications appear in queue
- [ ] Stock/capacity decreases on booking
- [ ] Order can be cancelled
- [ ] Cancellation email received

---

## 📦 File Structure

```
metromind-ai/
├── backend/
│   ├── main.py                 (Original trip planner)
│   ├── api_extended.py         (NEW - 30+ new endpoints)
│   ├── models.py              (NEW - Database layer)
│   ├── notifications.py       (NEW - Email & SMS)
│   ├── requirements.txt        (UPDATED)
│   ├── .env.example           (NEW - Config template)
│   └── metromind.db           (AUTO-CREATED)
│
├── frontend/
│   ├── src/
│   │   ├── App.js             (Main app)
│   │   ├── components/
│   │   │   ├── AdminDashboard.js      (NEW)
│   │   │   ├── AdminDashboard.css     (NEW)
│   │   │   ├── AuthModal.js           (NEW)
│   │   │   ├── AuthModal.css          (NEW)
│   │   │   ├── OrderManager.js        (NEW)
│   │   │   ├── OrderManager.css       (NEW)
│   │   │   └── ... (existing components)
│   │   └── .env.local         (Create with API_URL)
│   └── package.json
│
├── FEATURES_IMPLEMENTATION.md  (NEW - Comprehensive guide)
├── README.md
└── ... (other docs)
```

---

## 🎯 Expected Test Results

| Test | Expected | Status |
|---|---|---|
| Signup | New user created, email unique | ✅ |
| Login | User authenticated, token returned | ✅ |
| Book Trip | Order created, seat allocated | ✅ |
| Email Sent | HTML email in inbox/spam | ✅ |
| Admin Login | Dashboard loads | ✅ |
| Status Update | Email notification sent | ✅ |
| Cancel Order | Seat released, email sent | ✅ |
| SMS Alert | (Premium) SMS received | ✅ |

---

**Ready to test? Start with backend setup above!**

Last updated: June 2024

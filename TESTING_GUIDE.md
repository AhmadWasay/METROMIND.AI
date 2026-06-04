# 🧪 MetroMind AI - Complete Testing Guide

This guide provides step-by-step instructions to test all features of the MetroMind AI application.

---

## 📋 Pre-Testing Checklist

Before starting tests, ensure:

- [ ] Backend dependencies installed: `pip install -r requirements.txt`
- [ ] Database initialized: `python setup.py`
- [ ] Backend running: `python main.py` (Terminal 1)
- [ ] Frontend dependencies installed: `npm install`
- [ ] Frontend running: `npm start` (Terminal 2)
- [ ] Browser open to http://localhost:3000
- [ ] Optional: Email configured in `.env` for confirmation testing

---

## ✅ Test Suite

### TEST 1: Application Startup & Health Check

**Objective:** Verify app launches without errors

**Steps:**
```
1. Terminal 1: Navigate to backend/
2. Run: python main.py
3. Verify: "🚀 Starting MetroMind API" message appears
4. Check: http://localhost:5000/ loads

Terminal 3: 
5. Run: curl http://localhost:5000/api/health
6. Verify: Returns {"status": "healthy", ...}

Terminal 2: Navigate to frontend/
7. Run: npm start
8. Verify: "Compiled successfully" message appears
9. Browser: Navigate to http://localhost:3000
10. Verify: MetroMind homepage loads with search bar
```

**Expected Results:**
- ✅ Both servers start without errors
- ✅ No red error messages in console
- ✅ Frontend loads with navigation buttons
- ✅ Search bar is visible

---

### TEST 2: User Signup

**Objective:** Create new user account via signup form

**Steps:**
```
1. Go to http://localhost:3000
2. Click "🔐 Login / Sign Up" button
3. Click "Sign Up" tab in modal
4. Fill form:
   Email: testuser@example.com
   Password: TestPass123
   Full Name: Test User
   Phone: 03001234567
5. Click "Sign Up" button
6. Wait for response (1-2 seconds)
7. Verify success message appears
```

**Expected Results:**
- ✅ Form submits successfully
- ✅ "Account created successfully!" message shown
- ✅ Modal closes automatically
- ✅ User is automatically logged in
- ✅ Header shows "📦 My Bookings" button

**Backend Verification:**
```bash
# Check user was created
sqlite3 backend/metromind.db "SELECT * FROM users WHERE email='testuser@example.com';"
```

---

### TEST 3: User Login

**Objective:** Verify existing user can login

**Steps:**
```
1. From logged-in state, click "🚪 Logout"
2. Verify: "🔐 Login / Sign Up" button returns
3. Click "🔐 Login / Sign Up"
4. Use demo credentials:
   Email: demo@metromind.com
   Password: demo123
5. Click "Login" button
6. Wait for response
7. Verify: Logged in successfully
```

**Expected Results:**
- ✅ Login successful message shown
- ✅ Modal closes
- ✅ Header shows "📦 My Bookings"
- ✅ User ID saved in browser localStorage

**Browser DevTools Check:**
```javascript
// In browser console (F12 -> Console):
console.log(localStorage.getItem('user_id'));
// Should show: USR_XXXXXX or similar
```

---

### TEST 4: Trip Search & Routing

**Objective:** Test trip planning functionality

**Steps:**
```
1. Ensure logged in (or on planner view)
2. Select source: "Islamabad Airport (ISB)"
3. Select destination: "Peshawar (PEW)"
4. Click "🔍 Plan Trip" button
5. Wait 2-3 seconds for results
6. Verify: Multiple itineraries appear
```

**Expected Results:**
- ✅ Results load showing 2-4 different routes
- ✅ Each route shows:
   - Source → Destination
   - Segments (metro/bus lines)
   - Journey time
   - Total fare
   - Number of transfers

---

### TEST 5: Trip Booking

**Objective:** Book a trip and create order

**Steps:**
```
1. From trip results, select any itinerary
2. Click "🎫 Book This Trip" button
3. Wait 1-2 seconds for processing
4. Verify: Success message appears
5. Expected message: "✅ Trip booked!"
```

**Expected Results:**
- ✅ Booking success message
- ✅ Page automatically switches to "📦 My Bookings"
- ✅ New booking appears in list
- ✅ Order status shows "pending"

**Optional Email Check:**
```
If Gmail is configured:
- Check inbox for "Trip Confirmation" email
- Email should contain:
  - Order ID
  - Journey details
  - Fare amount
  - Trip date
```

**Backend Check:**
```bash
# View orders in database
sqlite3 backend/metromind.db \
  "SELECT order_id, user_id, source, destination, status FROM orders ORDER BY created_at DESC LIMIT 5;"
```

---

### TEST 6: Order Tracking

**Objective:** View real-time order status and details

**Steps:**
```
1. In "📦 My Bookings" tab
2. Find the booking from TEST 5
3. Click on the order card
4. Verify: Modal opens showing:
   - Order ID
   - Source & Destination
   - Status badge
   - Progress bar
5. Click "📍 Track Live" button
6. Verify: Detailed tracking info appears:
   - Current status
   - Current location
   - Next milestone
   - Estimated time
```

**Expected Results:**
- ✅ Order details modal loads
- ✅ All information displayed correctly
- ✅ Progress bar shows journey progress
- ✅ Status color matches status type

**Status Color Reference:**
- 🔵 Pending (Light Blue)
- 🟢 Confirmed (Green)
- 🟡 In Transit (Yellow)
- 🟣 Completed (Purple)
- 🔴 Cancelled (Red)

---

### TEST 7: Order Cancellation

**Objective:** Cancel pending order and verify email

**Steps:**
```
1. Book a new trip (TEST 5) to have pending order
2. In "📦 My Bookings" tab
3. Find pending order
4. Click "✕ Cancel Booking" button
5. Confirm cancellation in dialog
6. Wait 1-2 seconds
7. Verify: Success message appears
```

**Expected Results:**
- ✅ Order status changes to "cancelled"
- ✅ Cancellation email sent (check inbox)
- ✅ Seat released (capacity increased)

**Email Verification:**
```
Subject: Trip Cancellation - MetroMind
Contains:
- Order ID
- Cancellation timestamp
- Reason: "User requested cancellation"
- Refund confirmation
```

**Database Check:**
```bash
sqlite3 backend/metromind.db \
  "SELECT order_id, status, cancellation_reason FROM orders ORDER BY updated_at DESC LIMIT 1;"
```

---

### TEST 8: Order Rating

**Objective:** Rate a completed trip

**Steps:**
```
1. Have a completed order (admin can set status to completed)
2. In "📦 My Bookings" tab, filter by "completed"
3. Find completed order
4. Click "⭐ Rate Trip" button
5. Select rating (click stars): 5 stars
6. Enter review: "Great service! Very comfortable."
7. Click "Submit Rating"
8. Verify: Success message
```

**Expected Results:**
- ✅ Rating submission successful
- ✅ Star rating displayed on order card
- ✅ Review saved to database
- ✅ Rating removed from "My Bookings" (not shown for completed trips)

**Database Verification:**
```bash
sqlite3 backend/metromind.db \
  "SELECT order_id, rating, review FROM orders WHERE rating > 0;"
```

---

### TEST 9: Admin Panel Access

**Objective:** Access admin dashboard with credentials

**Steps:**
```
1. Click "🎛️ Admin" button in header
   (appears only if logged in)
2. Modal appears asking for admin token
3. Enter: admin_secret
4. Click "Login as Admin"
5. Wait 1-2 seconds
6. Verify: Admin dashboard loads
```

**Expected Results:**
- ✅ Admin panel loads successfully
- ✅ Tab navigation visible:
   - 📊 Overview
   - 📦 Orders
   - 👥 Users
   - 📬 Notifications
   - 📢 Send Alerts
- ✅ No errors in console

---

### TEST 10: Admin Dashboard - Overview

**Objective:** View statistics and system health

**Steps:**
```
1. In Admin panel, stay on "📊 Overview" tab
2. Verify visible statistics cards:
   - Total Orders: count > 0
   - Pending: count (orders)
   - Confirmed: count (orders)
   - In Transit: count (orders)
   - Completed: count (orders)
   - Cancelled: count (orders)
   - Total Revenue: show fare total
   - Average Rating: show average (1-5)
   - Total Users: count
   - Premium Users: count
   - Top Routes: top 3 routes by booking count
```

**Expected Results:**
- ✅ All statistics cards load
- ✅ Numbers make sense (match database)
- ✅ No zero-division errors
- ✅ Top routes show actual trip pairs

---

### TEST 11: Admin Panel - Orders Management

**Objective:** View and update orders via admin

**Steps:**
```
1. Click "📦 Orders" tab in admin panel
2. Verify: Table shows all orders with columns:
   - Order ID
   - User Email
   - Route
   - Fare
   - Status
   - Date
3. Find an order with status "pending" or "confirmed"
4. Click on order row
5. Click "Update Status" dropdown
6. Select: "in_transit"
7. Click "Save"
8. Wait 1-2 seconds
9. Verify: Status updated on screen
```

**Expected Results:**
- ✅ Orders table loads all bookings
- ✅ Status dropdown shows all options
- ✅ Status updates successfully
- ✅ Table refreshes with new status
- ✅ Update email sent to user

**Email Verification:**
```
Subject: Order Status Update - MetroMind
Contains:
- Order ID
- New status: In Transit
- Updated timestamp
- Estimated completion time
```

---

### TEST 12: Admin Panel - Users

**Objective:** View all users and premium status

**Steps:**
```
1. Click "👥 Users" tab
2. Verify: Table shows all users with:
   - Email
   - Full Name
   - Phone
   - Premium Status (Yes/No)
   - Created Date
   - Last Login
3. Scroll down to see multiple users
```

**Expected Results:**
- ✅ All created users appear in table
- ✅ Premium status correctly shows for premium@metromind.com
- ✅ Regular users show "No"
- ✅ Dates are formatted correctly

---

### TEST 13: Seat Capacity Management

**Objective:** Verify seats allocated/released on booking

**Steps:**
```
1. Check initial capacity:
   curl "http://localhost:5000/api/capacity/R-2/08:00"

2. Book a trip on route R-2
3. Check capacity again:
   curl "http://localhost:5000/api/capacity/R-2/08:00"

4. Verify: available_seats decreased by 1
5. Cancel the booking
6. Check capacity one more time
7. Verify: available_seats increased by 1
```

**Expected Results:**
- ✅ Initial: available_seats = X, total = 60
- ✅ After booking: available_seats = X-1
- ✅ After cancellation: available_seats = X

**Backend API Response:**
```json
{
  "status": "success",
  "route_code": "R-2",
  "time": "08:00",
  "total_seats": 60,
  "available_seats": 45,
  "occupied_percentage": 25
}
```

---

### TEST 14: Premium Features (SMS) - Optional

**Objective:** Test SMS alerts for premium users

**Prerequisites:**
- Twilio or Africa's Talking API key configured in .env
- Account with SMS balance

**Steps:**
```
1. Admin panel → Users tab
2. Find premium@metromind.com (already premium)
3. Login as this premium user (logout first)
4. Book a trip
5. Wait 2-3 seconds for SMS
6. Check phone for confirmation SMS
```

**Expected Results:**
- ✅ SMS received within 2-3 seconds
- ✅ SMS contains: Order ID, route, fare, time
- ✅ No errors in backend logs

**SMS Format:**
```
MetroMind: Your booking confirmed!
Order: ORD_XXXXX
Route: Source → Destination
Fare: PKR XXXX
Date: YYYY-MM-DD
Track: https://metromind.com/track/XXXXX
```

---

### TEST 15: Notifications Queue

**Objective:** View pending notifications

**Steps:**
```
1. Admin panel → "📬 Notifications" tab
2. Verify: Table shows pending notifications
3. Each row should have:
   - Notification ID
   - Type (email/sms)
   - Channel
   - Recipient
   - Message preview
   - Status (pending/sent)
   - Timestamp
```

**Expected Results:**
- ✅ Recent notifications appear in queue
- ✅ Shows "pending" status for unsent
- ✅ Shows "sent" for delivered
- ✅ Timestamps are correct

---

### TEST 16: Broadcast SMS Alerts

**Objective:** Send bulk SMS to premium users (Optional)

**Prerequisites:**
- SMS provider configured
- Premium users exist
- SMS balance available

**Steps:**
```
1. Admin panel → "📢 Send Alerts" tab
2. Enter message: "Planned maintenance today 10-11 PM"
3. Click "Send SMS Alert"
4. Confirm dialog appears
5. Click "Confirm"
6. Wait for processing (2-5 seconds)
7. Verify: Success message shown
```

**Expected Results:**
- ✅ SMS sent to all premium users
- ✅ Success notification shown
- ✅ Confirmation SMS received
- ✅ Message appears in notifications queue

---

### TEST 17: Session Persistence

**Objective:** Verify user stays logged in across page refresh

**Steps:**
```
1. Login as demo@metromind.com
2. Click "📦 My Bookings"
3. Refresh page (F5 or Cmd+R)
4. Wait for page to reload
5. Verify: Still logged in
6. Click booking to view details
7. Refresh page again
8. Verify: Still logged in and details visible
```

**Expected Results:**
- ✅ User ID persists in localStorage
- ✅ No redirect to login after refresh
- ✅ Previous navigation state maintained
- ✅ Bookings data reloaded from API

---

### TEST 18: Error Handling

**Objective:** Verify proper error handling and messages

**Steps:**
```
1. Login attempt with wrong password
   - Email: demo@metromind.com
   - Password: wrongpassword
   - Verify: "Invalid credentials" message

2. Signup with existing email
   - Use: demo@metromind.com
   - Verify: "Email already exists" message

3. Admin access with wrong token
   - Token: wrong_token
   - Verify: "Invalid admin token" message

4. Book trip while offline
   - Open DevTools (F12)
   - Go to Network tab
   - Set to "Offline"
   - Try to book
   - Verify: Connection error message
   - Go back online
```

**Expected Results:**
- ✅ All error messages are clear and helpful
- ✅ No console errors or crashes
- ✅ User can retry after error
- ✅ App remains responsive

---

### TEST 19: Responsive Design

**Objective:** Verify UI works on different screen sizes

**Steps:**
```
1. Open browser DevTools (F12)
2. Click device toolbar icon
3. Test different sizes:
   - Mobile (375px) - iPhone
   - Tablet (768px) - iPad
   - Desktop (1920px)
   - Verify on each:
     - Header navigation visible/accessible
     - Search bar functional
     - Results display properly
     - Buttons are clickable
     - Modals fit screen
     - No horizontal scrolling needed
```

**Expected Results:**
- ✅ Mobile: Stack layout, touch-friendly buttons
- ✅ Tablet: 2-column layout works
- ✅ Desktop: Full layout with sidebars
- ✅ All text readable
- ✅ No layout breaking

---

### TEST 20: Performance Check

**Objective:** Verify reasonable performance metrics

**Steps:**
```
1. Open browser DevTools
2. Go to Network tab
3. Reload page (Cmd+Shift+R to clear cache)
4. Observe metrics:
   - Page load time: < 3 seconds
   - Requests count: < 50
   - Total size: < 5 MB
   - API response time: < 1 second

5. Go to Performance tab
6. Record for 10 seconds while using app
7. Stop recording
8. Check for janky animations (yellow/red)
```

**Expected Results:**
- ✅ Page loads in < 3 seconds
- ✅ API calls respond < 1 second
- ✅ Smooth scrolling (60 FPS)
- ✅ No memory leaks
- ✅ No console errors

---

## 🎯 Quick Test Checklist

Complete this checklist for quick validation:

```
CORE FEATURES:
☐ App starts without errors
☐ Can signup new user
☐ Can login with credentials  
☐ Can search trips
☐ Can book a trip
☐ Order appears in "My Bookings"
☐ Can cancel order
☐ Can rate completed trip

ADMIN:
☐ Admin panel opens
☐ Can view statistics
☐ Can update order status
☐ Can see all users
☐ Can view notifications

EMAIL (if configured):
☐ Booking confirmation email received
☐ Cancellation email received
☐ Status update email received

SMS (if configured):
☐ Confirmation SMS received
☐ Status SMS received

TECHNICAL:
☐ No console errors
☐ No network errors
☐ Database saves correctly
☐ Stays logged in after refresh
```

---

## 📊 Test Results Template

Use this template to document test run:

```markdown
## Test Run - [Date]

**Environment:**
- Python Version: 
- Node Version:
- Database: SQLite

**Configuration:**
- Email: [Configured / Not configured]
- SMS: [Configured / Not configured]
- Admin Token: admin_secret

**Test Results:**
- ☐ TEST 1: Application Startup - ✅/❌
- ☐ TEST 2: User Signup - ✅/❌
- ☐ TEST 3: User Login - ✅/❌
- ☐ TEST 4: Trip Search - ✅/❌
- ☐ TEST 5: Trip Booking - ✅/❌
- [... etc ...]

**Issues Found:**
1. [Issue 1]
2. [Issue 2]

**Status:** ✅ Ready for Deployment / ❌ Issues Found

**Tester:** [Name]
**Date:** [Date]
```

---

## 🚨 Common Test Failures & Solutions

### "Cannot connect to API"
```
Problem: Frontend can't reach backend
Solution:
1. Ensure backend is running: python main.py
2. Check port 5000: http://localhost:5000/
3. Check .env.local has: REACT_APP_API_URL=http://localhost:5000
4. If on Windows with WSL, use 127.0.0.1 instead of localhost
```

### "No results when searching trips"
```
Problem: Trip search returns empty
Solution:
1. Ensure source/destination are valid codes
2. Check transit_data.py has station data
3. Verify graph_engine.py initializes correctly
4. Check backend logs for errors
```

### "Email not sending"
```
Problem: No confirmation email received
Solution:
1. Verify Gmail 2FA is enabled
2. Verify app password copied correctly (no spaces)
3. Check .env GMAIL_ADDRESS matches password
4. Check spam/promotions folder
5. Look in backend logs for email errors
```

### "SMS not sending"
```
Problem: Premium users don't get SMS
Solution:
1. Verify user is_premium = 1 in database
2. Verify phone number is saved
3. Verify API key is in .env
4. Verify SMS account has balance
5. Check backend logs for Twilio/Africa's Talking errors
```

### "Database locked"
```
Problem: Database file is locked
Solution:
1. Close all backend instances
2. Delete backend/metromind.db
3. Restart backend (rebuilds database)
4. Ensure only one main.py instance running
```

---

## ✅ Test Completion

After completing all tests:

1. ✅ Verify all 20 tests pass (or document failures)
2. ✅ Check error handling works
3. ✅ Confirm email/SMS sending (if configured)
4. ✅ Test on mobile/tablet sizes
5. ✅ Review performance metrics
6. ✅ Document any issues found

**You're ready to deploy!** 🚀

---

For questions or issues, check:
- [GETTING_STARTED.md](GETTING_STARTED.md) - Setup guide
- [FEATURES_IMPLEMENTATION.md](FEATURES_IMPLEMENTATION.md) - Feature docs
- Backend logs: Terminal running `python main.py`
- Frontend logs: Browser DevTools (F12)

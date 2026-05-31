# 🚀 MetroMind AI - Complete Setup Guide

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [Running the Application](#running-the-application)
4. [Testing the API](#testing-the-api)
5. [Troubleshooting](#troubleshooting)
6. [Demo Walkthrough](#demo-walkthrough)

---

## System Requirements

### Minimum Requirements
- **Python:** 3.9 or higher
- **Node.js:** 16.0.0 or higher
- **npm:** 8.0.0 or higher
- **RAM:** 2GB minimum
- **Storage:** 500MB free space

### Recommended Setup
- **OS:** Windows 10/11, macOS 10.15+, Ubuntu 20.04+
- **Editor:** VS Code with Python & JavaScript extensions
- **Terminal:** PowerShell (Windows), zsh/bash (macOS/Linux)

---

## Installation Steps

### Step 1: Clone or Extract the Project

```bash
# Navigate to the project directory
cd e:\D\ Drive\University\VS\ CODE\WEB_ENG\Semester\ Project\metromind-ai
```

### Step 2: Automated Setup (Recommended)

#### On Windows:
```bash
setup.bat
```

#### On macOS/Linux:
```bash
chmod +x setup.sh
./setup.sh
```

### Step 3: Manual Setup (if automated fails)

#### Backend Setup:
```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Frontend Setup:
```bash
# Navigate to frontend
cd frontend

# Install npm dependencies
npm install
```

---

## Running the Application

### Method 1: Manual Start (Two Terminals Required)

#### Terminal 1 - Backend (FastAPI Server):
```bash
cd backend
venv\Scripts\activate        # Windows
# source venv/bin/activate  # macOS/Linux

uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

#### Terminal 2 - Frontend (React Development Server):
```bash
cd frontend
npm start
```

**Expected Output:**
```
webpack compiled with ... warning
Compiled successfully!
On Your Network: http://192.168.x.x:3000
Local: http://localhost:3000
```

### Method 2: Docker Compose (Single Command)

```bash
# Make sure Docker and Docker Compose are installed
docker-compose up --build

# Access frontend at http://localhost:3000
# Access backend at http://localhost:8000
```

### Access Points

After starting both servers:
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **Swagger API Docs:** http://localhost:8000/docs
- **ReDoc API Docs:** http://localhost:8000/redoc

---

## Testing the API

### Using Swagger UI (Recommended)

1. Navigate to: `http://localhost:8000/docs`
2. Click on any endpoint to expand it
3. Click "Try it out"
4. Enter parameters and click "Execute"

### Example Test Cases

#### Test 1: Get All Stations
```
GET /api/stations
```

Expected Response:
```json
{
  "stations": [
    {
      "code": "Red_Sector_G7",
      "name": "Red Sector G7",
      "line": "Red Line",
      "coordinates": {
        "lat": 33.7265,
        "lng": 73.1950
      }
    }
    ...
  ],
  "total": 18
}
```

#### Test 2: Calculate Route
```
POST /api/get-route

Request Body:
{
  "source": "Red_Sector_G7",
  "destination": "Blue_NUST",
  "optimization": "time"
}
```

Expected Response:
```json
{
  "status": "success",
  "primary_route": {
    "path": ["Red_Sector_G7", "Red_Adiala_Road", "Red_Faizabad", "Red_PIMS", "Blue_PIMS_Exchange", "Blue_NUST"],
    "estimated_time_minutes": 32,
    "transfers": [{"from_station": "Red_PIMS", "to_station": "Blue_PIMS_Exchange", ...}],
    "lines_used": ["Red Line", "Blue Line"],
    "product_id": "ROUTE_001"
  },
  "alternative_packages": [...]
}
```

#### Test 3: Book a Route
```
POST /api/book-route

Request Body:
{
  "route_id": "ROUTE_001",
  "num_passengers": 1,
  "user_id": "user_12345"
}
```

Expected Response:
```json
{
  "status": "success",
  "order_id": "ORD_20260524083045_7821",
  "route_id": "ROUTE_001",
  "passengers": 1,
  "booked_at": "2026-05-24T08:30:45.123456",
  "payment_status": "pending",
  "tracking_status": "Awaiting Transport"
}
```

#### Test 4: Get Admin Analytics
```
GET /api/admin/analytics
```

Expected Response:
```json
{
  "timestamp": "2026-05-24T08:30:45.123456",
  "total_active_users": 1247,
  "total_orders_today": 2458,
  "network_capacity_usage": {
    "Red_Line": "78%",
    "Green_Line": "65%",
    "Blue_Line": "82%"
  }
}
```

### Using cURL

```bash
# Get all stations
curl http://localhost:8000/api/stations

# Calculate route
curl -X POST http://localhost:8000/api/get-route \
  -H "Content-Type: application/json" \
  -d '{"source":"Red_Sector_G7","destination":"Blue_NUST","optimization":"time"}'

# Book a route
curl -X POST http://localhost:8000/api/book-route \
  -H "Content-Type: application/json" \
  -d '{"route_id":"ROUTE_001","num_passengers":1,"user_id":"user_12345"}'
```

---

## Frontend Testing

### 1. Home Page
- Load the app at http://localhost:3000
- Verify the header displays "🚇 MetroMind AI"
- Check that all tabs load without errors

### 2. Search Route
1. Select source: "Red Sector G7"
2. Select destination: "Blue NUST"
3. Click "Find Route"
4. Verify results appear with:
   - Recommended package
   - Alternative packages
   - Travel time
   - Transfer information
   - Map with route visualization

### 3. Book a Route
1. From search results
2. Click "Order Now" on any itinerary
3. Verify booking confirmation appears
4. Check order ID is generated
5. Verify order status tracking displays

### 4. Cancel Booking
1. From active order page
2. Click "Cancel Order"
3. Verify refund confirmation
4. Check inventory is updated

### 5. Rate Trip
1. After order completes
2. Submit rating (1-5 stars)
3. Add optional feedback
4. Verify confirmation message

---

## Troubleshooting

### Backend Issues

#### Error: "ModuleNotFoundError: No module named 'fastapi'"
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt
```

#### Error: "Port 8000 already in use"
```bash
# Solution 1: Kill process on port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :8000
kill -9 <PID>

# Solution 2: Use different port
uvicorn main:app --reload --port 8001
```

#### Error: "Connection refused" from frontend
```bash
# Solution: Check backend is running
# At http://localhost:8000
# If not, restart backend with correct host/port
```

### Frontend Issues

#### Error: "npm: command not found"
```bash
# Solution: Install Node.js from https://nodejs.org/
# Verify installation:
node --version
npm --version
```

#### Error: "React Router errors"
```bash
# Solution: Clear node_modules and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
npm start
```

#### Map not displaying
```bash
# Solution: Check Leaflet dependencies
npm install leaflet react-leaflet
```

### CORS Issues

If you see CORS errors in browser console:
```bash
# Backend CORS is already configured in main.py
# If issues persist, check:
# 1. Backend is running on http://localhost:8000
# 2. Frontend is running on http://localhost:3000
# 3. API endpoints have correct URLs
```

---

## Demo Walkthrough

### Complete User Journey (10 minutes)

#### Step 1: Start the Application
- Terminal 1: `cd backend && uvicorn main:app --reload`
- Terminal 2: `cd frontend && npm start`
- Open http://localhost:3000

#### Step 2: Explore Stations
- View "Find Route" tab
- Check available metro stations
- Notice line colors (Red, Green, Blue)

#### Step 3: Calculate a Route
- Source: "Red Sector G7"
- Destination: "Blue NUST"
- Click "Find Route"
- **Result:** 32 mins, 2 transfers

#### Step 4: View on Map
- See interactive Leaflet map
- Notice route polyline
- Check start/end markers
- View transfer points

#### Step 5: Compare Packages
- **Package 1:** Fastest Route via Blue Line (32 mins, ⭐ RECOMMENDED)
- **Package 2:** Budget Route via Feeder Buses (42 mins, cheaper)
- **Package 3:** Express Route Premium (27 mins, premium cost)

#### Step 6: Book a Route
- Click "Order Now" on Package 1
- Get Order ID: ORD_20260524083045_XXXX
- See live trip tracking

#### Step 7: Track Trip
- Status: "Awaiting Transport"
- Progress bar fills as trip progresses
- Shows next stop: "PIMS Medical Complex"
- Driver info displays

#### Step 8: Rate Experience
- After trip completes
- Rate 5 stars
- Add optional feedback
- Submit

#### Step 9: View Analytics
- Navigate to admin panel (http://localhost:8000/docs)
- Call `/api/admin/analytics`
- See system metrics, revenue, user count

---

## Performance Tips

1. **Backend Caching:**
   - Transit data is cached in memory
   - Timetables update every 5 minutes

2. **Frontend Optimization:**
   - React components are memoized
   - Map updates are debounced

3. **Network:**
   - API responses typically < 100ms
   - Map tiles cached by browser

---

## Next Steps

After setup is complete:
1. Review [PROJECT_DESCRIPTION.md](PROJECT_DESCRIPTION.md) for project overview
2. Check [README.md](README.md) for architecture details
3. Explore API at http://localhost:8000/docs
4. Deploy with Docker: `docker-compose up`

---

## Support

- **API Issues:** Check http://localhost:8000/docs
- **Frontend Issues:** Check browser DevTools (F12)
- **Database Issues:** Check SQLite file in `backend/`
- **General Help:** Review code comments in source files

Good luck! 🚀

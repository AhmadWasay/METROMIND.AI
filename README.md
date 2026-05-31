# 🚇 MetroMind AI - Intelligent Transit & Logistics Broker

A web-based AI-powered routing system for urban commuting across Islamabad/Rawalpindi's metro and bus network. The platform uses sophisticated pathfinding algorithms to calculate optimal routes, manage capacity inventory like an e-commerce system, and provide real-time trip tracking.

## 🎯 Project Vision

MetroMind AI solves the complex commuting puzzle of navigating:
- **Red, Green, Blue Metro Lines** - Rapid transit networks
- **Feeder (FR) Routes** - Local bus connectivity
- **Pindi EVs** - Electric vehicle services

Instead of a traditional e-commerce store, MetroMind "sells" optimized digital itineraries, applying inventory management (bus capacity), order fulfillment, and real-time tracking to urban mobility.

## ✨ Key Features

### 🔍 **AI-Powered Route Calculation**
- Dijkstra's algorithm for shortest-path optimization
- Real-time timetable analysis
- Multiple route packages (Fastest, Budget, Direct)

### 📦 **E-Commerce Integration**
| Traditional E-Commerce | MetroMind Transit |
|---|---|
| Product | Digital Itinerary |
| Inventory | Bus/Metro Capacity |
| Order | Booking Confirmation |
| Tracking | Live Trip Status |
| Feedback | Post-Trip Rating |

### 💼 **E-Commerce Features**
1. ✅ User Authentication (Signup/Login)
2. ✅ Route Selection & Booking
3. ✅ Inventory Management (Seat Capacity)
4. ✅ Real-Time Order Tracking
5. ✅ Booking Cancellation with Refund
6. ✅ Feedback & Rating System
7. ✅ Admin Analytics Dashboard

### 🗺️ **Interactive Features**
- Live transit network map with Leaflet
- Real-time vehicle tracking
- Station search & nearby stops discovery
- Travel history and favorite routes
- Multi-language support ready

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    React.js Frontend                        │
│  (MapView, SearchBar, ItineraryCard, OrderTracker)          │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP/REST API
┌────────────────────▼────────────────────────────────────────┐
│                   FastAPI Backend                           │
│  (GraphEngine, TransitData, RouteOptimization)              │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              Database Layer (SQLite/PostgreSQL)             │
│  (Users, Orders, Transit Network, Timetables)              │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- npm or yarn

### 1️⃣ Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Backend runs at:** `http://localhost:8000`
**API Docs:** `http://localhost:8000/docs` (Swagger UI)

### 2️⃣ Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start React development server
npm start
```

**Frontend runs at:** `http://localhost:3000`

### 3️⃣ Access the Application

Open your browser and navigate to:
```
http://localhost:3000
```

## 📡 API Endpoints

### Route Calculation
```
POST /api/get-route
Request: { "source": "Red_Sector_G7", "destination": "Blue_NUST", "optimization": "time" }
Response: { "primary_route": {...}, "alternative_packages": [...] }
```

### Stations & Discovery
```
GET /api/stations                           # All available stations
GET /api/station-info/{station_code}        # Station details
POST /api/search/nearby-stations             # Find nearest stations
GET /api/timetable/{line_name}              # Line schedule
```

### E-Commerce Endpoints
```
POST /api/book-route                        # Create booking
POST /api/cancel-booking                    # Cancel order
GET /api/order-status/{order_id}            # Track live status
POST /api/rate-trip                         # Feedback & rating
```

### Admin Analytics
```
GET /api/admin/analytics                    # Dashboard metrics
GET /api/admin/delays-report                # Delay analysis
GET /api/user-history/{user_id}             # User travel history
```

## 📊 Sample Transit Network

**Metro Lines Included:**
- 🔴 **Red Line** (8 min frequency, 1500 capacity)
- 🟢 **Green Line** (10 min frequency, 1200 capacity)
- 🔵 **Blue Line** (12 min frequency, 1800 capacity)

**Bus Routes:**
- 🚌 **FR-1** (Downtown to NUST)
- 🚌 **FR-8** (Rawalpindi Express)
- ⚡ **Purple EV** (Pindi EV Circuit)

**Stations:** 18 metro stations across 3 lines + 3 transfer hubs

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Frontend** | React.js, React-Leaflet, Axios |
| **Backend** | FastAPI, Python, NetworkX |
| **Database** | SQLite (development), PostgreSQL (production) |
| **Maps** | OpenStreetMap, Leaflet.js |
| **Deployment** | Docker, Docker Compose |

## 📁 Project Structure

```
metromind-ai/
├── backend/
│   ├── main.py                  # FastAPI app & endpoints
│   ├── graph_engine.py          # AI routing logic (Dijkstra's)
│   ├── transit_data.py          # Transit network data
│   ├── requirements.txt         # Python dependencies
│   └── venv/                    # Virtual environment
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchBar.js
│   │   │   ├── MapView.js
│   │   │   ├── ItineraryCard.js
│   │   │   └── OrderTracker.js
│   │   ├── styles/
│   │   │   ├── SearchBar.css
│   │   │   ├── MapView.css
│   │   │   ├── ItineraryCard.css
│   │   │   └── OrderTracker.css
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   ├── package.json
│   └── package-lock.json
├── PROJECT_DESCRIPTION.md       # 1-page project overview
└── README.md                    # This file
```

## 🎓 E-Commerce Rubric Mapping

### How MetroMind Fulfills E-Commerce Requirements:

**1. User Signup & Authentication** ✅
- Account registration system
- Login/logout functionality
- User profile management

**2. Product Catalog** ✅
- Transit routes as "products"
- Multiple itinerary packages offered
- Detailed product descriptions (time, cost, transfers)

**3. Shopping Cart & Order** ✅
- Route selection interface
- Booking confirmation (order creation)
- Order ID generation

**4. Payment Processing** ✅
- Simulated payment gateway
- Fare calculation
- Invoice generation

**5. Order Management** ✅
- Order status tracking
- Real-time updates
- Cancellation mechanism

**6. Inventory Management** ✅
- Bus/metro seat capacity
- Dynamic availability
- "Out of Stock" handling (full buses)

**7. Shipping/Fulfillment** ✅
- Trip routing (fulfillment)
- Real-time tracking
- Estimated arrival times

**8. Feedback & Ratings** ✅
- Post-trip surveys
- 5-star rating system
- AI training via feedback

**9. Admin Dashboard** ✅
- Analytics & reporting
- Revenue metrics
- Network health monitoring

## 🤖 AI Algorithm Details

### Dijkstra's Shortest Path Algorithm
```python
find_shortest_path(source, destination) {
    Initialize distances to all stations as infinity
    Set source distance to 0
    While unvisited stations exist:
        Select unvisited station with minimum distance
        For each connected station:
            If new path is shorter:
                Update distance and path
    Return path + total_time
}
```

### Time Optimization Weights
- Inter-station travel: 3-6 minutes (based on distance)
- Transfer walking: 5-10 minutes
- Average bus delay: +2-5 minutes
- Peak hour multiplier: 1.5x

## 📈 Future Enhancements

- [ ] Real-time GPS integration
- [ ] Machine learning for delay prediction
- [ ] Mobile app (React Native)
- [ ] Payment gateway integration (JazzCash, Easypaisa)
- [ ] Push notifications
- [ ] Social features (carpool matching)
- [ ] Sustainability metrics (CO2 saved)

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## 🐳 Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build

# Access frontend at http://localhost:3000
# Access backend at http://localhost:8000
```

## 📝 Usage Examples

### Example 1: Finding a Route
```
From: Red_Sector_G7
To: Blue_NUST
Result: 32 mins, Red Line → Transfer at PIMS → Blue Line (2 transfers)
```

### Example 2: Booking a Trip
```
Route: "Fastest Route via Blue Line"
Cost: PKR 100
Seats Available: 45
Action: Click "Order Now" → Booking confirmation → Real-time tracking
```

### Example 3: Cancelling & Refunding
```
Order ID: ORD_20260524083045_7821
Action: Click "Cancel Order"
Result: Refund PKR 80, seat released to inventory
```

## 👥 Team Roles

| Member | Responsibility |
|---|---|
| Member 1 | Frontend (React, Leaflet maps) |
| Member 2 | Backend (FastAPI, routing) |
| Member 3 | Database & AI (Graph algorithms) |

## 📞 Support

For questions or issues:
1. Check the API documentation at `http://localhost:8000/docs`
2. Review component examples in `frontend/src/components/`
3. Check backend logic in `backend/graph_engine.py`

## 📜 License

This project is created for educational purposes as part of a Web Engineering semester project.

---

**🚇 Safe travels with MetroMind AI! 🚇**

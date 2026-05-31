# MetroMind AI: Intelligent Transit & Logistics Broker

## Project Overview

MetroMind AI is a web-based logistics platform designed to solve complex commuting challenges across the twin cities. The local transport network—comprising Pindi EVs, Feeder (FR) buses, and the Red, Green, and Blue Metro lines—operates on staggered schedules that are difficult for daily commuters to track. MetroMind AI acts as a digital broker. Users input their source and destination, and the system's AI engine analyzes starting times, average arrival intervals, and transfer walking distances. Instead of a traditional store selling physical goods, MetroMind AI "sells" optimized, multi-stop digital itineraries, applying standard e-commerce mechanics to urban mobility.

## Group Members

| Student ID | Full Name | Role / Primary Responsibility |
|---|---|---|
| STU-1001 | [Member 1 Name] | Front-End UI/UX & Map Integration |
| STU-1002 | [Member 2 Name] | Back-End Development & Database |
| STU-1003 | [Member 3 Name] | AI Routing Logic & Transit Timetable Data |

## Key e-Commerce Features Mapped to Transit Logistics

### 1. User Signup and Authentication
Commuters register accounts to save their frequent locations (e.g., home, university campus) and view their past travel history. User credentials stored securely in PostgreSQL with password hashing.

### 2. Product Ordering Mechanism (Route Generation)
The "product" is the AI-generated journey. Users input their current location and destination. The AI crunches timetable data and offers 2-3 "Itinerary Packages" (e.g., *Fastest Route via Blue Line* vs. *Cheapest Route via FR Buses*). The user selects and "orders" their preferred digital transit pass.

### 3. Stock / Inventory Management (Network Capacity)
"Inventory" represents the physical capacity and active schedules of buses. The system limits digital passes issued for specific time slots (e.g., 8:15 AM Red Line bus) to prevent overcrowding. If a bus is delayed or at full capacity, that route leg is temporarily marked as "Out of Stock."

### 4. Order Status Management (Live Trip Tracking)
Once a digital itinerary is "ordered," the dashboard updates dynamically based on AI predictions. Status flow: *Awaiting Transport → Boarded First Bus → Transferring at Hub → Final Leg → Destination Reached*.

### 5. Order Cancellation Mechanism
If a user changes their mind, they can cancel their active itinerary before the first bus arrives. This instantly releases their allocated "seat" back into the system's inventory for other commuters.

### 6. Feedback and Rating Process
After the trip, the system prompts users to rate the AI's accuracy out of 5 stars (e.g., "Did the Green Line bus actually arrive within the predicted 5-minute window?"). This feedback loop continuously trains and improves AI time estimates.

### 7. Admin Analytics Dashboard
Reports generation for transit authorities: peak commuting hours, most heavily ordered route combinations, average delay times across specific Metro stations, and revenue metrics from "sold" itineraries.

## Technical Architecture

**Backend:** FastAPI (Python) with NetworkX for graph-based pathfinding using Dijkstra's algorithm, Pandas for timetable data parsing, and SQLAlchemy ORM for database management.

**Frontend:** React.js with React-Leaflet for interactive map visualization, Hooks for state management, and Axios for API communication.

**Database:** SQLite for MVP static data (stations, routes), PostgreSQL with PostGIS extension for production-level spatial queries and user data persistence.

**Deployment:** Both backend and frontend run on localhost during development; containerized with Docker for production deployment.

## Expected Deliverables

1. ✅ Working API with 5+ endpoints for route calculation, order management, and analytics
2. ✅ Interactive React frontend with Leaflet map showing real-time route visualization
3. ✅ Sample transit data for Red, Green, Blue Metro lines and FR bus routes
4. ✅ Database schema supporting user accounts, orders, and transit inventory
5. ✅ AI-powered pathfinding algorithm optimizing for time, cost, and transfers
6. ✅ Live order tracking with estimated arrival times
7. ✅ Admin analytics dashboard

---

**Result:** A fully functional proof-of-concept platform that demonstrates e-commerce principles applied to urban mobility logistics.

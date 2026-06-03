# Quick Start - Trip Planner Testing

## Fast Setup (5 minutes)

### Terminal 1 - Backend
```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Expected output:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

### Terminal 2 - Frontend
```powershell
cd frontend
npm install
npm start
```

App opens automatically at `http://localhost:3000`

---

## Testing Checklist

### ✓ Backend API Tests

**1. Check Health**
```
GET http://localhost:8000/api/health
Expected: {"status": "healthy", "service": "MetroMind Trip Planner"}
```

**2. Get All Locations**
```
GET http://localhost:8000/api/locations
Expected: 100+ locations with metro stations and bus stops
```

**3. Get Bus Routes**
```
GET http://localhost:8000/api/bus-routes
Expected: 4 routes (R-2, R-4, R-5, R-10)
```

**4. Plan a Trip**
```
POST http://localhost:8000/api/plan-trip
{
  "source": "Fawara_Chowk",
  "destination": "Saddar_Metro_Station"
}
Expected: Journey with segments showing walking distances
```

### ✓ Frontend UI Tests

**1. Load Home Page**
- Header shows "MetroMind - Trip Planner" ✓
- Tab navigation visible (Plan Trip, Results, Bookings) ✓
- Search form displayed ✓

**2. Search and Plan**
- Select "Fawara_Chowk" as source ✓
- Select "Saddar_Metro_Station" as destination ✓
- Click "Plan Trip" ✓
- Results appear with journey details ✓

**3. View Journey Details**
- Click "Show Details" on recommended route ✓
- See time breakdown (transit + walking) ✓
- See all journey segments ✓
- See walking distances in km ✓
- See lines/routes used ✓

**4. Test Other Routes**
- Try R-2 route (Fawara → Quaid-e-Quad)
- Try R-4 route (Saddar Metro → Munawwar Colony)
- Try R-5 route (Marrir Metro → Motorway Chowk)
- Try R-10 route (Saddar → Shatta Chowk)

---

## Expected Results

### Sample Journey: Fawara Chowk → Saddar Metro Station
```
Status: Success
Total Time: 25-35 minutes
Cost: PKR 20
Walking Distance: 0.5-1.2 km
Transfers: 0
Journey Segments:
  1. Bus: Fawara_Chowk → Saddar_Metro_Station
     Time: 20-25 mins | Distance: 1.2km | Walk: 3 mins
  2. Walk: Final approach
     Time: 2-5 mins | Distance: 0.2km
```

### Sample Journey: Multiple Routes
```
When combining different bus routes:
- Shows clear segment boundaries
- Walking time between transfers
- Total journey time includes all segments
- Each segment shows distance and walking time
```

---

## Key Features to Verify

✓ **Walking Distance Display**
- Shows in kilometers in info box
- Each segment shows walking time
- Haversine calculation accurate

✓ **Journey Segments**
- Clear bus/metro/walk labeling
- From/To stops clearly shown
- Timing accurate for each segment

✓ **Search Functionality**
- Can search by partial name
- Dropdown shows matching locations
- Both metro stations and bus stops appear

✓ **Responsive Design**
- Works on desktop (1920px+)
- Works on tablet (768px+)
- Works on mobile (375px+)

---

## Troubleshooting

### Backend Issues
- Check port 8000 is not in use: `netstat -ano | findstr :8000`
- Verify Python version: `python --version` (should be 3.9+)
- Check dependencies: `pip list | findstr fastapi`

### Frontend Issues
- Clear cache: `npm cache clean --force`
- Rebuild: `npm install && npm start`
- Check Node version: `node --version` (should be 16+)

### API Connection Issues
- Backend must be running first
- Frontend looks for backend at `http://localhost:8000`
- Check CORS is enabled (should be in main.py)

---

## Sample Test Locations

### Start Points
- `Fawara_Chowk` - Downtown hub
- `Saddar_Metro_Station` - Major station
- `Marrir_Metro_Station` - Metro connection
- `Liaqat_Bagh_Station` - Transport hub

### Destinations
- `Saddar_Stop` - Local stop
- `Quaid_e_Quad` - Educational area
- `Munawwar_Colony` - Residential area
- `Motorway_Chowk` - Highway access

---

## Performance Metrics

| Operation | Expected Time | Status |
|-----------|--------------|--------|
| Backend startup | <2 seconds | ✓ |
| Frontend load | <2 seconds | ✓ |
| Trip calculation | <100ms | ✓ |
| API response | <200ms | ✓ |
| UI render | <300ms | ✓ |

---

## Notes

- Default demo locations already selected (will show journey)
- All feeder route data is real (from Excel file)
- Coordinates are accurate for Islamabad-Rawalpindi
- Walking times based on standard 1.4 m/s speed
- Fares fixed at PKR 20 per route

**Ready to test? Start terminals and navigate to http://localhost:3000! 🚀**

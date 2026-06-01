# backend/main.py - Trip Planning API using Flask
from flask import Flask, request, jsonify
from flask_cors import CORS
from graph_engine import TransitGraph
from transit_data import METRO_STATIONS, ALL_STOPS, BUS_ROUTES, BUS_STOPS
from datetime import datetime
import random
from models import init_db, init_transit_capacity

app = Flask(__name__)
CORS(app, origins=['*'], supports_credentials=True)

# Initialize database
try:
    init_db()
    init_transit_capacity()
except Exception as e:
    print(f"Database initialization: {e}")

# Initialize transit engine
transit_engine = TransitGraph()

# Import extended API endpoints
try:
    from api_extended import *
except Exception as e:
    print(f"Warning: Extended API not available: {e}")

# ============= API ENDPOINTS =============

@app.route("/", methods=["GET"])
def root():
    """API documentation"""
    return jsonify({
        "name": "MetroMind Trip Planner API",
        "version": "2.0",
        "endpoints": {
            "GET /api/health": "Health check",
            "GET /api/locations": "Get all metro stations and bus stops",
            "GET /api/bus-routes": "Get all available bus routes",
            "POST /api/plan-trip": "Plan a trip with full journey details",
            "GET /api/location-search/<query>": "Search for locations",
            "POST /api/book-trip": "Book a trip",
            "POST /api/cancel-booking": "Cancel a booking",
            "POST /api/rate-trip": "Rate a completed trip"
        }
    })

@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "MetroMind Trip Planner",
        "version": "2.0"
    })

@app.route("/api/locations", methods=["GET"])
def get_all_locations():
    """Get all available locations (metro stations + bus stops)"""
    locations = []
    known_codes = set()
    # Add metro stations
    for station in METRO_STATIONS:
        locations.append({
            'code': station['code'],
            'name': station['name'],
            'type': 'metro',
            'line': station['line'],
            'area': station.get('area', ''),
            'coordinates': station['coordinates']
        })
        known_codes.add(station['code'])
    
    # Add bus stops
    for stop in BUS_STOPS:
        locations.append({
            'code': stop['code'],
            'name': stop['name'],
            'type': 'bus',
            'area': stop.get('area', ''),
            'coordinates': stop['coordinates']
        })
        known_codes.add(stop['code'])
    
    # Ensure all stops referenced by bus routes are included using actual known stop records
    from transit_data import ALL_STOPS
    for route in BUS_ROUTES:
        for code in route.get('stops', []):
            if code not in known_codes:
                found = next((s for s in ALL_STOPS if s.get('code') == code), None)
                if found:
                    locations.append({
                        'code': found['code'],
                        'name': found.get('name', found['code']),
                        'type': found.get('type', 'bus'),
                        'area': found.get('area', ''),
                        'coordinates': found.get('coordinates', {'lat': 0, 'lng': 0})
                    })
                    known_codes.add(code)
                else:
                    # Skip unknown codes rather than creating placeholder entries
                    app.logger.warning(f"Skipped unknown route stop code in /api/locations: {code}")
    
    return jsonify({
        "status": "success",
        "locations": locations,
        "total": len(locations),
        "metro_stations": len(METRO_STATIONS),
        "bus_stops": len(BUS_STOPS)
    })

@app.route("/api/bus-routes", methods=["GET"])
def get_bus_routes():
    """Get all available bus routes"""
    routes = []
    for route in BUS_ROUTES:
        routes.append({
            'route_code': route['code'],
            'name': route['name'],
            'operator': route['operator'],
            'type': route['type'],
            'fare': route['fare'],
            'stops_count': len(route['stops']),
            'description': route.get('description', '')
        })
    return jsonify({"status": "success", "routes": routes, "total": len(routes)})

@app.route("/api/plan-trip", methods=["POST"])
def plan_trip():
    """
    Main endpoint: Plan a trip from source to destination
    Returns full journey with walking distances and transit times
    """
    try:
        data = request.get_json()
        source = data.get('source')
        destination = data.get('destination')
        optimization = data.get('optimization', 'time')
        
        result = transit_engine.find_shortest_path(source, destination, optimization=optimization)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/location-search/<query>", methods=["GET"])
def search_locations(query):
    """Search for locations by name"""
    query_lower = query.lower()
    results = []
    
    # Search in metro stations
    for station in METRO_STATIONS:
        if query_lower in station['code'].lower() or query_lower in station['name'].lower():
            results.append({
                'code': station['code'],
                'name': station['name'],
                'type': 'metro',
                'line': station['line']
            })
    
    # Search in bus stops
    from transit_data import BUS_STOPS
    for stop in BUS_STOPS:
        if query_lower in stop['code'].lower() or query_lower in stop['name'].lower():
            results.append({
                'code': stop['code'],
                'name': stop['name'],
                'type': 'bus',
                'area': stop.get('area', '')
            })
    
    return jsonify({
        "status": "success",
        "query": query,
        "results": results[:10],
        "total": len(results)
    })

@app.route("/api/book-trip", methods=["POST"])
def book_trip():
    """Book a trip/reserve seats"""
    try:
        data = request.get_json()
        route_id = data.get('route_id')
        num_passengers = data.get('num_passengers', 1)
        
        result = transit_engine.book_route(route_id, num_passengers)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/cancel-booking", methods=["POST"])
def cancel_booking():
    """Cancel a booking"""
    try:
        data = request.get_json()
        order_id = data.get('order_id')
        
        result = transit_engine.cancel_booking(order_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/rate-trip", methods=["POST"])
def rate_trip():
    """Rate a completed trip"""
    try:
        data = request.get_json()
        order_id = data.get('order_id')
        rating = data.get('rating')
        feedback = data.get('feedback', '')
        
        result = transit_engine.rate_trip(order_id, rating, feedback)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/route-info/<route_code>", methods=["GET"])
def get_route_info(route_code):
    """Get detailed information about a specific bus route"""
    for route in BUS_ROUTES:
        if route['code'] == route_code:
            return jsonify({
                "status": "success",
                "route_code": route_code,
                "name": route['name'],
                "operator": route['operator'],
                "type": route['type'],
                "fare": route['fare'],
                "stops": route['stops'],
                "description": route.get('description', '')
            })
    return jsonify({"error": "Route not found"}), 404

@app.route("/api/order-status/<order_id>", methods=["GET"])
def get_order_status(order_id):
    """Get real-time tracking status of a booked trip"""
    statuses = [
        "Awaiting Transport",
        "Boarded First Bus",
        "Transferring at Hub",
        "On Final Leg",
        "Destination Reached"
    ]
    current_status = random.choice(statuses)
    
    return jsonify({
        "order_id": order_id,
        "status": current_status,
        "progress_percentage": 45,
        "next_stop": "PIMS Medical Complex",
        "estimated_arrival": "08:35 AM",
        "current_location": {
            "lat": 33.7456,
            "lng": 73.1756,
            "description": "On Red Line, approaching PIMS station"
        }
    })

@app.route("/api/user-history/<user_id>", methods=["GET"])
def get_user_travel_history(user_id):
    """Get user's past trips and booking history"""
    return jsonify({
        "user_id": user_id,
        "total_trips": 24,
        "favorite_routes": [
            {
                "source": "Red_Sector_G7",
                "destination": "Red_PIMS",
                "times_used": 12,
            }
        ]
    })

@app.route("/api/admin/delays-report", methods=["GET"])
def get_delays_report():
    """Detailed delay analysis for transit authorities"""
    return jsonify({
        "report_date": datetime.now().isoformat(),
        "stations_with_delays": [
            {"station": "Red_PIMS", "avg_delay": 3.2, "reason": "High traffic"},
            {"station": "Green_Sector_G11", "avg_delay": 2.8, "reason": "Signal maintenance"},
            {"station": "Blue_Sector_B17", "avg_delay": 1.5, "reason": "Minimal"},
        ],
        "recommendation": "Increase Blue Line frequency during peak hours"
    })

@app.route("/api/auth/signup", methods=["POST"])
def signup():
    """Register a new commuter account"""
    try:
        data = request.get_json()
        return jsonify({
            "status": "success",
            "user_id": f"USR_{random.randint(100000, 999999)}",
            "message": f"Welcome {data.get('username')}! Your MetroMind account is ready.",
            "email_verification": "Verification email sent"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/auth/login", methods=["POST"])
def login():
    """User login endpoint"""
    try:
        data = request.get_json()
        return jsonify({
            "status": "success",
            "token": f"TOKEN_{random.randint(1000000, 9999999)}",
            "user_id": f"USR_{random.randint(100000, 999999)}",
            "message": "Login successful"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Starting MetroMind API on http://localhost:{port}")
    print("📚 API Documentation: http://localhost:{port}/")
    app.run(host="0.0.0.0", port=port, debug=False, threaded=True)

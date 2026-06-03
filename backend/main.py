from flask import Flask, jsonify
from flask_cors import CORS

import models

# Based on the documentation, this is a Flask app.
# The port 5000 is mentioned for the backend in MARKING_CRITERIA_VERIFICATION.md.
app = Flask(__name__)

# The documentation mentions CORS is configured.
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Import the blueprint from api_extended and register it with the app.
# This is the standard Flask pattern for organizing routes.
from api_extended import api as api_blueprint
app.register_blueprint(api_blueprint)

# A health check endpoint is good practice.
@app.route("/api/health")
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "MetroMind Trip Planner", "version": "2.0"})

# This block allows running the server directly with `python main.py`
if __name__ == "__main__":
    # To ensure the database is always available when the app runs,
    # we initialize it here. The `CREATE TABLE IF NOT EXISTS` statements
    # make this operation safe to run every time.
    with app.app_context():
        print("INFO:     Checking and initializing database...")
        models.init_db()
        models.init_transit_capacity()
        print("INFO:     Database is ready.")

    # Port 5000 is the correct port for the Flask backend based on the docs.
    print("INFO:     Starting Flask development server at http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
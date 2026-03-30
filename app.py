from flask import Flask, request, jsonify  # Import Flask framework components for building API

# Import your existing pipeline functions
from core.correlator import analyze_logs  # Core engine that detects incidents from logs
from storage import save_incidents         # Function to persist incidents into the database

# Initialize the Flask application
app = Flask(__name__)


@app.route("/")
def home():
    """
    Root endpoint to verify that the API is running.
    """
    return "Incident Correlator API is running"


@app.route("/ingest", methods=["POST"])
def ingest_logs():
    """
    Endpoint to receive logs in real-time and process them.

    Workflow:
    1. Accept JSON payload
    2. Validate input
    3. Run correlation engine
    4. Save incidents to database
    5. Return structured response
    """

    # Step 1: Parse incoming JSON request body
    data = request.get_json()

    # Step 2: Validate that data exists
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Step 3: Extract logs from the request payload
    logs = data.get("logs")

    # Step 4: Validate that logs are present
    if not logs:
        return jsonify({"error": "Missing 'logs' field"}), 400

    # Step 5: Pass logs to correlation engine to generate incidents
    incidents = analyze_logs(logs)

    # Step 6: Persist the generated incidents into the database
    save_incidents(incidents)

    # Step 7: Return a structured JSON response to the client
    return jsonify({
        "message": "Logs processed successfully",
        "incidents": incidents
    }), 200


# Entry point of the application
if __name__ == "__main__":
    # Run Flask app in debug mode (auto-reloads on changes, useful for development)
    app.run(debug=True)
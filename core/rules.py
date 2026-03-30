# Import helper function for timestamp conversion
from utils import parse_timestamp

def detect_brute_force(logs, time_window=60):
    """
    Detect brute force attacks using time window correlation.

    Logic:
    - If 3+ failed login attempts from same IP within time window → alert
    """

    # Dictionary to store suspicious IPs and counts
    alerts = {}

    # Sort logs by timestamp for proper chronological analysis
    logs = sorted(logs, key=lambda x: x["timestamp"])

    # Loop through logs
    for i in range(len(logs)):
        current = logs[i]

        # Only consider failed login attempts
        if current["event"] != "failed_login":
            continue

        # Extract IP
        ip = current["ip"]

        # Convert timestamp to datetime
        current_time = parse_timestamp(current["timestamp"])

        # Counter for failed attempts
        count = 0

        # Compare with other logs
        for j in range(i, len(logs)):
            next_log = logs[j]

            # Only same IP
            if next_log["ip"] != ip:
                continue

            # Convert timestamp
            next_time = parse_timestamp(next_log["timestamp"])

            # Calculate time difference
            diff = (next_time - current_time).total_seconds()

            # Check if within time window and failed login
            if diff <= time_window and next_log["event"] == "failed_login":
                count += 1

        # If threshold exceeded, mark IP
        if count >= 3:
            alerts[ip] = count

    return alerts

#Rule 2: Login Pattern Anomaly

def detect_login_anomaly(logs):
    """
    Detect suspicious login behavior.

    Logic:
    - If an IP has both failed_login and success_login
      → possible brute force success
    """

    # Dictionary to group events by IP
    ip_events = {}

    # Group logs by IP
    for log in logs:
        ip = log["ip"]

        # Store all events for each IP
        ip_events.setdefault(ip, []).append(log["event"])

    # List to store suspicious IPs
    suspicious_ips = []

    # Analyze each IP
    for ip, events in ip_events.items():

        # If both failed and success login exist
        if "failed_login" in events and "success_login" in events:
            suspicious_ips.append(ip)

    # ✅ FIX: return the correct variable
    return suspicious_ips
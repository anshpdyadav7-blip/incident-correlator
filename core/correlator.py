# Import detection rules for identifying specific security patterns
from core.rules import detect_brute_force, detect_login_anomaly

# Import helper function to convert numeric risk score into severity level
from utils import calculate_severity

# Import function that calculates risk score based on alerts
from core.scoring import calculate_risk


def analyze_logs(logs):
    """
    Correlate alerts into incidents.

    Purpose:
    - Apply multiple detection rules
    - Combine results per IP (correlation)
    - Generate structured incidents with risk and severity
    """

    # Step 1: Initialize an empty list to store final incidents
    incidents = []

    # Step 2: Run brute force detection rule on logs
    # Returns a dictionary like: {ip: attempt_count}
    brute_force = detect_brute_force(logs)

    # Step 3: Run login anomaly detection rule
    # Returns a list of suspicious IPs
    anomaly_ips = detect_login_anomaly(logs)

    # Step 4: Combine all unique IPs from both detection sources
    # set() ensures no duplicate IPs are processed
    for ip in set(list(brute_force.keys()) + anomaly_ips):

        # Step 5: Initialize a list to store alerts related to this IP
        alerts = []

        # Step 6: Check if this IP was flagged for brute force activity
        if ip in brute_force:

            # Step 7: Add brute force alert with attempt count
            alerts.append({
                "type": "Brute Force Attack",
                "attempts": brute_force[ip]
            })

        # Step 8: Check if this IP was flagged for login anomaly
        if ip in anomaly_ips:

            # Step 9: Add suspicious login pattern alert
            alerts.append({
                "type": "Suspicious Login Pattern"
            })

        # Step 10: Calculate total risk score based on all alerts for this IP
        score = calculate_risk(alerts)

        # Step 11: Create a structured incident object
        incidents.append({
            "ip": ip,  # IP address being analyzed
            "alerts": alerts,  # List of detected alerts for this IP
            "risk_score": score,  # Numeric risk score
            "severity": calculate_severity(score)  # Severity derived from score
        })

    # Step 12: Return the final list of correlated incidents
    return incidents
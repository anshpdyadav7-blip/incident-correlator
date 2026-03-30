def calculate_risk(alerts):
    """
    Assign a risk score based on alerts.

    Why?
    → Helps prioritize incidents like real SOC systems
    """

    # Step 1: Initialize total risk score to 0
    # This variable will accumulate risk points from all alerts
    score = 0

    # Step 2: Loop through each alert in the alerts list
    # Each alert is expected to be a dictionary with a "type" field
    for alert in alerts:

        # Step 3: Check if the alert type is "Brute Force Attack"
        # This type of attack is considered high risk, so we assign more points
        if alert["type"] == "Brute Force Attack":

            # Step 4: Increase score by 3 for brute force detection
            score += 3

        # Step 5: Check if the alert type is "Suspicious Login Pattern"
        # This indicates abnormal behavior, but slightly lower risk than brute force
        if alert["type"] == "Suspicious Login Pattern":

            # Step 6: Increase score by 2 for suspicious login activity
            score += 2

    # Step 7: Return the final computed risk score
    # This score will later be used to determine severity (LOW / MEDIUM / HIGH)
    return score
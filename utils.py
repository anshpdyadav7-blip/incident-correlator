# Import datetime module for time handling
from datetime import datetime

def parse_timestamp(ts):
    """
    Convert timestamp string to datetime object.

    Why?
    → Needed for comparing time differences between logs
    """

    # Convert ISO timestamp string into datetime object
    return datetime.fromisoformat(ts)


def calculate_severity(score):
    """
    Convert numeric score into severity label.

    Why?
    → Helps categorize alerts into LOW / MEDIUM / HIGH
    """

    # If risk score is high
    if score >= 5:
        return "HIGH"
    
    # Moderate risk
    elif score >= 3:
        return "MEDIUM"
    
    # Low risk
    else:
        return "LOW"
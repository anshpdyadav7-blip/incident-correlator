# Import JSON module to read structured log data from a file
import json

# Import database connection function from db.py
from db import get_connection


def load_logs(file_path):
    """
    Load logs from a JSON file and store them into the database.

    Purpose:
    - Read raw log data
    - Persist it into SQLite DB
    - Return logs for further processing
    """

    # Step 1: Open the JSON file in read mode
    # 'file_path' is the path provided when calling this function
    with open(file_path, "r") as file:

        # Step 2: Parse JSON content into Python list of dictionaries
        # Each dictionary represents one log entry
        logs = json.load(file)

    # Step 3: Establish a connection to the SQLite database
    conn = get_connection()

    # Step 4: Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Step 5: Iterate through each log entry
    for log in logs:

        # Step 6: Insert each log into the 'logs' table
        # Using parameterized query to prevent SQL injection and ensure safety
        cursor.execute("""
        INSERT INTO logs (timestamp, ip, event, user)
        VALUES (?, ?, ?, ?)
        """, (
            log["timestamp"],  # Extract timestamp from log
            log["ip"],         # Extract IP address
            log["event"],      # Extract event type (e.g., login, failure)
            log["user"]        # Extract username
        ))

    # Step 7: Commit the transaction to save all inserted records permanently
    conn.commit()

    # Step 8: Close the database connection to free resources
    conn.close()

    # Step 9: Return the parsed logs for further processing (correlation engine)
    return logs
# Import database initialization function
from db import init_db

# Import log loading function
from core.parser import load_logs

# Import correlation engine
from core.correlator import analyze_logs

# Import incident saving function from correct module
from storage import save_incidents


def main():
    """
    Full pipeline of the incident correlation system.

    Steps:
    1. Initialize database
    2. Load logs from file
    3. Run correlation engine
    4. Display incidents
    5. Save incidents to database
    """

    # Step 1: Initialize database (creates tables if not exist)
    init_db()

    # Step 2: Notify user that logs are being loaded
    print("[*] Loading logs...")

    # Step 3: Load logs from JSON file into Python objects
    logs = load_logs("data/sample_logs.json")

    # Step 4: Notify user that correlation is starting
    print("[*] Correlating incidents...")

    # Step 5: Run correlation engine to generate incidents
    incidents = analyze_logs(logs)

    # Step 6: Display generated incidents
    print("\n[+] Incidents:\n")
    for inc in incidents:
        print(inc)

    # Step 7: Notify user that incidents are being saved
    print("[*] Saving incidents to database...")

    # Step 8: Save correlated incidents into database
    save_incidents(incidents)

    # Step 9: Final completion message
    print("[+] Done.")


# Entry point
if __name__ == "__main__":
    main()
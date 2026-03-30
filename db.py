# Import sqlite3 for lightweight database
import sqlite3

# Database file name
DB_NAME = "incident.db"


def get_connection():
    """
    Create and return a database connection.
    """
    return sqlite3.connect(DB_NAME)


def init_db():
    """
    Initialize database tables.

    Why?
    → Ensures tables exist before inserting data
    """

    conn = get_connection()
    cursor = conn.cursor()

    # Table for logs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        ip TEXT,
        event TEXT,
        user TEXT
    )
    """)

    # Table for alerts
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        alert_type TEXT,
        severity TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()
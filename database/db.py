import sqlite3

def connect_to_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect("telemetry.db")
    return conn

def initialize_db():
    """Create the telemetry table if it doesn't exist."""
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS telemetry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        cpu_usage REAL NOT NULL,
        memory_usage REAL NOT NULL,
        response_time REAL NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Call the function to initialize the database
if __name__ == "__main__":
    initialize_db()

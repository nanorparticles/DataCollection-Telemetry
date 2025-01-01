import sqlite3
from datetime import datetime

def connect_to_db():
    """Connect to the SQLite database."""
    return sqlite3.connect("telemetry.db")

def insert_telemetry_data(cpu_usage, memory_usage, response_time):
    """Insert telemetry data into the SQLite table."""
    conn = connect_to_db()
    cursor = conn.cursor()

    # Insert data
    cursor.execute("""
    INSERT INTO telemetry (timestamp, cpu_usage, memory_usage, response_time)
    VALUES (?, ?, ?, ?)
    """, (datetime.now().isoformat(), cpu_usage, memory_usage, response_time))
    
    conn.commit()
    conn.close()

# Example: Simulate data insertion
if __name__ == "__main__":
    insert_telemetry_data(50.5, 30.2, 120.0)  # Example telemetry values

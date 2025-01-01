import sqlite3

# Path to the SQLite database file
db_path = r'C:/Users/alexn/DataCollection&Telemetry/database/telemetry.db'

try:
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check available tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in database:", tables)

    # View the data from the telemetry_data table
    table_name = 'telemetry_data'  # Change if the table name differs
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()

    if rows:
        # Print column names
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = [col[1] for col in cursor.fetchall()]
        print("Columns:", columns)

        # Print data
        print(f"Data from table '{table_name}':")
        for row in rows:
            print(row)
    else:
        print(f"No data found in table '{table_name}'.")

except sqlite3.Error as e:
    print(f"SQLite error: {e}")
finally:
    if conn:
        conn.close()

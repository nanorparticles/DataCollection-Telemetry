import sqlite3
import plotly.graph_objects as go

# Connect to the SQLite database
conn = sqlite3.connect('C:/Users/alexn/DataCollection&Telemetry/database/telemetry.db')
cursor = conn.cursor()

# Query the data (timestamp, cpu_usage, memory_usage) from the telemetry table
cursor.execute("SELECT timestamp, cpu_usage, memory_usage FROM telemetry_data")
data = cursor.fetchall()

# Close the database connection
conn.close()

# Separate the data into timestamps, cpu_usage, and memory_usage
timestamps = [row[0] for row in data]
cpu_usages = [row[1] for row in data]
memory_usages = [row[2] for row in data]

# Optional: Clean the data by ensuring there are no invalid or None values
cpu_usages = [float(value) if isinstance(value, (int, float)) else 0 for value in cpu_usages]
memory_usages = [float(value) if isinstance(value, (int, float)) else 0 for value in memory_usages]

# Create the Plotly figure
fig = go.Figure()

# Plot CPU Usage
fig.add_trace(go.Scatter(
    x=timestamps,
    y=cpu_usages,
    mode='lines+markers',
    name='CPU Usage',
))

# Plot Memory Usage
fig.add_trace(go.Scatter(
    x=timestamps,
    y=memory_usages,
    mode='lines+markers',
    name='Memory Usage',
))

# Customize the layout
fig.update_layout(
    title="Telemetry Data: CPU Usage vs Memory Usage",
    xaxis_title="Timestamp",
    yaxis_title="Usage (%)",
    xaxis=dict(tickangle=-45),  # Rotate x-axis labels for better visibility
)

# Show the plot
fig.show()

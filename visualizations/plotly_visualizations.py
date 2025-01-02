import sqlite3
import plotly.graph_objects as go
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('C:/Users/alexn/DataCollection&Telemetry/database/telemetry.db')
cursor = conn.cursor()


# Query data from the database
query = """
SELECT timestamp, cpu_usage, memory_usage, error_rate 
FROM telemetry_data 
ORDER BY timestamp ASC
"""
cursor.execute(query)
rows = cursor.fetchall()
conn.close()

# Check if data is available
if not rows:
    print("No data found in the database.")
    exit()

# Extract columns from the rows
timestamps = []
cpu_usage = []
memory_usage = []
error_rate = []

for row in rows:
    timestamps.append(datetime.fromisoformat(row[0]))  # Convert timestamp string to datetime object
    cpu_usage.append(row[1])
    memory_usage.append(row[2])
    error_rate.append(row[3])

# Create the line charts
fig = go.Figure()

# Add CPU usage trace
fig.add_trace(go.Scatter(
    x=timestamps,
    y=cpu_usage,
    mode='lines+markers',
    name='CPU Usage (%)',
    line=dict(color='blue'),
    marker=dict(size=6)
))

# Add Memory usage trace
fig.add_trace(go.Scatter(
    x=timestamps,
    y=memory_usage,
    mode='lines+markers',
    name='Memory Usage (%)',
    line=dict(color='green'),
    marker=dict(size=6)
))

# Add Error Rate trace
fig.add_trace(go.Scatter(
    x=timestamps,
    y=error_rate,
    mode='lines+markers',
    name='Error Rate (%)',
    line=dict(color='red'),
    marker=dict(size=6)
))

# Update layout for better visualization
fig.update_layout(
    title='Telemetry Data Visualization',
    xaxis_title='Timestamp',
    yaxis_title='Usage/Error Rate (%)',
    legend=dict(x=0, y=1),
    template='plotly_dark',
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True),
    hovermode='x unified'
)

# Show the plot
fig.show()

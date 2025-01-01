# Data Collection & Telemetry System

This project implements a telemetry data collection system that gathers system performance metrics (CPU usage, memory usage, error rates) and stores them in a SQLite database. The system allows you to visualize the collected data using Plotly for insights into system performance over time.

# Features

* Data Collection: Collect telemetry data such as CPU usage, memory usage, and error rates via HTTP requests.
* SQLite Database: Store telemetry data in an SQLite database for easy management and retrieval.
* Data Visualization: Visualize telemetry data using Plotly for better insights into system behavior.
* Flask Backend: A Flask web application that handles incoming telemetry data and stores it in the database.
  
# Technologies Used
* Flask: Lightweight Python web framework for handling HTTP requests.
* SQLite: Relational database used to store telemetry data.
* Plotly: Data visualization library to plot the telemetry data.
* SQLAlchemy: ORM to interact with the SQLite database seamlessly.
* Python: Programming language for the backend logic and data manipulation

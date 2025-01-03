from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/alexn/DataCollection&Telemetry/database/telemetry.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TelemetryData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    cpu_usage = db.Column(db.Float, nullable=False)
    memory_usage = db.Column(db.Float, nullable=False)
    error_rate = db.Column(db.Float, nullable=False)

@app.route('/telemetry', methods=['POST'])
def collect_telemetry():
    data = request.get_json()
    
    # Log received data
    print("Received telemetry data:", data)
    
    # Convert the timestamp to a datetime object
    try:
        timestamp = datetime.fromisoformat(data['timestamp'])
    except ValueError as e:
        print(f"Error in timestamp: {e}")
        return jsonify({"error": "Invalid timestamp format"}), 400

    telemetry_data = TelemetryData(
        timestamp=timestamp,
        cpu_usage=data['cpu_usage'],
        memory_usage=data['memory_usage'],
        error_rate=data['error_rate']
    )

    # Log data object before inserting
    print("Telemetry data object to be inserted:", telemetry_data)
    
    try:
        db.session.add(telemetry_data)
        db.session.commit()  # Commit the transaction
        print("Data committed to the database")
        return jsonify({"message": "Telemetry data collected"}), 201
    except Exception as e:
        db.session.rollback()  # Rollback if any error occurs
        print(f"Error committing data: {e}")  # Log the error
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)

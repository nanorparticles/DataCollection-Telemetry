import requests
import random
from datetime import datetime
import time

url = 'http://127.0.0.1:5000/telemetry'  # Replace with your Flask app URL

def generate_telemetry_data():
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'cpu_usage': random.uniform(0, 100),
        'memory_usage': random.uniform(1000, 8000),
        'error_rate': random.uniform(0, 1)
    }

while True:
    telemetry_data = generate_telemetry_data()
    response = requests.post(url, json=telemetry_data)

    print("Sending telemetry data:", telemetry_data)  # Log the data being sent
    print("Response status code:", response.status_code)  # Log the status code
    print("Response text:", response.text)  # Log the response

    time.sleep(5)  # Wait 5 seconds before sending next data point


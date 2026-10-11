import time
import random
import requests

API_URL = "http://127.0.0.1:8000/ingest"
devices = ["Vehicle-01", "Vehicle-02", "Vehicle-03"]

print("Starting data producer... Press Ctrl+C to stop.")

while True:
    payload = {
        "device_id": random.choice(devices),
        "speed": round(random.uniform(40.0, 120.0), 2),
        "temperature": round(random.uniform(70.0, 110.0), 2)
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        print(f"Sent: {payload} | Response: {response.status_code}")
    except Exception as e:
        print(f"Connection error: {e}. Is the backend running?")
        
    time.sleep(1)
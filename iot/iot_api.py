import requests
import random
import json

url = "https://httpbin.org/post"

sensor_data = {
    "device_id": "sensor_001",
    "temperature": round(random.uniform(20, 40), 2)
}

response = requests.post(
    url,
    json=sensor_data,
    timeout=10
)

if response.status_code == 200:
    print("Sensor data sent successfully")
    print(json.dumps(sensor_data, indent=4))
else:
    print("Failed to send sensor data")
    print("Status:", response.status_code)
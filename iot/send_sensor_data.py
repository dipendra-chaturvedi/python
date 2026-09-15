import requests
import random

url = "https://httpbin.org/post"

temperature = round(random.uniform(20, 40), 2)

data = {
    "device_id": "sensor_001",
    "temperature": temperature
}

response = requests.post(
    url,
    json=data,
    timeout=10
)

print("Status:", response.status_code)
print("Sent data:", data)
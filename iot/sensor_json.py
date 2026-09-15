import json
import random
from datetime import datetime

temperature = round(random.uniform(20, 40), 2)

sensor_data = {
    "device_id": "sensor_001",
    "temperature": temperature,
    "unit": "C",
    "timestamp": datetime.now().isoformat()
}

json_data = json.dumps(sensor_data, indent=4)

print(json_data)
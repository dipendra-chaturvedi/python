import sqlite3
import random
from datetime import datetime

connection = sqlite3.connect(
    r"C:\Development\python\iot\sensor.db"
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT,
    temperature REAL,
    recorded_at TEXT
)
""")

temperature = round(random.uniform(20, 40), 2)

cursor.execute("""
INSERT INTO sensor_data (device_id, temperature, recorded_at)
VALUES (?, ?, ?)
""", (
    "sensor_001",
    temperature,
    datetime.now().isoformat()
))

connection.commit()

print("Sensor data stored:", temperature, "°C")

connection.close()
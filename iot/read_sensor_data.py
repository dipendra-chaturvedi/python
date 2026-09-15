import sqlite3

connection = sqlite3.connect(
    r"C:\Development\python\iot\sensor.db"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM sensor_data")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
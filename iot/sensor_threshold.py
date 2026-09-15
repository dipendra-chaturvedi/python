import random

temperature = random.uniform(20, 40)

print("Temperature:", round(temperature, 2), "°C")

if temperature > 35:
    print("ALERT: High temperature")
else:
    print("Temperature is normal")
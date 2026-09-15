import random
import time

for _ in range(10):

    temperature = round(random.uniform(20, 40), 2)

    print("Temperature:", temperature, "°C")

    if temperature > 35:
        print("ALERT: High temperature!")

    time.sleep(2)
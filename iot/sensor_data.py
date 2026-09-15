import random
import time

for _ in range(5):

    temperature = random.uniform(20, 35)

    print("Temperature:", round(temperature, 2), "°C")

    time.sleep(2)
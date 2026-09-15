import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
port = 1883
topic = "python/iot/sensor"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# client.connect(broker, port, 60)
client.connect("test.mosquitto.org", 1883, 60)

client.publish(
    topic,
    "Temperature: 32°C"
)

print("Sensor data published")

client.disconnect()
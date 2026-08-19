import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello UDP Server"

client.sendto(
    message.encode(),
    ("127.0.0.1", 5001)
)

print("Message sent")

client.close()
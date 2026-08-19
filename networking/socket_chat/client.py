import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

print("Connected to server")

client.send("Hello Server".encode())

response = client.recv(1024)

print("Message from server:", response.decode())

client.close()
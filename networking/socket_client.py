import socket

host = "example.com"
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

print("Connected successfully")

client.close()
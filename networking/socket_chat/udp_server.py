import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("127.0.0.1", 5001))

print("UDP server is waiting for message...")

data, client_address = server.recvfrom(1024)

print("Message from client:", data.decode())
print("Client address:", client_address)

server.close()
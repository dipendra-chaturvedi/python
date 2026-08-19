import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))

server.listen()

print("Server is waiting for connection...")

client_socket, client_address = server.accept()

print("Client connected:", client_address)

message = client_socket.recv(1024)

print("Message from client:", message.decode())

client_socket.send("Hello Client".encode())

client_socket.close()
server.close()
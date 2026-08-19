# Connection with google
# import socket
# import ssl

# host = "www.google.com"
# port = 443

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# secure_client = ssl.create_default_context().wrap_socket(
#     client,
#     server_hostname=host
# )

# secure_client.connect((host, port))

# print("Connected successfully to Google")

# secure_client.close()

# Recieved data from google
import socket
import ssl

host = "www.google.com"
port = 443

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

secure_client = ssl.create_default_context().wrap_socket(
    client,
    server_hostname=host
)

secure_client.connect((host, port))

request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

secure_client.send(request.encode())

data = secure_client.recv(500)

print(data.decode(errors="ignore"))

secure_client.close()
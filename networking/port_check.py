import socket

host = "google.com"
port = 443

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = sock.connect_ex((host, port))

if result == 0:
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED")

sock.close()
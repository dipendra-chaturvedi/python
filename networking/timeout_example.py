import socket

host = "google.in"
port = 81

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.settimeout(10)

try:
    sock.connect((host, port))
    print("Connected successfully")

except socket.timeout:
    print("Connection timed out")

except socket.error as error:
    print("Connection failed:", error)

finally:
    sock.close()
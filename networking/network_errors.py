import socket

host = "wrong-domain-example.invalid"
port = 443

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

try:
    sock.connect((host, port))
    print("Connected successfully")

except socket.gaierror:
    print("DNS error: hostname could not be resolved")

except socket.timeout:
    print("Connection timed out")

except ConnectionRefusedError:
    print("Connection refused")

except socket.error as error:
    print("Network error:", error)

finally:
    sock.close()
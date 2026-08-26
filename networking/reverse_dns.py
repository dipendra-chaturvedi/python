import socket

ip_address = "88.222.243.199"

try:
    hostname = socket.gethostbyaddr(ip_address)

    print("Reverse DNS result:")
    print(hostname)

except socket.herror:
    print("No reverse DNS record found")
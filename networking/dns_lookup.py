import socket

domain = "google.com"

ip_address = socket.gethostbyname(domain)

print("Domain:", domain)
print("IP Address:", ip_address)
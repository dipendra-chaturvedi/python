import socket

# domain = "google.com"
domain = "nodbot.org"
port = 443

info = socket.getaddrinfo(domain, port)

for item in info:
    print(item)
import socket

domain1 = "google.com"

ip_address1 = socket.gethostbyname(domain1)
print("Domain:", domain1)
print("IP Address 1:", ip_address1)
print(socket.gethostbyname(domain1))

domain2 = "nodbot.in"
ip_address2 = socket.gethostbyname(domain2)
host_info = socket.gethostbyname(domain2)


print("Domain:", domain2)
print("IP Address 2:", ip_address2)
print("Host Info:", host_info)

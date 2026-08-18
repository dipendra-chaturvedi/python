# import requests

# url = "https://example.com"

# response = requests.get(url)

# print("Status Code:", response.status_code)
# print("HTTPS used:", response.url.startswith("https://"))


import requests

url = "https://www.facebook.com"

response = requests.get(url, timeout=10)

print("Status Code:", response.status_code)
print("Final URL:", response.url)
print("HTTPS used:", response.url.startswith("https://"))
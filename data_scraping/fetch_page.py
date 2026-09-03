import requests

url = "https://www.google.com"

response = requests.get(url, timeout=10)

print("Status:", response.status_code)
print(response.text[:500])
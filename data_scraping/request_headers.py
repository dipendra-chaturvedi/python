import requests

url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers,
    timeout=10
)

print("Status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Server:", response.headers.get("Server"))
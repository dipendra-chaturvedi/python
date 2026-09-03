import requests
from bs4 import BeautifulSoup

url = "https://nodbot.org"

response = requests.get(url, timeout=10)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

for link in links:
    text = link.get_text(strip=True)
    url = link.get("href")

    print("Text:", text)
    print("URL:", url)
    print("-" * 40)
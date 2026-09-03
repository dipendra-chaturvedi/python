import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/"

response = requests.get(base_url, timeout=10)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

for link in links:
    href = link.get("href")

    if href:
        absolute_url = urljoin(base_url, href)
        print(absolute_url)
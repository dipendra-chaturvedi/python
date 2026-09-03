import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url, timeout=10)

soup = BeautifulSoup(response.text, "html.parser")

images = soup.find_all("img")

for image in images:
    print("Image:", image.get("src"))
    print("Alt:", image.get("alt"))
    print("-" * 40)
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://books.toscrape.com/"

response = requests.get(base_url, timeout=10)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")[:5]

for book in books:
    relative_url = book.find("h3").find("a").get("href")
    book_url = urljoin(base_url, relative_url)

    book_response = requests.get(book_url, timeout=10, verify=False)

    book_soup = BeautifulSoup(book_response.text, "html.parser")

    title = book_soup.find("h1").get_text(strip=True)

    print("Title:", title)
    print("URL:", book_url)
    print("-" * 60)
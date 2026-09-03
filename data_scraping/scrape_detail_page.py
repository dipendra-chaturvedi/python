import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/"

response = requests.get(base_url, timeout=10)

soup = BeautifulSoup(response.text, "html.parser")

book = soup.find("article", class_="product_pod")

relative_url = book.find("h3").find("a").get("href")

book_url = urljoin(base_url, relative_url)

print("Book URL:", book_url)

book_response = requests.get(book_url, timeout=10)

book_soup = BeautifulSoup(book_response.text, "html.parser")

title = book_soup.find("h1").get_text(strip=True)

print("Title:", title)
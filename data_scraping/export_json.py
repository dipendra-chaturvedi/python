import requests
from bs4 import BeautifulSoup
import json

url = "https://books.toscrape.com/"

response = requests.get(url, timeout=10)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

book_data = []

for book in books:
    title = book.find("h3").find("a").get("title")
    price = book.find("p", class_="price_color").get_text(strip=True)
    availability = book.find("p", class_="instock").get_text(strip=True)

    book_data.append({
        "title": title,
        "price": price,
        "availability": availability
    })

with open(
    r"C:\Development\python\data_scraping\books.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(book_data, file, indent=4, ensure_ascii=False)

print("Data exported successfully")
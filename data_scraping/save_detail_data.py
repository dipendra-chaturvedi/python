import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://books.toscrape.com/"

response = requests.get(
    base_url,
    timeout=10,
    verify=False
)

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article", class_="product_pod")[:5]

book_data = []

for book in books:

    relative_url = book.find("h3").find("a").get("href")
    book_url = urljoin(base_url, relative_url)

    book_response = requests.get(
        book_url,
        timeout=10,
        verify=False
    )

    book_soup = BeautifulSoup(
        book_response.content,
        "html.parser"
    )

    title = book_soup.find("h1").get_text(strip=True)

    price = book_soup.find(
        "p",
        class_="price_color"
    ).get_text(strip=True)

    availability = book_soup.find(
        "p",
        class_="instock availability"
    ).get_text(strip=True)

    upc = None

    for row in book_soup.find_all("tr"):
        cells = row.find_all(["th", "td"])

        if len(cells) >= 2 and cells[0].get_text(strip=True) == "UPC":
            upc = cells[1].get_text(strip=True)
            break

    book_data.append({
        "title": title,
        "price": price,
        "availability": availability,
        "upc": upc
    })

with open(
    r"C:\Development\python\data_scraping\book_details.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        book_data,
        file,
        indent=4,
        ensure_ascii=False
    )

print("Book details saved successfully")
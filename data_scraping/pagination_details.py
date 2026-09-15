import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

for page in range(1, 3):

    url = base_url.format(page)

    response = requests.get(
        url,
        timeout=10,
        verify=False
    )

    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all(
        "article",
        class_="product_pod"
    )[:5]

    print(f"\n===== PAGE {page} =====")

    for book in books:

        relative_url = book.find("h3").find("a").get("href")
        book_url = urljoin(
            "https://books.toscrape.com/catalogue/",
            relative_url
        )

        detail_response = requests.get(
            book_url,
            timeout=10,
            verify=False
        )

        detail_soup = BeautifulSoup(
            detail_response.content,
            "html.parser"
        )

        title = detail_soup.find("h1").get_text(strip=True)

        price = detail_soup.find(
            "p",
            class_="price_color"
        ).get_text(strip=True)

        availability = detail_soup.find(
            "p",
            class_="instock availability"
        ).get_text(strip=True)

        print("Title:", title)
        print("Price:", price)
        print("Availability:", availability)
        print("-" * 40)
import requests
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

for page in range(1, 4):

    url = base_url.format(page)

    response = requests.get(url, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print(f"\n--- Page {page} ---")

    for book in books:
        title = book.find("h3").find("a").get("title")
        price = book.find("p", class_="price_color").get_text(strip=True)

        print(title, "-", price)
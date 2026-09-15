import requests

session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0"
})

urls = [
    "https://books.toscrape.com/",
    "https://books.toscrape.com/catalogue/page-2.html"
]

for url in urls:

    response = session.get(
        url,
        timeout=10,
        verify=False
    )

    print("URL:", url)
    print("Status:", response.status_code)
    print("-" * 40)
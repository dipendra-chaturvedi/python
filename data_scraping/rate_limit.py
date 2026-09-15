import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = [
    "https://books.toscrape.com/",
    "https://books.toscrape.com/catalogue/page-2.html",
    "https://books.toscrape.com/catalogue/page-3.html"
]

for url in urls:

    response = requests.get(
        url,
        timeout=10,
        verify=False
    )

    print("URL:", url)
    print("Status:", response.status_code)

    time.sleep(2)
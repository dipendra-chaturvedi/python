import requests

url = "https://books.toscrape.com/page-that-does-not-exist"

try:
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    print("Page fetched successfully")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)
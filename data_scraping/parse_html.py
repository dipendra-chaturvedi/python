import requests
from bs4 import BeautifulSoup

# url = "https://google.com"
url = "https://nodbot.org"

response = requests.get(url, timeout=10)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)
import requests
from bs4 import BeautifulSoup

url = "https://nodbot.org"

response = requests.get(url, timeout=10)

soup = BeautifulSoup(response.text, "html.parser")

headings = soup.find_all("h2")

for heading in headings:
    print(heading.get_text(strip=True))
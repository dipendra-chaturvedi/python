import requests
from bs4 import BeautifulSoup

html = """
<table>
    <tr>
        <th>Name</th>
        <th>Salary</th>
    </tr>
    <tr>
        <td>Rahul</td>
        <td>55000</td>
    </tr>
    <tr>
        <td>Amit</td>
        <td>60000</td>
    </tr>
</table>
"""

soup = BeautifulSoup(html, "html.parser")

table = soup.find("table")

rows = table.find_all("tr")

for row in rows:
    cells = row.find_all(["th", "td"])
    data = [cell.get_text(strip=True) for cell in cells]

    print(data)
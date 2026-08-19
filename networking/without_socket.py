# Simple google search using requests
# import requests

# response = requests.get("https://www.google.com")

# print(response.status_code)
# print(response.text[:200])

# Simple google search using requests with parameters
# import requests

# url = "https://www.google.com/search"
# params = {
#     "q": "python networking"
# }

# response = requests.get(url, params=params)

# print(response.status_code)
# # print(response.text[:500]) # for 500 characters of the response text
# print(response.text) # for the entire response text


import requests
import os

url = "https://www.google.com/search"

params = {
    "q": "python networking"
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)

file_path = os.path.join(
    os.path.dirname(__file__),
    "google_response.html"
)

with open(file_path, "w", encoding="utf-8") as file:
    file.write(response.text)

print("Response saved to:")
print(file_path)
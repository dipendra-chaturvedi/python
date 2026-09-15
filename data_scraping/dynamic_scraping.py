from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://books.toscrape.com/")

title = driver.find_element(
    By.CSS_SELECTOR,
    "h1"
)

print("Page title:", title.text)

# driver.quit()
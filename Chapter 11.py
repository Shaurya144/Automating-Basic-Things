# Chapter 11 — Web Scraping

import requests
from bs4 import BeautifulSoup
import time

# download page
response = requests.get("https://example.com")
response.raise_for_status()

# parse html
soup = BeautifulSoup(response.text, "html.parser")

# get title
print(soup.title.getText())

# get all links
links = soup.select("a")
for link in links:
    print(link.getText(), link.get("href"))

# get first paragraph
p = soup.select_one("p")
if p:
    print(p.getText())

# download an image
image_url = "https://example.com/image.png"
res = requests.get(image_url)
res.raise_for_status()

with open("image.png", "wb") as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)

# delay to avoid spamming
time.sleep(2)

# save links to file
with open("links.txt", "w") as f:
    for link in links:
        f.write(f"{link.getText()} -> {link.get('href')}\n")

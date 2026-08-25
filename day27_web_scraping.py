from bs4 import BeautifulSoup
import requests

# 1. lay HTML thô từ trang web
url = "https://quotes.toscrape.com"
response = requests.get(url)

# 2. phan tich cu phap HTML voi BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# 3. lay tieu de trang (the h1)
title = soup.find("h1").text.strip()
print(f"=== {title} ===\n")

# 4. tìm tất cả các thẻ <span class="text"> chứa câu trích dẫn
quotes = soup.find_all("span", class_="text")

# 5. duyệt qua từng câu và in ra Terminal
for idx, quote in enumerate(quotes, 1):
    print(f"{idx}. {quote.text}")


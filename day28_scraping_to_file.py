import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 1.tim toan bo cac khoi quote (nam trong div class="quote")
quote_blocks = soup.find_all("div", class_="quote")
data = []

# 2. Duyệt qua từng khối để lấy cả câu nói lẫn tác giả
for block in quote_blocks:
    text = block.find("span", class_="text").text
    author = block.find("small", class_="author").text
    
    # Gom vào dictionary
    data.append({
        "quote": text,
        "author": author
    })

# 3. Ghi dữ liệu ra file JSON
with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(" Khảo sát & cào thành công! Đã xuất dữ liệu ra file quotes.json")
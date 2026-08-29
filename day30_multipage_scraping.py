from bs4 import BeautifulSoup
import requests


all_quotes = []
for page in range(1, 6):  # Dùng vòng lặp for page in range(1, 6) để duyệt qua 5 trang.
    url = f"https://quotes.toscrape.com/page/{page}/"

#  Lấy HTML về và soi
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Tìm tất cả các thẻ <div> có class="quote" trên TRANG HIỆN TẠI
quotes_block = soup.find_all("div", class_="quote")


# Vòng lặp nhỏ: Lấy từng câu + tác giả trong trang đó
for block in quotes_block:
    text = block.find("span", class_="text").text
    author = block.find("small", class_="author").text
    #  Thêm vào danh sách tổng all_quotes
    all_quotes.append({
            "quote": text,
            "author": author
        })
print(f"Finished page {page}")


    

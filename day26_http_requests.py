import requests

# 1. Gửi yêu cầu GET tới đường dẫn API
url = "https://api.github.com/users/octocat"
response = requests.get(url)

# 2. Kiểm tra xem kết nối có thành công không (200 = Thành công)
if response.status_code == 200:
    # 3. Chuyển dữ liệu JSON nhận được thành Dictionary trong Python
    data = response.json()
    
    print(" Connection successful!")
    print(f"Name: {data.get('name')}")
    print(f"Public Repos: {data.get('public_repos')}")
else:
    print(f" Connection failed. Error code: {response.status_code}")
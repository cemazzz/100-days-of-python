import pandas as pd
import json

# 1. doc file du lieu cao dc tu Day 28
with open("quotes.json", "r", encoding="utf-8") as d:
    data = json.load(d)

# 2. bien du lieu thanh bang (DataFrame)
df = pd.DataFrame(data)

# 3. in thu bang ra ter xem dang bang
print(df)

# 4. Xuất thẳng ra file CSV cho khách (encoding utf-8-sig để Excel không lỗi tiếng Việt/ký tự đặc biệt)
df.to_csv("quotes.csv", index=False, encoding="utf-8-sig")

print("\n⚡ Đã xuất dữ liệu ra file quotes.csv thành công!")
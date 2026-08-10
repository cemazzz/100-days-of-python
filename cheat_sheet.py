# ==========================================
# 📘 CHEAT SHEET - SỔ TAY TỪ VỰNG PYTHON
# ==========================================

# 1. THẺ GHI CHÚ (#)
# Dùng để giải thích cho con người đọc, máy tính sẽ bỏ qua dòng này.

# 2. KHÁI NIỆM def (Define - Định nghĩa)
# Dùng để "chế tạo" một cỗ máy/hàm. Khi gọi tên thì nó mới chạy.
def ten_co_may(dau_vao):
    # Lấy đầu vào xử lý...
    ket_qua = dau_vao + 10
    return ket_qua  # 3. return: Đẩy sản phẩm ra ngoài cho người dùng

# 4. DANH SÁCH (List) - Chứa nhiều đồ ngăn nắp bằng dấu []
danh_sach = ["Tao", "Chuoi", "Cam"]

# 5. TỪ ĐIỂN (Dictionary) - Chứa thông tin cặp "Khóa: Giá trị" bằng dấu {}
thong_tin = {"name": "Duy", "job": "AI Engineer"}

# 6. VÒNG LẶP for - Duyệt từng phần tử trong danh sách
for mon in danh_sach:
    print(mon)  # Lần lượt in ra Tao, Chuoi, Cam

# 7. CÂU ĐIỀU KIỆN if / else - Kiểm tra đúng/sai
if thong_tin["job"] == "AI Engineer":
    print("Duy vip pro!")
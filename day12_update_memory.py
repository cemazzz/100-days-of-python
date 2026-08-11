# du lieu ban dau

memory = [
    {"task": "viet bai blog", "status": "dang lam ⌛"},
    {"task": "sua loi code", "status": "that bai ❌"},
    {"task": "hoc python", "status": "dang lam ⌛"}
]
print("Bo nho truoc khi cap nhat: ")
for item in memory:
    print(f"📌task: {item['task']} | Trang thai: {item['status']}")

# --- VIET HAM ---
def cap_nhat_task(ten_task, trang_thai_moi):
    for item in memory:                          # 1. dung vong lap for duyet tung item trong memory
        if item["task"] == ten_task:             # 2. neu task trung voi ten_task
            item["status"] = trang_thai_moi      #    cap nhat trang thai moi
            return f"Da cap nhat '{ten_task}' thanh '{trang_thai_moi}'!"    # tra ve thong bao thanh cong
    return f"Khong tim thay '{ten_task}' trong bo nho" # 3. het vong lap for ma k tim thay tra ve khong tim thay

# --- TEST HAM ---

#test 1: cap nhat task co that

ket_qua1 = cap_nhat_task("hoc python", "hoan thanh ✅")
print(ket_qua1)

#test 2: cap nhat task k ton tai

ket_qua2 = cap_nhat_task("di da bong", "hoan thanh ✅")
print(ket_qua2)

# in lai memory xem task "hoc python" da doi trang thai chua
print("\nBo nho sau khi cap nhat: ")
for item in memory:
    print(f"📌task: {item['task']} | Trang thai: {item['status']}")

            
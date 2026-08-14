# tao du lieu
memory = [
    {"task": "viet bai blog", "status": "Dang lam ⌛"},
    {"task": "sua loi code", "status": "that bai ❌"},
    {"task": "hoc python", "status": "hoan thanh ✅"},
    {"task": "don phong tro", "status": "hoan thanh ✅"},
    {"task": "lau nha", "status": "Dang lam ⌛"}
]
print("📋 Bo nho truoc khi them")
for item in memory:
    print(f"- {item['task']} | Trang thai: {item['status']}")

# VIET HAM
def them_task(ten_task_moi, trang_thai="dang lam ⌛"):
    for item in memory:                         # duyet tung item trong memory
        if item["task"] == ten_task_moi:        # neu task trung voi ten_task_moi
            return f"⚠️ Task '{ten_task_moi}' da ton tai !"
    task_moi = {"task": ten_task_moi, "status": trang_thai}
    memory.append(task_moi)
    return f"✅ Da them task '{ten_task_moi}' vao bo nho !"

# --- TEST HAM ---
print("-" * 30)
print(them_task("quay video tiktok")) # them task chua co

print(them_task("hoc python"))  # them task da co
print("-" * 30)
 # in lai memory xem da them task moi chua

print("\n📋 Bo nho sau khi them")
for item in memory:
    print(f"- {item['task']} | Trang thai: {item['status']}")


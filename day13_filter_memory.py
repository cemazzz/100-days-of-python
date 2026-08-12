# tao du lieu
memory = [
    {"task": "viet bai blog", "status": "Dang lam ⌛"},
    {"task": "sua loi code", "status": "that bai ❌"},
    {"task": "hoc python", "status": "hoan thanh ✅"},
    {"task": "don phong tro", "status": "hoan thanh ✅"},
    {"task": "lau nha", "status": "Dang lam ⌛"}
]

#  VIET HAM
def lay_danh_sach_task(status_can_tim): 
    ket_qua =[]             # tao danh sach rong
    for item in memory:     # duyet tung item trong memory
      if item["status"] == status_can_tim:      # dung if kiem tra status neu dung
        ket_qua.append(item["task"])                                            # thi ket_qua.append(..)
    return ket_qua             # ra ngoai for va tra ve ket qua

# --- TEST HAM ---

# lay danh sach cac task hoan thanh ✅

completed_tasks = lay_danh_sach_task("hoan thanh ✅")
print("🎉 Cac cong viec da hoan thanh:")
for task in completed_tasks:
    print(f"- {task}")
    print("-" * 30)

# that bai
    
completed_tasks = lay_danh_sach_task("that bai ❌")
print("❌ Cac cong viec that bai:")
for task in completed_tasks:
    print(f"- {task}")
print("-" * 30)

# dang lam

completed_tasks = lay_danh_sach_task("Dang lam ⌛")
print("⌛ Cac cong viec dang lam:")
for task in completed_tasks:
    print(f"- {task}")

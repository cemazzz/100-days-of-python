# tao du lieu task
memory = [
    {"task": "viet bai blog", "status": "hoan thanh✅"},
    {"task": "sua loi code", "status": "that bai❌"},
    {"task": "lam bai tap", "status": "hoan thanh✅"},
    {"task": "phan tich du lieu", "status": "dang lam🛠️"},
    {"task": "hoc tieng anh", "status": "hoan thanh✅"},
    {"task": "hoc python", "status": "dang lam🛠️"},
]
# ham tim kiem va dem so luong
def tim_kiem_task(status_can_tim):
    count = 0 # b1: tao bien dem
    for item in memory: # b2: duyet tung phan tu trong memory
        if item["status"] == status_can_tim: # b3: so sanh dieu kien 
            count += 1 # b4: tang bien neu dung
    return count # b5: tra ve ket qua dem
# --- chay thu ham ---
completed = tim_kiem_task("hoan thanh✅")
failed = tim_kiem_task("that bai❌")
in_progress = tim_kiem_task("dang lam🛠️")

print(f" so task hoan thanh: {completed}")
print(f" so task that bai: {failed}")
print(f" so task dang lam: {in_progress}")

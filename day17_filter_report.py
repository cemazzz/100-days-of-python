# tao bo nho
memory = [
    {"task": "viet bai blog", "status": "Dang lam ⌛"},
    {"task": "sua loi code python", "status": "that bai ❌"},
    {"task": "hoc python", "status": "hoan thanh ✅"}
]
# bang for truoc

ten_task_co_python = []
for item in memory:
    if "python" in item["task"]:
        ten_task_co_python.append(item["task"])
print(ten_task_co_python)

# bang for sau khi nen lai

ten_task_co_python = [item["task"] for item in memory if "python" in item["task"]]
print(ten_task_co_python)
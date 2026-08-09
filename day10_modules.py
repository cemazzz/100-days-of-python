import json
import random
import time
# 1. danh sach cac cong viec
tasks = ["phan tich du lieu", "viet bai blog", "sua loi code", "tim kiem thong tin"]

print("🤖 AI agent dang khoi dong...")
time.sleep(1) # dung 1s de tao cam giac khoi dong

# 2. boc ngau nhien 1 cong viec
chosen_task = random.choice(tasks)
print(f"⚡ AI da chon cong viec: {chosen_task}")
print("⌛ dang xu ly...")
time.sleep(2) # dung 2s de tao cam giac xu ly

# 3. tao ket qua
result = {
    "task": chosen_task,
    "status": random.choice(["hoan thanh✅", "that bai❌"]),
    "speed": "2s"
}
print(f"--- ket qua ---", "\n 📝 nhiem vu: " ,result["task"])
print(f"📊 trang thai: {result['status']}")
print(f"⏱️ thoi gian hoan thanh: {result['speed']}")
# 4, luu ket qua vao json
try:
    with open("agent_day10.json", "w") as f:
        json.dump(result, f, indent=4)
    print("✅ da luu ket qua thanh cong vao agent day10.json!")
except Exception as e:
    print(f"⚠️ co loi khi luu: {e}")




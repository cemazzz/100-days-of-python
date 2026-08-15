import json
# tao du lieu
memory = [
    {"task": "viet bai blog", "status": "Dang lam ⌛"},
    {"task": "sua loi code", "status": "that bai ❌"},
    {"task": "hoc python", "status": "hoan thanh ✅"}
]
def luu_bo_nho(filename="agent_memory.json"):
    with open(filename, "w") as f:
      json.dump(memory, f , indent=4)
    print(f"💾 Da vinh vien bo nho vao file'{filename}' !")

 # test
luu_bo_nho()

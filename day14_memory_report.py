# tao du lieu
memory = [
    {"task": "viet bai blog", "status": "Dang lam ⌛"},
    {"task": "sua loi code", "status": "that bai ❌"},
    {"task": "hoc python", "status": "hoan thanh ✅"},
    {"task": "don phong tro", "status": "hoan thanh ✅"},
    {"task": "lau nha", "status": "Dang lam ⌛"}
]

#  VIET HAM
def tao_bao_cao():
    tong_task = len(memory)
    so_hoan_thanh = 0
    for item in memory:
        if item["status"] == "hoan thanh ✅":
            so_hoan_thanh = so_hoan_thanh + 1  
    ty_le = (so_hoan_thanh / tong_task) * 100  
    print("📊 --- BAO CAO HIEU SUAT AI AGENT ---")
    print(f"tong so cong viec: {tong_task}")
    print(f"so viec da hoan thanh: {so_hoan_thanh}")
    print(f"ty le hoan thanh: {ty_le:.1f}%")
tao_bao_cao()
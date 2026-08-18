import json
class AgentMemory:
    def __init__(self, filename="agent_memory.json"):
        self.filename = filename
        self.memory = self.load_memory() # tu dong tai file khi khoi tao

    def load_memory(self):
        try:
            with open(self.filename, "r" ) as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    def save_memory(self):
        with open(self.filename, "w" ) as f:
            json.dump(self.memory, f, indent=4)
        print("💾 Automatically permanently saved to file JSON!")

    def show_tasks(self):
        print("\n📋 List of tasks in memory:")
        for item in self.memory:
            print(f"- Task: {item['task']} | Status: {item['status']}")

    def add_task(self, task_name):
        self.memory.append({"task": task_name, "status": "in progress ⏳"})
        print(f"✅ Added: {task_name}")
        self.save_memory() # them xong tu luu luon


# TEST CLASS
# 1. Khởi tạo đối tượng Agent Memory (Chỉ 1 dòng duy nhất!)
agent_brain = AgentMemory()

# 2. Xem danh sách hiện tại
agent_brain.show_tasks()

# 3. Thêm task mới (Tự động append + tự động lưu file JSON)
agent_brain.add_task("Hoc OOP Python Day 19")

# 4. Xem lại danh sách sau khi thêm
agent_brain.show_tasks()



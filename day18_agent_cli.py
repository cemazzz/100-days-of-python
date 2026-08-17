import json

# 1. file processing functions  [VN:cac ham xu ly file]

def load_memory(filename="agent_memory.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_memory(data, filename="agent_memory.json"):
    with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    print("💾 automatically save memory contents to a file ! ")
    
# 2. MAIN PROGRAM (AGENT CLI)   [VN:chuong trinh chinh]
memory = load_memory()
print("🤖 AI AGENT Memory System is READY !")
while True:
    print("\n--- MENU AGENT ---")
    print("1. 👁️ View the task list")
    print("2. ➕ Add new task")
    print("3. 💾 SAVE & EXIT 🏃‍➡️")
    pick = input("⌨️ Enter your choice: ")
    if pick == "1":
        print("\nCurrent memory:")
        for item in memory:
            print(f"- 📋 Task: {item['task']} | 📊 Status: {item['status']}")
    elif pick == "2":
        new_task = input("📋 Enter a new task name: ")
        memory.append({"task": new_task, "status": "⌛ in progress"})
        print(f"✅ '{new_task} has been added to the clipboard !")
    elif pick == "3":
        save_memory(memory)
        print("🏃‍➡️ Exit the program \n GOODBYE 👋")
        break
    else:
        print("⚠️ Invalid selection, please select again !: ")
    
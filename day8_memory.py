import json

agent_history = [
    {"agent": "cemazzz", "task": "write python", "status": "SUCCESS"},
    {"agent": "cemazz", "task": "play game", "status": "FAILED"}
]

with open("agent_memory.json", "w") as f:
    json.dump(agent_history, f, indent=4)
print("Đã lưu bộ nhớ vào file agent_memory.json")

with open("agent_memory.json", "r") as f:
    loaded_data = json.load(f)

print("\n--- Bộ nhớ đã tải lên ---")
for a in loaded_data:
    print(f"Agent: {a['agent']} | Task: {a['task']} | Status: {a['status']}")
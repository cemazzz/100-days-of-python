ai_agent = {
    "name": "Jarvis",
    "model":"GPT-4o",
    "memory_capacity": "256GB",
    "skill":["coding", "data analysis", "english translation"],
    "is_online": True    
}
print("=== AI information ===")
print(f"Agent name: {ai_agent['name']}")
print(f"current model: {ai_agent['model']}")
print(f"Memory capacity: {ai_agent['memory_capacity']}")
print("\n... AI is updating ...")
ai_agent["model"] = "Gemini 1.5 pro"
ai_agent["skill"].append("computer vision")
ai_agent["creator"] = "Duy"
print("\n=== AI after update ===")
for key, value in ai_agent.items():
    print(f"- {key.capitalize()}: {value}")

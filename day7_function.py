def run_agent_task(agent_name, task_name, agent_level, task_difficulty=5):
    if agent_level >= task_difficulty:
        return {
            "status": "SUCCESS",
            "agent": agent_name,
            "task": task_name,
            "xp_gained": task_difficulty * 8.375
        }
    else:
        return {
            "status": "FAILURE",
            "agent": agent_name,
            "task": task_name,
            "reason": "level too low NOOB!"
        }
task1 = run_agent_task("cemazz", "write a python function", 6, 7)
task2 = run_agent_task("cemazz", "play a game", 10, 8)
print("=== test results ===")
print(f"Task 1: ","\n status: ", task1['status'], "\n agent: ", task1['agent'], "\n task: ", task1['task'],"\n reason: ", task1['reason'])
print(f"Task 2: ","\n status: ", task2['status'], "\n agent: ", task2['agent'], "\n task: ", task2['task'], "\n xp gained: ", task2['xp_gained']) 
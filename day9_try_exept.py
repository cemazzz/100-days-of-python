import json
try:
    with open("agent_memory_test.json", "r") as f:
        loaded_data = json.load(f)
        print("doc bo nho thanh cong")
except FileNotFoundError:
    print("⚠️   chua co file bo nho, tao moi nhe ?.")
    loaded_data = []
except json.JSONDecodeError:
    print("⚠️   file bi loi, reset lai bo nho!?.")
    loaded_data = []
except Exception as e:
    print(f"⚠️   co loi nao do xay ra : {e}")
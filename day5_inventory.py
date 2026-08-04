inventory = ["wooden sword", "shield", "health potion"]
print("starter pack:", inventory)

new_item = input("You found a new item! What is it? ")
inventory.append(new_item)

print("\n--- Your updated inventory ---")
print("total items:", len(inventory))
for item in inventory:
    print("-", item)
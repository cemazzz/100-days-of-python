# 1. Encapsulation (dong goi)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable (giau so du)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def get_balance(self):
        return self.__balance

# 2.Polymorphism (da hinh)
class FastCharger:
    def charge(self):
        print("⚡ Fast charging at 65W...")

class NormalCharger:
    def charge(self):
        print("🔌 Standard 10W charging...")


# --- TEST CODE---
# Test Encapsulation
acc = BankAccount("Duy MMO", 100)
acc.deposit(50)
print("Balance via function call:", acc.get_balance())

# Test Polymorphism (cung goi ham .charge() nhung chay logic khac nhau)
chargers = [FastCharger(), NormalCharger()]
for c in chargers:
    c.charge()
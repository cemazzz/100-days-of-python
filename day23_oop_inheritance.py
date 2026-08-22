class phone:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
class SmartPhone(phone):
    pass
my_smart = SmartPhone("iPhone 16", 100)
print(my_smart.name)
class phone:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
    def use_battery(self, amount = 36):
        self.battery -= amount
        print(f"{self.name} used {amount}% battery. Battery remaining: {self.battery}%")
    def charge(self):  
        self.battery = 100  
        print(f"🔋 {self.name} Fully charged to 100%!")
my_phone = phone("IQOO NEO 10", 100)
my_phone.use_battery(36)
my_phone.charge()
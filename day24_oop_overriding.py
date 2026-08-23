class Phone:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
class SmartPhone(Phone):
    def __init__(self, name, battery, os):
        self.os = os
        super().__init__(name, battery)
    def swipe_tiktok(self, hours):
        self.battery = hours * 6
        print(f"{self.name} {self.os} has spent {hours} hours browsing Tiktok, Remaining battery {self.battery}%")
my_phone = SmartPhone("samsung j7", 98, "Android")
my_phone.swipe_tiktok(3)
    
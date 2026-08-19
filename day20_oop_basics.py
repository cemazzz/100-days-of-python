class phone:                    # dinh nghia 1 ham ten la phone
    def __init__ (self, name_phone, battery, storage):    # Dùng hàm __init__ để nhận vào 3 thuộc tính: name_phone, battery, storage
        self.battery  = battery
        self.storage = storage
        self.name_phone = name_phone
my_phone = phone("IQOO NEO 10", 67, 256)      # Khởi tạo 1 đối tượng điện thoại tên là my_phone với thông số: iqoo neo 10 ,67, 256
 
print(f"Your phone 📱 {my_phone.name_phone} with 📁 {my_phone.storage} GB storage and 🔋 {my_phone.battery} % battery health ")
# 👆 in ra thoi
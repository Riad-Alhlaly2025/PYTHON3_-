#قم بانشاء كلاس باسم سيارة
#قم بانشاء دالة init داخل الكلاس تأخذ 3 باراميترات وهم نوع السيارة وسنة الصنع واللون
class Car:
    def __init__(self, car_type, year, color):
        self.car_type = car_type
        self.year = year
        self.color = color
#قم بانشاء دالة داخل الكلاس باسم display_info تقوم بطباعة نوع السيارة وسنة الصنع واللون
    def display_info(self):
        print(f"نوع السيارة: {self.car_type}")
        print(f"سنة الصنع: {self.year}")
        print(f"اللون: {self.color}")
#قم بانشاء كائن من الكلاس باسم my_car وقم بتمرير نوع السيارة وسنة الصنع واللون
my_car = Car("تويوتا", 2020, "أحمر")
#قم بانشاء كائن اخر من الكلاس باسم youer_car وقم بتمرير نوع السيارة وسنة الصنع واللون
youer_car = Car("هوندا", 2018, "أزرق")
#قم باستدعاء دالة display_info لطباعة معلومات السيارة
my_car.display_info()
#قم باستدعاء دالة display_info لطباعة معلومات السيارة
youer_car.display_info()
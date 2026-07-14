
#*** المطلوب ثلاثة واجبات تتعلق بالكلاس *********

#** الواجب الاول *********
# انشاء كلاس باسم Profile
#وضع فيه الخصائص التالية : الاسم المستخدم ، ايميله ،واللغة المفضلة   
# يخزن بيانات المستخدمين على التطبيق تبعك ويكون فية التالي
#اسم المستخدم : name
#ايميل المستخدم : email
#اللغة المفضلة : language

class Profile:
    def __init__(self, name, email, language):
        self.name = name
        self.email= email
        self.language= language
        
    def display_info(self):
        print(f"اسم المستخدم: {self.name}")
        print(f"الايميل :{self.email}")
        print(f"اللغة المفضلة : {self.language}")

#انشاء كائنات واسناد لهم بيانات
new1_profile = Profile("Riad", "riad@gmail.com", "Arbice")
new2_profile = Profile("Ahmed", "ahmed@gmail.com", "English")
new3_profile = Profile("Ali", "ali@gmail.com", "Chaine")

# التالي طباعة الكائنات
new1_profile.display_info()
new2_profile.display_info()
new2_profile.display_info()

#****************************************************

#********* الواجب الثاني **************************
#*** Massage اسم الكلاس
# انشاء كلاس تطبيق الدردشة 
# كلاس لتطبيق دردشة مثل واتس اب وتلجرام يتعامل مع الرسايل ك كائنات
# في هذا الكلاس بتكون الخصائص على الشكل التالي:
# اسم المرسل \ اسم المتسقبل \ محتوئ الرسالة \ تاريخ الارسال
# وبتكون دالة داخل الكلاس لعرض الرسالة بشكل منسق
# مثال على البيانات التي يمكن تخزينها في الكلاس
# اسم المرسل : sender
# اسم المتسقبل : receiver
# محتوئ الرسالة : content
# تاريخ الارسال : date

class Massage:
    def __init__(self, sender, receiver, content, date):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.date = date
        
    def display_message(self):
        print(f"المرسل: {self.sender}")
        print(f"المستقبل: {self.receiver}")
        print(f"محتوى الرسالة: {self.content}")
        print(f"تاريخ الارسال: {self.date}")
#انشاء كائنات واسناد لهم بيانات
new1_massage = Massage("Riad", "Ahmed", "مرحبا كيف حالك؟", "2024-06-04")
new2_massage = Massage("Ahmed", "Riad", "انا بخير شكرا لك!", "2024-06-10")
new3_massage = Massage("Ali", "Riad", "هل تريد الخروج اليوم؟", "2024-06-23")

# التالي طباعة الكائنات
new1_massage.display_message()
new2_massage.display_message()
new3_massage.display_message()

#****************************************************

#********* الواجب الثالث **************************
#*** Product اسم الكلاس
# لمنصة تسوق الكترونيه مثل سوق كوم او امازون
# انشاء كلاس خاص بالمنتجات في المنصة
# في هذا الكلاس بتكون الخصائص على الشكل التالي:
# اسم المنتج \ سعر المنتج \ تقييم المنتج \ عدد المبيعات
# خصائص الكائنات في الكلاس
# اسم المنتج : name
# سعر المنتج : price
# تقييم المنتج : rating
# عدد المبيعات : sales

class Product:
    def __init__(self, name, price, rating, sales):
        self.name = name
        self.price = price
        self.rating = rating
        self.sales = sales
        
    def display_product(self):
        print(f"اسم المنتج: {self.name}")
        print(f"سعر المنتج: {self.price}")
        print(f"تقييم المنتج: {self.rating}")
        print(f"عدد المبيعات: {self.sales}")
        
#انشاء كائنات واسناد لهم بيانات
new1_product = Product("هاتف سامسونج", 1500, 4.5, 200)
new2_product = Product("لابتوب ديل", 3000, 4.0, 150)
new3_product = Product("سماعات بلوتوث", 200, 4.8, 500)

# التالي طباعة الكائنات
new1_product.display_product()
new2_product.display_product()
new3_product.display_product()


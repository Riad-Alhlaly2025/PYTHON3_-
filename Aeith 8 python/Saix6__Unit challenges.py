
#اولا تحدي لنهاية الوحدة
#********(> <المستوئ السهل والمستوئ متوسط - <برنامج أدارة المستخدميين>-<برنامج بوصفات الطعام)تحدي البرمجة الكائنية********

#كلاس الوصفات  
#تهيئة: اسم, مكونات, وقت الطهي, التعليمات
#ميثود للطباعة
#فانكشن خارجية لانشاء وصفة

#**************تعليمات وانشاء البرنامج******************
#البرنامج عبارة عن برنامج لتخزين وصفات الطعام باستخدام البرمجة الكائنية
#كلاس Collection يحتوي على خصائص الوصفة مثل الاسم والمكونات ووقت الطهي والتعليمات
#انشاء كائن من الكلاس Collection باستخدام دالة recipe التي تطلب من المستخدم إدخال البيانات
#وعرض البيانات المخزنة في الكائن باستخدام دالة displaying

class Collection:
    def __init__(self, name, ingredients, times, instruction):
        #ادراج الاسم والمكونات ووقت الطهي والتعليمات في الكائنات
        self.name = name
        #ادراج المكونات في الكائنات
        self.ingredients = ingredients
        #ادراج وقت الطهي في الكائنات
        self.times = times
        #ادراج التعليمات في الكائنات
        self.instruction = instruction
        
        
#دالة recipe تطلب من المستخدم إدخال البيانات لإنشاء كائن من الكلاس Collection
def recipe():
    name =input("Enter recipe name: ")
    ingredients =input("Enter ingredients (comma--separated):  ")
    times =input("Enter cookingtime:  ")
    instruction =input("Enter cooking instruction: ")
    
    return Collection(name,ingredients,times,instruction)
#دالة لعرض البيانات المخزنة في الكائنات
def displaying(Collection):
    print(f"Name: {Collection.name}")
    print(f"Ingredients: {Collection.ingredients}")
    print(f"Cooking Time: {Collection.times}")
    print(f"Instructions: {Collection.instruction}")
    print("***************************************")


print("Welcime to Recipe Collection\n")
#استدعاء دالة recipe لإنشاء كائن من الكلاس Collection باستخدام البيانات المدخلة من قبل المستخدم
user1 =recipe()

print("Displaying recipe ....")

#عرض البيانات المخزنة في الكائن باستخدام دالة displaying
user1=displaying(user1)
#print(f"Name: {user1.name}\nIngredients:{user1.ingredients}\nCooking Time:{user1.times}\nInstructions:{user1.instruction}")









#ثانيا تحدي لنهاية الوحدة
#******برنامج ادارة المستخدمين باستخدام البرمجة الكائنية********
# المتطلبات: انشاء كلاس User يحتوي على خصائص المستخدم مثل الاسم الاول والاسم الاخير والبريد الالكتروني وكلمة المرور والحالة
#في البداية يعرض للمستخدم اختار واحد من اليكشن الثلاثة التاليه
#اضافة مستخدم جديد اضغط 1
#عرض بيانات المستخدمين اضغط 2
#الخروج من البرنامج اضغط 3

#اذا اختار المستخدم 1 يتم استدعاء دالة create_user التي تطلب من المستخدم إدخال البيانات لإنشاء كائن من الكلاس User
#وبعد ان يدخل بياناته تضهر الرساله الاوله اختار واحد من اليكشن الثلاثة التاليه

#اذا اختار المستخدم 2 يتم عرض بيانات المستخدمين المخزنة في الكائنات باستخدام دالة displaying
#وبعد عرض البيانات تضهر الرساله الاوله اختار واحد من اليكشن الثلاثة التاليه

#اذا اختار المستخدم 3 يتم الخروج من البرنامج

#***نتمنى ان يكون البرنامج سهل الاستخدام ومرن في التعامل مع المستخدمين.
#بداية نكتب البرنامج المطلوب باستخدام البرمجة الكائنية في بايثون.


class User:
    #دالة init تقوم بتهيئة خصائص المستخدم عند انشاء كائن جديد من الكلاس User
    def __init__(self, first_name, last_name, email, password, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

#دالة create_user تطلب من المستخدم إدخال البيانات لإنشاء كائن من الكلاس User
def create_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    return User(first_name, last_name, email, password)


#الدالة displaying تعرض بيانات المستخدم المخزنة في الكائنات
def displaying(user):
    print(f"UserName: {user.first_name},\nLastName: {user.last_name},\nGmail: {user.email},\nPassword: {user.password}\nStatus: {user.status}")

#نوع من الحاويات لتخزين المستخدمين
#بالاول يتم انشاء قائمة فارغة لتخزين المستخدمين
users = []
#انضاف المستخدمين الجدد الى القائمة
while True:
    #عرض رسالة الترحيب والاختيارات للمستخدم
    print("\nWelcome to User Management System\n")
    print("\nChoose an Action:\n")
    print("1. Add a new user")
    print("2. Display users")
    print("3. Exit")
    
    #طلب من المستخدم اختيار احد الخيارات الثلاثة
    choice = input("Enter your choice (1/2/3): ")
    
    #التحقق من اختيار المستخدم وتنفيذ الاجراء المناسب
    if choice == "1":
        user = create_user()
        users.append(user)
        print("User added successfully!")
        
    elif choice == "2":
        if not users:
            print("No users to display.")
        else:
            for i, user in enumerate(users, start=1):
                print(f"\nUser {i}:")
                displaying(user)
                
    elif choice == "3":
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please try again.")
#كلاس المستخدم
#
#برنامج بسيط بلغة بايثون يوضح كيفية إنشاء كلاس يمثل المستخدمين في نظام معين. يحتوي الكلاس على خصائص مثل الاسم الأول، الاسم الأخير، البريد الإلكتروني، كلمة المرور، وحالة المستخدم (نشط أو غير نشط). كما يحتوي البرنامج على دالة لإنشاء مستخدم جديد من خلال إدخال البيانات من قبل المستخدم.

class User:
    def __init__(self, first_name, last_name, email, password, status="inactive"):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status
    
def create_user():
    first_name =input("Enter your first name:")
    last_name =input("Enter your last name:")
    email =input("Enter your  email:")
    password =input("Enter your password:")
        
    return User(first_name, last_name, email, password)
    
user2 =create_user()

print("********بيانات المستخدم الجديد*********")
print(f"UserName: {user2.first_name},\nLastName:{user2.last_name},\nGmail:{user2.email},\nPassword:{user2.password}\nStatus:{user2.status}")

#print(user2.first_name,"\n",user2.email)

user1 = User("Riadh", "Alylaly", "riad@gmail.com", "123456")
print(f"\nThis user name is {user1.first_name} and his email is {user1.status}")

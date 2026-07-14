#برنامج ادارة اشتراكات الجيم

#المطلوب كالتالي:

#اول ما يشتغل البرنامج يضهر رسالة ترحيب وبعدها يقول اختار احد الخيارات التالية:
#اضافة مستخدم جديد
#عرض اعضاء المستخدمين
#البحث عن مستخدم
#الخروج من البرنامج


# مثلا اخترت اضافة مستخدم جديد
#تختفي رسالة الترحيب وتظهر رسالة جديدة تقول ادخل البيانات التالية:
#يطلب ادخال الاسم[first_name] و الاسم[last_name] ورقم[qid] وادخال اكتيف او اينكتيف او اضغط انتر يعني يتركه على الوضع الافتراضي وهو اينكتيف
#بعد ما يدخل البيانات يضهر رسالة تقول تم اضافة المستخدم بنجاح
#وبعدها يرجع يضهر رسالة الترحيب مرة اخرى ويطلب منك اختيار احد الخيارات التالية:

# مثلا اخترت عرض اعضاء المستخدمين
#تختفي رسالة الترحيب وتظهر رسالة جديدة تقول اعضاء المستخدمين هم: مع مراعاة حالة المستخدم اذا كانت اكتيف او اينكتيف
#بعد خمس ثواني يرجع يضهر رسالة الترحيب مرة اخرى ويطلب منك اختيار احد الخيارات التالية:

# مثلا اخترت البحث عن مستخدم
#تختفي رسالة الترحيب والاختيارات وتضهر رسالة تقول اختر بماذا تريد البحث عن المستخدم:
#1. البحث بالاسم[first_name]
#2. ابحث برقم[qid]
#3. البحث بحالة المستخدم

#مثلا اخترت البحث بالاسم[first_name]
#تضهر رسالة تقول ادخل الاسم[first_name] الذي تريد البحث عنه:    
#وبعد ادخال اسم المستخدم تختفي رسالة البحث وتضهر بياناته
#وبعد ان تضهر البيانات تضل لفترة 5 ثواني وتختفي وتضهر رسالة الترحيب مرة اخرى ويطلب منك اختيار احد الخيارات التالية:

#ونطبق على نفس هذا النمط في قائمة البحث للبحث بالرقم او بالحالة المستخدم


# في حالة ادخلت بيانات غلط تضهر رسالة تقول البيانات التي ادخلتها غير صحيحة حاول مرة اخرى وتعيد اضهار رسالة الترحيب مرة اخرى ويطلب منك اختيار احد الخيارات التالية:

#نهاية البرنامج تكون عند اختيارك للخيار الرابع وهو الخروج من البرنامج


#نبدا بكتابة كود الكلاس
import time
import os

def clear_screen():
    # Clear the console screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')

class User:
    def __init__(self, first_name, last_name, qid, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.qid = qid
        self.status = status
        
def create_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    qid = input("Enter your QID: ")
    status = input("Enter status (active/inactive) or press Enter for default (inactive): ") or "inactive"
    
    return User(first_name, last_name, qid, status)

def display_user(user):
    print(f"UserName: {user.first_name}\nLastName: {user.last_name}\nQID: {user.qid}\nStatus: {user.status}")
    

users = []

while True:
    clear_screen()
    print("\nWelcome to Gym Subscription Management System\n")
    print("Choose an Action:\n")
    print("1. Add new user")
    print("2. Display all users")
    print("3. Search for a user")
    print("4. Exit")
    
    choice = input("Enter your choice (1, 2, 3, 4): ")
    
    if choice == "1":
        clear_screen()
        user = create_user()
        users.append(user)
        print("User added successfully!")
        clear_screen()
    elif choice == "2":
        clear_screen()
        if not users:
            print("No users to display.")
        else:
            print("\nDisplaying all members ....\n")
            for user in users:
                display_user(user)
                print("-------------------------")
        time.sleep(5)
        clear_screen()
    elif choice == "3":
        if users:
            
            clear_screen()
            search_choice = input("Search by:\n1. First Name\n2. QID\n3. Status\nEnter your choice (1, 2, 3): ")
        
            if search_choice == "1":
                search_name = input("Enter the first name to search: ")
            
                found_users = []
                for user in users:
                    if user.first_name.lower() == search_name.lower():
                        found_users.append(user)
                if found_users:
                    for user in found_users:
                        display_user(user)
                else:
                    print("No users found with that first name.")
                
            elif search_choice == "2":
                search_qid = input("Enter the QID to search: ")
                #found_users = [user for user in users if user.qid == search_qid]
                found_users = []
                for user in users:
                    if user.qid == search_qid:
                        found_users.append(user)
                        print(20 * "_")
                    
                if found_users:
                    for user in found_users:
                        display_user(user)
                        print(20 * "__")
                else:
                    print("No users found with that QID.")
                
            elif search_choice == "3":
                search_status = input("Enter the status (active/inactive) to search: ")
                found_users =[]
            
                for user in users:
                    if user.status.lower() == search_status.lower():
                        found_users.append(user)
                        print(20 *"_")
            
            #[user for user in users if user.status.lower() == search_status.lower()]
            
                if found_users:
                    for user in found_users:
                        print("-------------------------")
                        display_user(user)
                else:
                    print("No users found with that status.")

            else:
                print("Invalid choice. Please try again.")
        else:
            print("No users to search!")    
            time.sleep(2)
            
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
        time.sleep(2)
        
        
        















#Welcome to Recipe Collection 
#Enter recipe name: 
#Enter ingredients (comma-separated): 
#Enter cooking time: 
#Enter cooking instructions: 

#بعد ادخال المطلوب يضهر الرساله التالية
#Recipe added successfully!

#وبعدها تضهر النتائج وقبلها الرسالة التالية
#Displaying recipe ....

#name, Ingredients:, Cooking Time:, Instructions: 
#__________________________

# class Food:
#     def __init__(self,name,ingredients,cooking_time,instructions):
#         self.name = name
#         self.ingredients = ingredients
#         self.cooking_time = cooking_time
#         self.instructions = instructions
        
        
        
# def displaying():
#     name = input("Enter recipe name: ")
#     ingredients = input("Enter ingredients (comma-separated): ")
#     cooking_time = input("Enter cooking time: ")
#     instructions = input("Enter cooking instructions: ")
#     return Food(name, ingredients, cooking_time , instructions)

# def users_display(user):
#     print(f"Name User: {user.name}\nIngredients: {user.ingredients}\nCooking_time: {user.cooking_time}\nInstructions: {user.instructions}")


# print("Welcome to user  management \n")
# user2 = displaying()
# print("Recipe added successfully!\n")


# print("Displaying recipe ....")
# users_display(user2)
# print(20 *"_")

# #Welcome to user  management
# #Choose an Action:
# #1. Add new user
# #2. Display all users
# #3. Exit

# class management:
#     def __init__(self, name, last_name, gmail, password,status = "inactive"):
#         self.name = name
#         self.last_name = last_name
#         self.gmail = gmail
#         self.password = password
        

# def dispaly_manage():
#     name  =input("Enter first name: ")
#     last_name = input("Enter last name: ")
#     gmail = input("Enter gmail: ")
#     password = input("Enter passwourd: ")
    
#     return management(name, last_name, gmail, password)
    

# def print_name(user):
#     print(f"Frist name: {user.name}\nLast Name: {user.last_name}\nEmail: {user.gmail}\nPassword: {user.password}")

# users= []

# while True:
    
#     print("""
# Welcome to user  management
    
# Choose an Action:

# 1. Add new user
# 2. Display all users
# 3. Exit
#         """)
    
#     choice = input("Enter your Choice: (1,2,3)")
    
#     if choice == "1":
#         user = dispaly_manage()
#         users.append(user)
#         print("User added successfully!\n")
        
#     elif choice == "2":
#         if not users:
#             print("Sorry. didn't find any user to display!")
            
#         else:
#             print("Displaying all users.....")
#             for i in users:
#                 print_name(i)
#                 print(20 *"___")
                
#     elif choice == "3":
#         print("Exiting .....")
#         break
    
#     else:
#         print("No, Sorry !!!!!!!!")
















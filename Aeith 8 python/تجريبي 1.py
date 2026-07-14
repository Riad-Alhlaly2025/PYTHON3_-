
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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
        
        users.append( create_user())
        print("User added successfully!")
        time.sleep(4)
        
    elif choice == "2":
        clear_screen()
        if not users:
            print("No users to display.")
            time.sleep(2)
        else:
            print("Displaying all members ....\n")
            time.sleep(2)
            for i in users:
                print("-------------------------")
                displaying(i)
            time.sleep(5)
            

    elif choice == "3":
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please try again.")



















#****************************************************************************
# class User:
#     def __init__(self, name, last, email, password, status="inactive"):
#         self.name = name
#         self.last = last
#         self.email = email
#         self.password = password
#         self.status = status
        
        
# def choose():
#     name= input("Enter your frist name: ")
#     last =input("Enter last name: ")
#     email = input("Enter email: ")
#     password = input("Enter password: ")
    
#     return User(name,last,email,password)

# def displaying(user):
#     print(f"UserName: {user.name},\nLastName: {user.last},\nGmail: {user.email},\nPassword: {user.password}\nStatus: {user.status}")


# users=[]

# while True:
#     print("\nWelcome to User Management Systme\n")
#     print("Choose an Action:\n")
#     print("1. Add new user")
#     print("2. Display all users")
#     print("3. Exit")
    
#     choice=input("Enter your choice:(1,2,3):  ")
    
#     if choice =="1":
#         user= choose()
#         users.append(user)
#         print("User added successfully!")
        
#     elif choice == "2":
#         if not users:
#             print("No users to display.")
#         else:
#             for i, user in enumerate(users, start=1):
#                 print(f"\n User {i}")
#                 displaying(user)
                
#     elif choice == "3":
#         print("Exiting the program.")
#         break
    
#     else:
#         print("Invalid choice. Please try again.")
        
        
                
        







# import random
# words = ["office", "panda", "cabin", "ginger"]
# random_word = random.choice(words)
# print(random_word)

# l=[]
# for i in random_word:
#     l.append("_")
    
# print(l)
# while "_" in l:
    
#     guess =input("Please guess a letter: ").lower()

#     for position in range(len(random_word)):
#         if random_word[position] == guess:
#             l[position]=guess
#     print(l)

# print("""
#       ***********
#       YOU WIN!
#       ***********
#       """)

# for i in random_word:
#     if i == guess :
#         print("Right")
#     else:
#         print("Wrong")


# import numpy as np
# s = np.array([
#     [1,2,3,4],
#     [2,3,4,5],
#     [3,4,5,6],
#     [4,5,6,7]
# ])

# n=0
# for i in range(0, 4):
#     n = n+ s[i, 0]
# print(f"مجموع عناصر العمود الاول :{n}")
# def num():
    
#     m=0
#     for j in range(0,4):
#         m = m+ s[j, 3-j]
#     print(f"مجموع عناصر القطر الرئيسي {m}")
    
# num()

# k=0
# for f in range(0, 4):
#     k = k+ s[f, f]
# print(k)


#x =[1,4,3,8,9,6,2]
# for i in range(0,len(x)):
#     for j in range(0, len(x)-1):
#         if x[i] < x[j]:
#             t=[j]
#             x[j] = x[j+1]
#             x[j+1] =t



# for i in range(len(x)):
#     for j in range(i+1, len(x)):
#         if x[i] > x[j]:
#             x[i], x[j] =x[j], x[i]
# print(x)



# طلب من المستخدم ادخال 10 ارقام وايجاد الرقم الاكبر من بينهم
# num=[]

# for i in range(10):
#     n=int(input("Enter numper: "))
#     num.append(n)
# m=0

# for j in num:
#     if j > m:
#         m = j

# print(m)


# print(num)

# طباعه شكل النجمه على البعد المعطاء
# x =1
# while(x<37):
#     x+=1
#     print("*",end =" ")
    
#     if (x% 6==1):
#         print(" ")


# التحقق من الرقم المدخل هل هو عدد اولي او ليس اولي
# n =int(input("Enter numper : "))
# if n <= 1:
#     print("the numper is not prime")
    
# else:
#     s=True
#     for i in range(2, n):
#         if n %i==0:
#             s=False
#             break
#     if s:
#         print("the numper is prime")
        
#     else:
#         print("the numper is not prime")
    


# ماهي مخرجات الكود التالي

# for n in range(0, 30):
#     print(n, end=" ")
    
#     if(n %4==1):
#         print(" ")





#اكتب برنامج يتحقق من الرقم هل هو فردي او زوجي

# n =int(input("Enter numper : "))
# if n %2==0:
#     print("Thr numper is zojee odd")
# else:
#     print("The numper is not zojee odd")





# l =[1,3,2,5,2,4,1,3,2,1,4,3]
# #طباعه عناصر القائمة بدون تكرار
# m=[]
# for i in l:
#     if i not in m:
#         m.append(i)
        
# print(m)

# #طباعه عدد تكرار كل عنصر
# for x in m:
#     count =l.count(x)
    
#     print(x, ": ", count)



# x=1
# while x < 36:
#     x +=1
#     print("*", end=" ")
#     if (x %6==1):
#         print(" ")





#* اكتب المخرجات
# *ماهي الخطاء في البرنامج
#* صحح الخطاء في البرنامج
#* اختر الاجابة

#ايجاد جمع رقمين المدخله
# num1 =int(input("Enter numper On1: "))
# num2 =int(input("Enter numper To2: "))

# sums =num1 + num2
# print(sums)




# #برنامج يوجد مضروب العدد المدخل
# n =int(input("Enter numper: "))
# s =1
# for i in range(1,n+1):
#     s =s * i
# print(s)



# n =int(input("Enter: "))
# k=1
# for i in range(1,n+1):
#     k = k* i

# print(k)








# n=input("Enter numpers For: ")

# j=0
# for i in n:
#     j +=int(i)
    
# print(j)

# import numpy as np

# x =np.array([
#     [1,2,3,5],
#     [2,3,4,5],
#     [3,4,5,6],
#     [4,5,6,7]
# ])


# p=0
# for w in range(0,4):
#     p = p+ x[w,0]

# print("ppp: ",p)

# s=0
# for i in range(0, 4):
#     s = s + x[0,i]

# print(s)


# k =0
# for l in range(0,4):
#     k = k + x[l,l]

# print(k)


    
# a=0
# for m in range(0,4):
#     a = a + x[m, m - 1]
    
# print(a)








#************الواجهات (تجريبي فقط)*****************

# from tkinter import *
# too = Tk()
# too.title("My First GUI")
# too.geometry("400x400")

# def click():
#     s1=E1.get()
#     s2=E2.get()
#     sum = int(s1) + int(s2)
    
#     E3.insert(0, sum)

# L1 = Label(too, text="Enter numper 1: ")
# L1.grid(row=0, column=0)
# E1=Entry(too)
# E1.grid(row=0, column=1)

# L2 = Label(too, text="Enter numper 2: ")
# L2.grid(row=1, column=0)
# E2=Entry(too)
# E2.grid(row=1, column=1)

# L3=Label(too, text="Sum: ")
# L3.grid(row=2, column=0)
# E3=Entry(too)
# E3.grid(row=2, column=1)

# B1=Button(too, text="Calculate", command=click)
# B1.grid(row=3, column=0, columnspan=2)
# too.mainloop()
#















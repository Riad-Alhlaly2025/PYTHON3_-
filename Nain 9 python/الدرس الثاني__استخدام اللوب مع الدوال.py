
#*** في هذا الدرس سوف نتعلم في بدايته بعض الدوال الخاصه بالسلحفاة (Turtle) وواجهة السلحفاة (Screen) ونتعلم كيف نرسم مربع ودائرة باستخدام لوب (for loop) ونتعلم كيف نتحكم في شكل السلحفاة ولونها وسرعتها وحجم الخط الذي تتركه خلفها عند المشي


#تضمين المكتبات
from turtle import Turtle, Screen
import random
#تعريف نافذة السلحفاة
num =Turtle()
window = Screen()

#تحديد شكل السلحفاة
# num.shape("turtle") #** اشكال غير السلحفاة مثلا
# # بدل شكل السلحفاة turtle هذا   ** square , triangle, circle, classic, arrow 

# # لون السلحفاة
# num.color("red")


# #خصائص السلحفاة بطئ او سريع
# num.speed("fastest")# تستخدم لتسريع السلحفاة
# num.speed("slowest")# تستخدم لتبطئ السلحفاة


# #*** نتعرف على دوال القلم (رسم الخط ) الي بتتركه خلفها السلحفاة عند المشي
# #خصائص السلحفاة عند المشي
# num.penup() #تمشي ولا ترسم خلفها خط (مخفي)
# num.forward(100)

# num.pendown() # تترك خلفها اثر خط (خط ضاهر عند المشي)
# num.forward(100)

# num.pensize(10) # تحديد حجم الخط 
# num.forward(100)

#**       التحكم في ابعاد النافذة الي بترتسم عليها السلحفاة
window.setup(width=500, height=500) # تستخدم لتحديد ابعاد الشاشة طول وعرض


#**   تحديد لون الشاشة
window.bgcolor("black") #تغيير لون خلفية الشاشة


#** لوب لعمل مربع
# for _ in range(4):
#     num.forward(100)
#     num.left(90)


#** لوب لعمل رسمة دائرة
# for _ in range(360):
#     num.forward(1)
#     num.left(1)

#*******************************************************************
#*                      (واجب الدرس الثاني)                               *
#*******************************************************************
#* يلزم تضمين مكتبة العشوائية (random) في بداية الكود
#* مطلوب واجب باستخدام فونكتشن
#عمل دالة عند تشغيلها ترسم مربع وفي كل خط ترسمه له شكل مختلف عن الخط السابق
# يعني استخدم طريقه العشوائية في اختيار شكل الخطوط ولونها وحجمها


def draw_square(turtle):
    for _ in range(4):
        turtle.shape(random.choice(["turtle", "square" , "triangle", "circle", "classic", "arrow" ]))
        turtle.color(random.choice(["red", "blue", "green", "yellow"]))  # تغيير لون الخط
        turtle.pensize(random.randint(2, 15))     # تغيير حجم الخط
        turtle.forward(100)
        turtle.left(90)


#استدعاء دالة المربع العشوائي
draw_square(num)









window.exitonclick()


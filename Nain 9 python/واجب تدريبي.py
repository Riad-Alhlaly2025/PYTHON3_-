import random
from turtle import Turtle, Screen


# تم استدعاء كلاسين مهميين وهما التالي:
# Turtle: يتحكم في السلحفاة التي تظهر على الشاشة
# Screen: يستخدم للتحكم في النافذة التي ترسم عليها السلحفة

window = Screen()
window.setup(600, 400)
window.bgcolor("white")
window.title("واجهة السلحفاة")

sam = Turtle()
sam.speed("slowest")  # تستخدم لتبطئ السلحفاة

# مطلوب واجب باستخدام فونكتشن
#عمل دالة عند تشغيلها ترسم مربع وفي كل خط ترسمه له شكل مختلف عن الخط السابق
# يعني استخدم طريقه العشوائية في اختيار شكل الخطوط ولونها وحجمها

def draw_square(turtle):
    for _ in range(4):
        turtle.shape(random.choice(["turtle", "square" , "triangle", "circle", "classic", "arrow" ]))
        turtle.color(random.choice(["red", "blue", "green", "yellow"]))  # تغيير لون الخط
        turtle.pensize(random.randint(1, 10))     # تغيير حجم الخط
        turtle.forward(100)
        turtle.left(90)

#square , triangle, circle, classic, arrow 

# def draw_triangle(turtle):
#     for _ in range(8):
#         turtle.forward(100)
#         turtle.left(45)


draw_square(sam)









#draw_triangle(ali)

window.exitonclick()

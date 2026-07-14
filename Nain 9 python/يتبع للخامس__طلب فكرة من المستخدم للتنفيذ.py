

#****************(برنامج ينفذ رسومات المستخدم)**********************

#تحدي الدرس الخامس كالتالي
#اول ما يشتغل يضهر رسالة تقول لحضة من فضلك , مالذي تريد ترسمة؟ دائرة, مربع , مثلث
# بالمناسبة بيفهم اللغة المدخله عربي و الانجليزي
# مثلا ادخل المستخدم كلمة دائرة سيركل . تختفي رسالةالادخال وتضهر رسمة الدائرة وتعيد ضهور رسالة تقول لحضة من فضلك , مالذي تريد ترسمة؟ دائرة, مربع , مثلث
# وتتطبق نفس الشيء على المربع والمثلث
# الرسومات تبداء من منطقة 0,0 في نافذه واحدة

#ومثلا لو ادخل المستخدم اسم غلط البرنامج يضل على وضعه ولا يتغير شي و يضل يعيد نفس الرسالة لحضة من فضلك , مالذي تريد ترسمة؟ دائرة, مربع , مثلث
#او مثلا اذا كتبت اقزيت exit بيعرض لي في الشاشة كلام عربي وانجليزي بيقول اضغط في اي مكان للخروج من البرنامج


from turtle import Turtle, Screen

sam = Turtle()
window = Screen()
window.title("تحدي الدرس الخامس")

user_name = window.textinput("تحدي الدرس الخامس", "لحضة من فضلك , مالذي تريد ترسمة؟ دائرة, مربع , مثلث")
#user_name.hideturtle()

while True:
    if user_name.lower() == "دائرة" or user_name.lower() == "circle":
        sam.shape("circle")
        sam.pensize(1)  # Reset the shape size to default
        sam.color("red")  # Reset the shape size to default
        # Reset the shape size to default
        #square , triangle, circle, classic, arrow 
        sam.circle(50)
        user_name = window.textinput("تحدي الدرس الخامس", "لحضة من فضلك , مالذي تريد ترسمة؟ دائرة, مربع , مثلث")
    elif user_name.lower() == "مربع" or user_name.lower() == "square":
        sam.shape("square")
        sam.pensize(3)  # Reset the shape size to default
        sam.color("blue")  # Reset the shape size to default
        for _ in range(4):
            sam.forward(100)
            sam.right(90)
        user_name = window.textinput("تحدي الدرس الخامس", "لحضة من فضلك , مالذي تريد ترسمة؟ دائرة, مربع , مثلث")
    elif user_name.lower() == "مثلث" or user_name.lower() == "triangle":
        sam.shape("triangle")
        sam.pensize(2) # Reset the shape size to default
        sam.color("green")  # Reset the shape size to default
        for _ in range(3):
            sam.forward(100)
            sam.right(120)
        user_name = window.textinput("تحدي الدرس الخامس", "لحضة من فضلك , مالذي تريد ترسمة؟ دائرة, مربع , مثلث")
    elif user_name.lower() == "exit" or user_name.lower() == "خروج":
        
        #عندما يكتب المستخدم كلمة خروج او exit بيضهر له رسالة تقول اضغط في اي مكان للخروج من البرنامج
        #قبل ضهور الرسالة لازم مسح جميع الرسومات الموجوده على الشاشة وبعدها تضهر رسالة اضغط في اي مكان للخروج من البرنامج
        
        sam.clear()  # Clear the previous drawings
        sam.write(f"اضغط في اي مكان للخروج من البرنامج\n", font=("arial", 24,"bold"), align="center")
        
        sam.write(f"\nPress anywhere to exit the program", font=("arial", 24,"bold"), align="center") 
        sam.hideturtle()
        if window.onclick(lambda x, y: window.bye()):  # Wait for a click to exit the program
            
            window.exitonclick()  # Wait for a click to exit the program
            break  # Exit the loop after the click 
        
    else:
        user_name = window.textinput("تحدي الدرس الخامس", "لحضة من فضلك , مالذي تريد ترسمة؟ دائرة, مربع , مثلث")



window.exitonclick()
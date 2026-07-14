
#المقصد من الكلاس هو انشاء كائنات متعددة من نفس النوع (مثل الافلام) وتخزين بيانات مختلفة في كل كائن
#وعمل دالة داخل الكلاس لتعديل البيانات المخزنة في الكائنات (مثل تغيير اسم المخرج)
#العرض البيانات المخزنة في الكائنات بعد التعديل للتأكد من ان التعديل تم بنجاح

#المقصد عمل دوال كثيرة وتخلي الكائن يتعامل معها
#رسالة (قائمة الافلام)
#ثلاثة كائنات وتخزين فيهم بيانات مختلفة
#رسالة (جاري تعديل البيانات)
#عرض الكائنات مرة اخر وتغيير بيانات الاسماء السابقة


class Movire: #اسم الكلاس
    
    def __init__(self, title, director, releasa_year, genre):#دالة الانشاء (المقصد منها تخزين البيانات في الكائنات)
        
        self.title = title
        self.director = director
        self.releasa_year = releasa_year
        self.genre = genre
        
        
    def profile_print(self):#دالة العرض (المقصد منها عرض البيانات المخزنة في الكائنات)
        
        print(f"Title : {self.title}")
        print(f"Director : {self.director}")
        print(f"Releasa_Year : {self.releasa_year}")
        print(f"Genre : {self.genre}")
        print("\n")
        
    def object_profile(self, new_name):#دالة التعديل (المقصد منها تعديل البيانات المخزنة في الكائنات)
        self.director = new_name       #تعديل اسم المخرج في الكائنات
        
    
#وضع بيانات مختلفة في كل كائن (مثل اسم الفيلم، اسم المخرج، سنة الاصدار، نوع الفيلم)

print("\n_________ MOVIES LIST _______\n")#رسالة (قائمة الافلام)
new1_movie = Movire("Inception", "Christopher Nolan", 2010, "Sci-Fi")#انشاء كائن الاول من الكلاس وتخزين بيانات 
new1_movie.profile_print() #عرض بيانات الكائن الاول

new2_movie = Movire("The Godfather", "Francis Ford Coppola", 1972, "Crime") #انشاء كائن الثاني من الكلاس وتخزين بيانات مختلفة عن الكائن الاول
new2_movie.profile_print() #عرض بيانات الكائن الثاني للتأكد من ان البيانات المخزنة مختلفة عن الكائن الاول

new3_movie = Movire("Parasite", "Bong Joon-ho", 2019, "Thiller") #انشاء كائن الثالث من الكلاس وتخزين بيانات مختلفة عن الكائن الاول والثاني
new3_movie.profile_print()#عرض بيانات الكائن الثالث للتأكد من ان البيانات المخزنة مختلفة عن الكائن الاول والثاني

#رسالة (جاري تعديل البيانات)
print("\nChanging Movie Directors .....\n")
new1_movie.object_profile("Shokry Sarhan")#تعديل اسم المخرج في الكائن الاول
new2_movie.object_profile("Ahmed Mazhar")#تعديل اسم المخرج في الكائن الثاني
new3_movie.object_profile("Isamel Yassin")#تعديل اسم المخرج في الك  ائن الثالث  

print("Movie 1 Details:") #عرض بيانات الكائن الاول بعد التعديل للتأكد من ان التعديل تم بنجاح
new1_movie.profile_print()


print("Movie 2 Details:")#عرض بيانات الكائن الثاني بعد التعديل للتأكد من ان التعديل تم بنجاح
new2_movie.profile_print()


print("Movie 3 Details:")#عرض بيانات الكائن الثالث بعد التعديل للتأكد من ان التعديل تم بنجاح
new3_movie.profile_print()

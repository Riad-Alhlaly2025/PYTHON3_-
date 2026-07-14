# تعريف كلاس جديد باسم Book
class Book:
# دالة ينيت :تستخدم للتهيائة
# self = تستخدم لتخزين البيانات في نفس الكائن الذي استدعاء الكلاس فقط
# self / بمعنئ اخر. تقوم بربط البيانات الكائن بنفسة لا غير 
        
    def __init__(self, title, author, pages): #تحديد الدالة ينيت مع المتغيرات المطلوبة (العنوان، المؤلف، عدد الصفحات)
        self.title = title #تخزين العنوان في الكائن
        self.author = author #تخزين اسم المؤلف في الكائن
        self.pages = pages  #تخزين عدد الصفحات في الكائن
    def profile(self):
        print(f"name : {self.title}")
        print(f"auther : {self.author}")
        print(f"number : {self.pages}")
        
    def mark_as_complete(self): #تعديل البيانات المخزنة في الكائن باستخدام دالة mark_as_complete
        self.title = "Complete Book"
        self.author = "Alhlal--Y"
        self.pages = "705"
    
new_book = Book("Origin", "Dan Brown", 5354) #انشاء كائن جديد من الكلاس بوك وتخزين البيانات فيه
new_book.profile()#عرض البيانات المخزنة في الكائن الجديد
new_book.mark_as_complete() #تعديل البيانات المخزنة في الكائن الجديد باستخدام دالة mark_as_complete
new_book.profile() #عرض البيانات المخزنة في الكائن الجديد بعد التعديل للتأكد من ان التعديل تم بنجاح

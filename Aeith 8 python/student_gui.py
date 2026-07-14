# Student Information GUI System
# Python GUI Programming - Tkinter

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# ---------------- Window ----------------

root = Tk()
root.title("Student Information System")
root.geometry("500x450")
root.config(bg="#dfe6e9")

# ---------------- Functions ----------------

def submit_data():

    name = name_entry.get()
    student_id = id_entry.get()
    department = dept_combo.get()
    age = age_entry.get()

    # Validation
    if name == "" or student_id == "" or department == "" or age == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    if not age.isdigit():
        messagebox.showerror("Error", "Age must be numbers only")
        return

    # Display Result
    result_text = f"""
Student Information

Name: {name}
ID: {student_id}
Department: {department}
Age: {age}
"""

    result_label.config(text=result_text)


def clear_data():

    name_entry.delete(0, END)
    id_entry.delete(0, END)
    age_entry.delete(0, END)
    dept_combo.set("")

    result_label.config(text="")


# ---------------- Title ----------------

title_label = Label(
    root,
    text="Student Information System",
    font=("Arial", 18, "bold"),
    bg="#dfe6e9",
    fg="#2d3436"
)

title_label.pack(pady=15)

# ---------------- Name ----------------

name_label = Label(
    root,
    text="Student Name:",
    font=("Arial", 12),
    bg="#dfe6e9"
)

name_label.pack()

name_entry = Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=5)

# ---------------- Student ID ----------------

id_label = Label(
    root,
    text="Student ID:",
    font=("Arial", 12),
    bg="#dfe6e9"
)

id_label.pack()

id_entry = Entry(root, font=("Arial", 12), width=30)
id_entry.pack(pady=5)

# ---------------- Department ----------------

dept_label = Label(
    root,
    text="Department:",
    font=("Arial", 12),
    bg="#dfe6e9"
)

dept_label.pack()

dept_combo = ttk.Combobox(
    root,
    font=("Arial", 11),
    width=28,
    values=["IT", "CS", "IS", "AI", "Cyber Security"]
)

dept_combo.pack(pady=5)

# ---------------- Age ----------------

age_label = Label(
    root,
    text="Age:",
    font=("Arial", 12),
    bg="#dfe6e9"
)

age_label.pack()

age_entry = Entry(root, font=("Arial", 12), width=30)
age_entry.pack(pady=5)

# ---------------- Buttons ----------------

button_frame = Frame(root, bg="#dfe6e9")
button_frame.pack(pady=15)

submit_button = Button(
    button_frame,
    text="Submit",
    font=("Arial", 11, "bold"),
    bg="#00b894",
    fg="white",
    width=12,
    command=submit_data
)

submit_button.grid(row=0, column=0, padx=10)

clear_button = Button(
    button_frame,
    text="Clear",
    font=("Arial", 11, "bold"),
    bg="#d63031",
    fg="white",
    width=12,
    command=clear_data
)

clear_button.grid(row=0, column=1, padx=10)

# ---------------- Result Label ----------------

result_label = Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#b2bec3",
    fg="#2d3436",
    width=40,
    height=8,
    justify=LEFT,
    anchor="nw"
)

result_label.pack(pady=10)

# ---------------- Run Program ----------------

root.mainloop()









#********************************************************************************



# # #******************************************************
# from tkinter import * 
# from tkinter import ttk 
# root=Tk() 
# root.title("Data Entry") 
# root.geometry("470x340") 

# title=Label(root,text="Data Entry Form",font="Calibre 20 bold") 
# title.grid(row=0,column=0,pady=10, columnspan=4) 

# fname=Label(root,text="First name :") 
# fname.grid(row=1,column=0) 
# fnameEntry=Entry(root,width=20) 
# fnameEntry.grid(row=1,column=1) 

# Lname=Label(root,text="Last name :") 
# Lname.grid(row=1,column=2) 
# LnameEntry=Entry(root,width=20) 
# LnameEntry.grid(row=1,column=3) 

# bdate=Label(root,text="brith date :") 
# bdate.grid(row=2,column=0,sticky="w") 
# bdateEntry=Entry(root,width=20) 
# bdateEntry.grid(row=2,column=1,columnspan=3,sticky='we')


# gender=Label(root, text="Gender") 
# gender.grid(row=3,column=0,padx=10,sticky="w") 

# Gndr=StringVar() 
# Gndr.set('noun') 


# male=Radiobutton(root,text="male",variable=Gndr,value='Male') 
# male.grid(row=3,column=1,pady=5,sticky="w") 

# fmale=Radiobutton(root,text="fmale",variable=Gndr,value='Fmale') 
# fmale.grid(row=3,column=2,pady=5,sticky="w") 

# kntry=Label(root, text="Countries") 
# kntry.grid(row=4,column=0,padx=10,sticky="w") 

# country=ttk.Combobox(root, width=20,values=['hhh','kkkk','qqqqqq']) 
# country.grid(row=4,column=1) 

# txtlabel=Label(root, text='Address') 
# txtlabel.grid(row=5,column=0) 
# txtentry=Text(root,width=20,height=5) 
# txtentry.grid(row=5,column=1,pady=5,columnspan=3,sticky='we') 

# def record(): 
#     frstname=fnameEntry.get() 
#     lstname=LnameEntry.get() 
#     GG=Gndr.get() 
#     brathdate=bdateEntry.get() 
#     contry_=country.get() 
#     address=txtentry.get('1.0','end-1c') 

#     textt=frstname +"," + lstname + ',' + GG +',' + brathdate + ',' + contry_ + ',' + address +"\n" 

#     with open(r"C:\Users\mohse\Desktop\KKK\file.csv","a") as file: 
#         file.write(textt) 
#     clearall() 

# def clearall(): 
#     LnameEntry.delete(0,"end") 
#     fnameEntry.delete(0,"end") 
#     bdateEntry.delete(0,"end") 
#     Gndr.set('noun') 
#     country.delete(0,"end") 
#     txtentry.delete("1.0","end-1c") 
#     fnameEntry.focus_set() 

# b1=Button(root,text='save',command=record) 
# b1.grid(row=6,column=1) 

# b2=Button(root,text='Clear', command=clearall) 
# b2.grid(row=6,column=2) 

# root.mainloop()



















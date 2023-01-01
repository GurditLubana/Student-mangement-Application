from tkinter import *
from tkinter.ttk import Combobox

# import random
# import time
# import datetime
# from tkinter import messagebox
# # import mysql.connector

month = ('JAN','FEB','MAR','APR','MAY','JUN', 'JUL','AUG','SEP','OCT','NOV','DEC')
dates = list(range(1,32))
year = list(range(2020, 2040))

root = Tk()
root.title("Hospital Management System")
root.geometry("1540x800+0+0")
Label(root,text="HOSPITAL MANAGEMENT SYSTEM",bg = "light blue",fg="navy blue", font =("times new roman", 30,"bold")).pack(side=TOP,fill=X)
sideBar = Frame(root,bd=2,bg = "light blue", relief = RIDGE).place(x=0,y=50,width=240,height=735)

def addStudent():
	
    addStudentWindow=Tk()
    addStudentWindow.title('Add Student')
    addStudentWindow.geometry("600x600+480+100")
    addStudentWindow.resizable(False,False)
    Label(addStudentWindow,text='ENTER STUDENT DETAIL',bg = "light blue",fg="navy blue", font =("times new roman", 25,"bold")).pack(side=TOP,fill=X)
    Label(addStudentWindow,text='Personal Information',fg="navy blue", font =("times new roman", 17)).place(x=20,y=50)
    Label(addStudentWindow,text='First Name ', font=("times new roman",13)).place(x=20,y=100)
    Entry(addStudentWindow,width=13,font=("times new roman",13)).place(x=120,y=100)
    Label(addStudentWindow,text='Last Name ', font=("times new roman",13)).place(x=310,y=100)
    Entry(addStudentWindow,width=13,font=("times new roman",13)).place(x=420,y=100)
    Label(addStudentWindow,text='Date of Birth', font=("times new roman",13)).place(x=20,y=150)
    Combobox(addStudentWindow, value=dates, width = 2,height=10).place(x=20,y=180)
    Combobox(addStudentWindow, value=month, width = 5,height=10).place(x=80,y=180)
    Combobox(addStudentWindow, value=year, width = 5,height=10).place(x=150,y=180)
    
    
   
def updateStdntInfo():
	
	
	updateStudentaddStudentWindowdow = Tk()
	updateStudentaddStudentWindowdow.title("Update Student Information")
	updateStudentaddStudentWindowdow.geometry("1540x800+0+0")
	Label(updateStudentaddStudentWindowdow,text ="This is a update addStudentWindowdow").pack()

label = Label(root,text ="This is the main addStudentWindowdow")

label.pack(pady = 10)


Button(sideBar,height=2,width=30,text="Add new Student", command = addStudent).place(x=10,y=100)
Button(sideBar,height=2,width=30,text="Update Student", command = updateStdntInfo).place(x=10,y=150)

mainloop()











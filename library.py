from tkinter import *
from tkinter.ttk import Combobox

# import random
# import time
# import datetime
# from tkinter import messagebox
# # import mysql.connector

month = ('JAN','FEB','MAR','APR','MAY','JUN', 'JUL','AUG','SEP','OCT','NOV','DEC')
dates = list(range(1,32))
year = list(range(1995, 2017))

root = Tk()
root.title("Hospital Management System")
root.geometry("1540x800+0+0")
Label(root,text="HOSPITAL MANAGEMENT SYSTEM",bg = "DeepSkyBlue4",fg="white", font =("times new roman", 30,"bold")).pack(side=TOP,fill=X)
sideBar = Frame(root,bd=2,bg = "DeepSkyBlue4", relief = RIDGE).place(x=0,y=50,width=240,height=735)

def addStudent():
	
    addStudentWindow=Tk()
    addStudentWindow.title('Add Student')
    addStudentWindow.geometry("500x550+480+100")
    addStudentWindow.resizable(False,False)
    Label(addStudentWindow,text='ENTER STUDENT DETAILS',bg = "DeepSkyBlue4",fg="white", font =("times new roman", 20,"bold")).pack(side=TOP,fill=X,pady=2)
    Label(addStudentWindow,text='First Name ', font=("times new roman",13)).place(x=70,y=100)
    Entry(addStudentWindow,width=20,font=("times new roman",13)).place(x=170,y=100)
    Label(addStudentWindow,text='Last Name ', font=("times new roman",13)).place(x=70,y=140)
    Entry(addStudentWindow,width=20,font=("times new roman",13)).place(x=170,y=140)
    Label(addStudentWindow,text='Date of Birth:', font=("times new roman",13)).place(x=70,y=180)
    Label(addStudentWindow,text='Date', font=("times new roman",13)).place(x=70,y=210)
    Combobox(addStudentWindow, state="readonly",value=dates, width = 2,height=10).place(x=110,y=210)
    Label(addStudentWindow,text='Month', font=("times new roman",13)).place(x=155,y=210)
    Combobox(addStudentWindow, state="readonly",value=month, width = 5,height=10).place(x=210,y=210)
    Label(addStudentWindow,text='Year', font=("times new roman",13)).place(x=270,y=210)
    Combobox(addStudentWindow, state="readonly",value=year, width = 5,height=10).place(x=310,y=210)
    Label(addStudentWindow,text='Phone No ', font=("times new roman",13)).place(x=70,y=250)
    Entry(addStudentWindow,width=20,font=("times new roman",13)).place(x=170,y=250)
    Label(addStudentWindow,text='Email ', font=("times new roman",13)).place(x=70,y=290)
    Entry(addStudentWindow,width=20,font=("times new roman",13)).place(x=170,y=290)
    Label(addStudentWindow,text='Address ', font=("times new roman",13)).place(x=70,y=330)
    Entry(addStudentWindow,width=20,font=("times new roman",13)).place(x=170,y=330)
    Label(addStudentWindow,text='Assigned Classroom:', font=("times new roman",13)).place(x=70,y=370)
    Label(addStudentWindow,text='Grade ', font=("times new roman",13)).place(x=70,y=400)
    Combobox(addStudentWindow, state="readonly",value=list(range(1, 13)), width = 4,height=10).place(x=150,y=400)
    Label(addStudentWindow,text='Section ', font=("times new roman",13)).place(x=220,y=400)
    Combobox(addStudentWindow, state="readonly",value= ['A','B','C','D','E'], width = 4,height=10).place(x=290,y=400)
    Button(addStudentWindow,height=2,width=20,text="Save", bg="azure3", command = addStudent,cursor="hand2").place(x=100,y=450)
    Button(addStudentWindow,height=2,width=20,text="Close", bg="azure3",command = addStudentWindow.withdraw,cursor="hand2").place(x=290,y=450)
    
    
def updateStdntInfo():
    updateStdntInfoWindow = Tk()
    updateStdntInfoWindow.title('Update Student')
    updateStdntInfoWindow.geometry("1540x800+0+0")
    updateStdntInfoWindow.resizable(False,False)
    Label(updateStdntInfoWindow,text='ENTER STUDENT DETAILS',bg = "DeepSkyBlue4",fg="white", font =("times new roman", 30,"bold")).pack(side=TOP,fill=X,pady=2)
    infoFrame = LabelFrame(updateStdntInfoWindow,bd=2).place(x=5,y=70,width=800,height =700)
    StndtListFrame = LabelFrame(updateStdntInfoWindow,bd=2).place(x=850,y=70,width=650,height =700)
    Label(updateStdntInfoWindow,text='Student Number ', font=("times new roman",13)).place(x=70,y=80)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=170,y=80)
    Label(updateStdntInfoWindow,text='First Name ', font=("times new roman",13)).place(x=70,y=100)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=170,y=100)
    Label(updateStdntInfoWindow,text='Last Name ', font=("times new roman",13)).place(x=70,y=140)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=170,y=140)
    Label(updateStdntInfoWindow,text='Date of Birth:', font=("times new roman",13)).place(x=70,y=180)
    Label(updateStdntInfoWindow,text='Date', font=("times new roman",13)).place(x=70,y=210)
    Combobox(updateStdntInfoWindow, state="readonly",value=dates, width = 2,height=10).place(x=110,y=210)
    Label(updateStdntInfoWindow,text='Month', font=("times new roman",13)).place(x=155,y=210)
    Combobox(updateStdntInfoWindow, state="readonly",value=month, width = 5,height=10).place(x=210,y=210)
    Label(updateStdntInfoWindow,text='Year', font=("times new roman",13)).place(x=270,y=210)
    Combobox(updateStdntInfoWindow, state="readonly",value=year, width = 5,height=10).place(x=310,y=210)
    Label(updateStdntInfoWindow,text='Phone No ', font=("times new roman",13)).place(x=70,y=250)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=170,y=250)
    Label(updateStdntInfoWindow,text='Email ', font=("times new roman",13)).place(x=70,y=290)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=170,y=290)
    Label(updateStdntInfoWindow,text='Address ', font=("times new roman",13)).place(x=70,y=330)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=170,y=330)
    Label(updateStdntInfoWindow,text='Assigned Classroom:', font=("times new roman",13)).place(x=70,y=370)
    Label(updateStdntInfoWindow,text='Grade ', font=("times new roman",13)).place(x=70,y=400)
    Combobox(updateStdntInfoWindow, state="readonly",value=list(range(1, 13)), width = 4,height=10).place(x=150,y=400)
    Label(updateStdntInfoWindow,text='Section ', font=("times new roman",13)).place(x=220,y=400)
    Combobox(updateStdntInfoWindow, state="readonly",value= ['A','B','C','D','E'], width = 4,height=10).place(x=290,y=400)




label = Label(root,text ="This is the main addStudentWindowdow")
label.pack(pady = 10)


Button(sideBar,height=2,width=30,text="Add new Student", bg="azure3",command = addStudent,cursor="hand2").place(x=10,y=100)
Button(sideBar,height=2,width=30,text="Update Student", bg="azure3",command = updateStdntInfo,cursor="hand2").place(x=10,y=150)

mainloop()











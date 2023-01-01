from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk


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
    Label(addStudentWindow,text='First Name ', font=("times new roman",13)).place(x=70,y=60)
    Entry(addStudentWindow,width=20,font=("times new roman",13)).place(x=190,y=60)
    Label(addStudentWindow,text='Last Name ', font=("times new roman",13)).place(x=70,y=100)
    Entry(addStudentWindow,width=20,font=("times new roman",13)).place(x=190,y=100)
    Label(addStudentWindow,text='Gender ', font=("times new roman",13)).place(x=70,y=140)
    Combobox(addStudentWindow, state="readonly",value= ['MALE','FEMALE','OTHERS'], width = 8,height=10).place(x=190,y=140)
    Label(addStudentWindow,text='Date of Birth:', font=("times new roman",13)).place(x=70,y=180)
    Label(addStudentWindow,text='Date', font=("times new roman",13)).place(x=70,y=210)
    Combobox(addStudentWindow, state="readonly",value=dates, width = 2,height=10).place(x=110,y=210)
    Label(addStudentWindow,text='Month', font=("times new roman",13)).place(x=155,y=210)
    Combobox(addStudentWindow, state="readonly",value=month, width = 5,height=10).place(x=210,y=210)
    Label(addStudentWindow,text='Year', font=("times new roman",13)).place(x=270,y=210)
    Combobox(addStudentWindow, state="readonly",value=year, width = 5,height=10).place(x=310,y=210)
    Label(addStudentWindow,text='Phone No ', font=("times new roman",13)).place(x=70,y=250)
    Entry(addStudentWindow,width=20,font=("times new roman",13)).place(x=190,y=250)
    Label(addStudentWindow,text='Email ', font=("times new roman",13)).place(x=70,y=290)
    Entry(addStudentWindow,width=20,font=("times new roman",13)).place(x=190,y=290)
    Label(addStudentWindow,text='Address ', font=("times new roman",13)).place(x=70,y=330)
    Entry(addStudentWindow,width=20,font=("times new roman",13)).place(x=190,y=330)
    Label(addStudentWindow,text='Assigned Classroom:', font=("times new roman",13)).place(x=70,y=370)
    Label(addStudentWindow,text='Grade ', font=("times new roman",13)).place(x=70,y=400)
    Combobox(addStudentWindow, state="readonly",value=list(range(1, 13)), width = 4,height=10).place(x=150,y=400)
    Label(addStudentWindow,text='Section ', font=("times new roman",13)).place(x=220,y=400)
    Combobox(addStudentWindow, state="readonly",value= ['A','B','C','D','E'], width = 4,height=10).place(x=290,y=400)
    Button(addStudentWindow,height=1,width=20,text="Save", activebackground = "navy blue", activeforeground = "white",bg="azure3", command = addStudent,cursor="hand2").place(x=100,y=450)
    Button(addStudentWindow,height=1,width=20,text="Close", activebackground = "navy blue", activeforeground = "white", bg="azure3",command = addStudentWindow.withdraw,cursor="hand2").place(x=290,y=450)
    
    
def updateStdntInfo():
    
    updateStdntInfoWindow = Toplevel(root)
    updateStdntInfoWindow.title('Update Student')
    updateStdntInfoWindow.geometry("1340x700+100+45")
    updateStdntInfoWindow.resizable(False,False)
    Label(updateStdntInfoWindow,text='UPDATE STUDENT DETAILS',bg = "DeepSkyBlue4",fg="white", font =("times new roman", 30,"bold")).pack(side=TOP,fill=X,pady=2)
    infoFrame = LabelFrame(updateStdntInfoWindow,bd=2).place(x=20,y=70,width=700,height =500)
    StndtListFrame = LabelFrame(updateStdntInfoWindow,bd=2).place(x=750,y=70,width=550,height =500)
    Label(updateStdntInfoWindow,text='Student Number ', font=("times new roman",13)).place(x=70,y=90)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=190,y=90)
    Label(updateStdntInfoWindow,text='First Name ', font=("times new roman",13)).place(x=70,y=130)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=190,y=130)
    Label(updateStdntInfoWindow,text='Last Name ', font=("times new roman",13)).place(x=70,y=170)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=190,y=170)
    Label(updateStdntInfoWindow,text='Gender ', font=("times new roman",13)).place(x=70,y=210)
    Combobox(updateStdntInfoWindow, state="readonly",value= ['MALE','FEMALE','OTHERS'], width = 8,height=10).place(x=190,y=210)
    Label(updateStdntInfoWindow,text='Date of Birth:', font=("times new roman",13)).place(x=70,y=250)
    Label(updateStdntInfoWindow,text='Date', font=("times new roman",13)).place(x=70,y=280)
    Combobox(updateStdntInfoWindow, state="readonly",value=dates, width = 2,height=10).place(x=110,y=280)
    Label(updateStdntInfoWindow,text='Month', font=("times new roman",13)).place(x=155,y=280)
    Combobox(updateStdntInfoWindow, state="readonly",value=month, width = 5,height=10).place(x=210,y=280)
    Label(updateStdntInfoWindow,text='Year', font=("times new roman",13)).place(x=270,y=280)
    Combobox(updateStdntInfoWindow, state="readonly",value=year, width = 5,height=10).place(x=310,y=280)
    Label(updateStdntInfoWindow,text='Phone No ', font=("times new roman",13)).place(x=70,y=320)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=190,y=320)
    Label(updateStdntInfoWindow,text='Email ', font=("times new roman",13)).place(x=70,y=360)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=190,y=360)
    Label(updateStdntInfoWindow,text='Address ', font=("times new roman",13)).place(x=70,y=400)
    Entry(updateStdntInfoWindow,width=20,font=("times new roman",13)).place(x=190,y=400)
    Label(updateStdntInfoWindow,text='Assigned Classroom:', font=("times new roman",13)).place(x=70,y=440)
    Label(updateStdntInfoWindow,text='Grade ', font=("times new roman",13)).place(x=70,y=470)
    Combobox(updateStdntInfoWindow, state="readonly",value=list(range(1, 13)), width = 4,height=10).place(x=150,y=470)
    Label(updateStdntInfoWindow,text='Section ', font=("times new roman",13)).place(x=220,y=470)
    Combobox(updateStdntInfoWindow, state="readonly",value= ['A','B','C','D','E'], width = 4,height=10).place(x=290,y=470)
    Button(updateStdntInfoWindow,height=1,width=20,font=("times new roman",13), text="Update", activebackground = "navy blue", activeforeground = "white",bg="azure3", command = addStudent,cursor="hand2").place(x=460,y=600)
    Button(updateStdntInfoWindow,height=1,width=20,font=("times new roman",13), text="Close", activebackground = "navy blue", activeforeground = "white", bg="azure3",command = updateStdntInfoWindow.withdraw,cursor="hand2").place(x=680,y=600)
    

    Frame(updateStdntInfoWindow,bg="lightgray", bd=1,relief=GROOVE).place(x=750,y=70,width=550,height =45)
    Label(updateStdntInfoWindow,text="Search",bg="lightgray", font=("times new roman",13)).place(x=770,y=80)
    Combobox(updateStdntInfoWindow, state="readonly",value=['Name','Student No','Phone No','Email'], width = 12,height=10).place(x=830,y=80)
    Button(updateStdntInfoWindow,height=1,text="Search").place(x=940,y=80)
    Button(updateStdntInfoWindow,height=1,text="Show all").place(x=1000,y=80)

    scrollBar = Scrollbar(StndtListFrame,orient=VERTICAL)
    
label = Label(root,text ="This is the main addStudentWindowdow")
label.pack(pady = 10)


Button(sideBar,height=2,width=30,text="Add new Student", activeforeground = "white", bg="azure3",command = addStudent,cursor="hand2").place(x=10,y=100)
Button(sideBar,height=2,width=30,text="Update Student", bg="azure3",activeforeground = "white",command = updateStdntInfo,cursor="hand2").place(x=10,y=150)

mainloop()











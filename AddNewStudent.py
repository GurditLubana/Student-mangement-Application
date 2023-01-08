from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk,messagebox
import random
from UpdateStudentInfo import UpdateStudentInfo
import mysql.connector


month = ('JAN','FEB','MAR','APR','MAY','JUN', 'JUL','AUG','SEP','OCT','NOV','DEC')
dates = list(range(1,32))
year = list(range(1995, 2017))


class AddNewStudent:
    def __init__(self, root):
        self.root = root
        self.root.title('Add Student')
        self.root.geometry("500x590+480+100")
        self.root.resizable(False,False)

        self.studentNo = StringVar()
        x=random.randint(1000,9999)

        self.studentNo.set("788"+str(x))
        self.firstName=StringVar()
        self.lastName=StringVar()
        self.gender=StringVar()
        self.date=StringVar()
        self.month=StringVar()
        self.year=StringVar()
        self.phone=StringVar()
        self.email=StringVar()
        self.address=StringVar()
        self.grade=StringVar()
        self.section=StringVar()

        Label(root,text='ENTER STUDENT DETAILS',bg = "DeepSkyBlue4",fg="white", font =("times new roman", 20,"bold")).place(x=0,y=0,width=500,height=50)
        Label(root,text='Student Number  ', font=("times new roman",13)).place(x=70,y=90)
        ttk.Entry(root,width=19,textvariable=self.studentNo,state='readonly',font=("times new roman",13)).place(x=200,y=90)
        Label(root,text='First Name ', font=("times new roman",13)).place(x=70,y=130)
        ttk.Entry(root,width=20,textvariable=self.firstName,font=("times new roman",13)).place(x=190,y=130)
        Label(root,text='Last Name ', font=("times new roman",13)).place(x=70,y=170)
        ttk.Entry(root,width=20,textvariable=self.lastName,font=("times new roman",13)).place(x=190,y=170)
        Label(root,text='Gender ', font=("times new roman",13)).place(x=70,y=210)
        genderCombobox = Combobox(root, state="readonly",value= ['MALE','FEMALE','OTHERS'],font=("times new roman",13), textvariable=self.gender,width = 8,height=10)
        genderCombobox.place(x=190,y=210)
        genderCombobox.current(0)
        Label(root,text='Date of Birth:', font=("times new roman",13)).place(x=70,y=250)
        Label(root,text='Date', font=("times new roman",13)).place(x=70,y=280)
        dateCombobox=Combobox(root, state="readonly",value=dates,font=("times new roman",13), textvariable=self.date,width = 2,height=10)
        dateCombobox.place(x=110,y=280)
        dateCombobox.current(0)
        Label(root,text='Month', font=("times new roman",13)).place(x=155,y=280)
        monthCombobox=Combobox(root, state="readonly",value=month,font=("times new roman",13), textvariable=self.month,width = 4,height=10)
        monthCombobox.place(x=210,y=280)
        monthCombobox.current(0)
        Label(root,text='Year', font=("times new roman",13)).place(x=270,y=280)
        yearCombobox=Combobox(root, state="readonly",value=year,font=("times new roman",13), textvariable=self.year,width = 5,height=10)
        yearCombobox.place(x=310,y=280)
        yearCombobox.current(0)
        Label(root,text='Phone No ', font=("times new roman",13)).place(x=70,y=320)
        ttk.Entry(root,textvariable=self.phone,width=20,font=("times new roman",13)).place(x=190,y=320)
        Label(root,text='Email ', font=("times new roman",13)).place(x=70,y=360)
        ttk.Entry(root,width=20,textvariable=self.email,font=("times new roman",13)).place(x=190,y=360)
        Label(root,text='Address ', font=("times new roman",13)).place(x=70,y=400)
        Entry(root,width=20,textvariable=self.address,font=("times new roman",13)).place(x=190,y=400,height=35)
        Label(root,text='Assigned Classroom:', font=("times new roman",13)).place(x=70,y=440)
        Label(root,text='Grade ', font=("times new roman",13)).place(x=70,y=470)
        gradeCombobox=Combobox(root, state="readonly",value=list(range(1, 13)), textvariable=self.grade,width = 4,height=10,font=("times new roman",13))
        gradeCombobox.place(x=150,y=470)
        gradeCombobox.current(0)
        Label(root,text='Section ', font=("times new roman",13)).place(x=220,y=470)
        sectionCombo=ttk.Combobox(root, state="readonly",value= ['A','B','C','D','E'], textvariable=self.section,width = 4,height=10)
        sectionCombo.place(x=290,y=470)
        sectionCombo.current(0)
        Button(root,height=1,width=20,text="Save", activebackground = "navy blue", activeforeground = "white",bg="azure3",command=self.addStudentToDb, cursor="hand2").place(x=100,y=530)
        Button(root,height=1,width=20,text="Close", activebackground = "navy blue", activeforeground = "white", bg="azure3",command = root.withdraw,cursor="hand2").place(x=290,y=530)

    def addStudentToDb(self):
        if(self.validateInput()!=True):
            messagebox.showerror('Error','All fields are required', parent=self.root)
            
        else:
            try:
                databaseConnection=mysql.connector.connect(host='localhost',username="root",password='9878059867gG@',database='student_list')
                myCursor = databaseConnection.cursor()
                formattedDOB = self.date.get() + " " + self.month.get()+" "+self.year.get()
                formattedClassroom = self.grade.get() + " " + self.section.get()
                myCursor.execute("INSERT INTO student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                        self.studentNo.get(),
                                                        self.firstName.get(),
                                                        self.lastName.get(),
                                                        self.gender.get(),
                                                        formattedClassroom,
                                                        self.phone.get(),
                                                        self.email.get(),
                                                        formattedDOB,
                                                        self.address.get()
                ))
                messagebox.showinfo("SUCCESS","New student added.")
                databaseConnection.commit()
                studentTable = UpdateStudentInfo(self.root)
                studentTable.showStudentList()
                databaseConnection.close()
                self.root.withdraw()
            except Exception as e:
                messagebox.showwarning("Warning","Something went wrong! ")
                print(e)

    def validateInput(self):
        if(self.firstName.get() == "" or self.lastName.get() == "" or self.phone.get() == "" or self.email.get() == "" or self.address.get() == "" ):
            return False
        else:
            return True;  


if __name__ == "__main__":
        root = Tk()
        testObj = AddNewStudent(root)
        root.mainloop()

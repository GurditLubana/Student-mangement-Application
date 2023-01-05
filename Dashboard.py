from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from AddNewStudent import AddNewStudent
from UpdateStudentInfo import UpdateStudentInfo



class Dashboard:
    def __init__(self, root):
        self.root = root
        root.title("Student Management System")
        root.geometry("1540x800+0+0")
        Label(root,text="STUDENT MANAGEMENT SYSTEM",bg = "DeepSkyBlue4",fg="white", font =("times new roman", 30,"bold")).place(x=0,y=0,width=1540,height=50)
        sideBar = Frame(root,bg = "DeepSkyBlue4", relief = RIDGE).place(x=0,y=50,width=240,height=750)
        
        Button(sideBar,height=2,width=30,text="Add new Student", activeforeground = "white", bg="azure3",command = self.addStudent,cursor="hand2").place(x=10,y=100)
        Button(sideBar,height=2,width=30,text="Update Student", bg="azure3",activeforeground = "white",command = self.updateStdntInfo,cursor="hand2").place(x=10,y=150)
        

    def addStudent(self):
        self.addStudentWindow = Toplevel(self.root)
        self.app=AddNewStudent(self.addStudentWindow)

    def updateStdntInfo(self):
        self.updateStdntInfoWindow = Toplevel(self.root)
        self.newWindow=UpdateStudentInfo(self.updateStdntInfoWindow)

if __name__ == "__main__":
        root = Tk()
        testObj = Dashboard(root)
        root.mainloop()









from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk


month = ('JAN','FEB','MAR','APR','MAY','JUN', 'JUL','AUG','SEP','OCT','NOV','DEC')
dates = list(range(1,32))
year = list(range(1995, 2017))


class AddNewStudent:
    def __init__(self, root):
        self.root = root
        root.title('Add Student')
        root.geometry("500x550+480+100")
        root.resizable(False,False)
        Label(root,text='ENTER STUDENT DETAILS',bg = "DeepSkyBlue4",fg="white", font =("times new roman", 20,"bold")).pack(side=TOP,fill=X,pady=2)
        Label(root,text='First Name ', font=("times new roman",13)).place(x=70,y=60)
        Entry(root,width=20,font=("times new roman",13)).place(x=190,y=60)
        Label(root,text='Last Name ', font=("times new roman",13)).place(x=70,y=100)
        Entry(root,width=20,font=("times new roman",13)).place(x=190,y=100)
        Label(root,text='Gender ', font=("times new roman",13)).place(x=70,y=140)
        Combobox(root, state="readonly",value= ['MALE','FEMALE','OTHERS'], width = 8,height=10).place(x=190,y=140)
        Label(root,text='Date of Birth:', font=("times new roman",13)).place(x=70,y=180)
        Label(root,text='Date', font=("times new roman",13)).place(x=70,y=210)
        Combobox(root, state="readonly",value=dates, width = 2,height=10).place(x=110,y=210)
        Label(root,text='Month', font=("times new roman",13)).place(x=155,y=210)
        Combobox(root, state="readonly",value=month, width = 5,height=10).place(x=210,y=210)
        Label(root,text='Year', font=("times new roman",13)).place(x=270,y=210)
        Combobox(root, state="readonly",value=year, width = 5,height=10).place(x=310,y=210)
        Label(root,text='Phone No ', font=("times new roman",13)).place(x=70,y=250)
        Entry(root,width=20,font=("times new roman",13)).place(x=190,y=250)
        Label(root,text='Email ', font=("times new roman",13)).place(x=70,y=290)
        Entry(root,width=20,font=("times new roman",13)).place(x=190,y=290)
        Label(root,text='Address ', font=("times new roman",13)).place(x=70,y=330)
        Entry(root,width=20,font=("times new roman",13)).place(x=190,y=330)
        Label(root,text='Assigned Classroom:', font=("times new roman",13)).place(x=70,y=370)
        Label(root,text='Grade ', font=("times new roman",13)).place(x=70,y=400)
        Combobox(root, state="readonly",value=list(range(1, 13)), width = 4,height=10).place(x=150,y=400)
        Label(root,text='Section ', font=("times new roman",13)).place(x=220,y=400)
        Combobox(root, state="readonly",value= ['A','B','C','D','E'], width = 4,height=10).place(x=290,y=400)
        Button(root,height=1,width=20,text="Save", activebackground = "navy blue", activeforeground = "white",bg="azure3",cursor="hand2").place(x=100,y=450)
        Button(root,height=1,width=20,text="Close", activebackground = "navy blue", activeforeground = "white", bg="azure3",command = root.withdraw,cursor="hand2").place(x=290,y=450)
        root.mainloop()
if __name__ == "__main__":
        root = Tk()
        testObj = AddNewStudent(root)
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk


month = ('JAN','FEB','MAR','APR','MAY','JUN', 'JUL','AUG','SEP','OCT','NOV','DEC')
dates = list(range(1,32))
year = list(range(1995, 2017))


class UpdateStudentInfo:
    def __init__(self, root):
        self.root = root
        root.title('Update Student')
        root.geometry("1340x700+100+45")
        root.resizable(False,False)
        Label(root,text='UPDATE STUDENT DETAILS',bg = "DeepSkyBlue4",fg="white", font =("times new roman", 30,"bold")).pack(side=TOP,fill=X,pady=2)
        infoFrame = LabelFrame(root,bd=2).place(x=20,y=70,width=700,height =500)
        StndtListFrame = LabelFrame(root,bd=2).place(x=750,y=70,width=550,height =500)
        Label(root,text='Student Number ', font=("times new roman",13)).place(x=70,y=90)
        Entry(root,width=20,font=("times new roman",13)).place(x=190,y=90)
        Label(root,text='First Name ', font=("times new roman",13)).place(x=70,y=130)
        Entry(root,width=20,font=("times new roman",13)).place(x=190,y=130)
        Label(root,text='Last Name ', font=("times new roman",13)).place(x=70,y=170)
        Entry(root,width=20,font=("times new roman",13)).place(x=190,y=170)
        Label(root,text='Gender ', font=("times new roman",13)).place(x=70,y=210)
        Combobox(root, state="readonly",value= ['MALE','FEMALE','OTHERS'], width = 8,height=10).place(x=190,y=210)
        Label(root,text='Date of Birth:', font=("times new roman",13)).place(x=70,y=250)
        Label(root,text='Date', font=("times new roman",13)).place(x=70,y=280)
        Combobox(root, state="readonly",value=dates, width = 2,height=10).place(x=110,y=280)
        Label(root,text='Month', font=("times new roman",13)).place(x=155,y=280)
        Combobox(root, state="readonly",value=month, width = 5,height=10).place(x=210,y=280)
        Label(root,text='Year', font=("times new roman",13)).place(x=270,y=280)
        Combobox(root, state="readonly",value=year, width = 5,height=10).place(x=310,y=280)
        Label(root,text='Phone No ', font=("times new roman",13)).place(x=70,y=320)
        Entry(root,width=20,font=("times new roman",13)).place(x=190,y=320)
        Label(root,text='Email ', font=("times new roman",13)).place(x=70,y=360)
        Entry(root,width=20,font=("times new roman",13)).place(x=190,y=360)
        Label(root,text='Address ', font=("times new roman",13)).place(x=70,y=400)
        Entry(root,width=20,font=("times new roman",13)).place(x=190,y=400)
        Label(root,text='Assigned Classroom:', font=("times new roman",13)).place(x=70,y=440)
        Label(root,text='Grade ', font=("times new roman",13)).place(x=70,y=470)
        Combobox(root, state="readonly",value=list(range(1, 13)), width = 4,height=10).place(x=150,y=470)
        Label(root,text='Section ', font=("times new roman",13)).place(x=220,y=470)
        Combobox(root, state="readonly",value= ['A','B','C','D','E'], width = 4,height=10).place(x=290,y=470)
        Button(root,height=1,width=20,font=("times new roman",13), text="Update", activebackground = "navy blue", activeforeground = "white",bg="azure3", cursor="hand2").place(x=460,y=600)
        Button(root,height=1,width=20,font=("times new roman",13), text="Close", activebackground = "navy blue", activeforeground = "white", bg="azure3",command = root.withdraw,cursor="hand2").place(x=680,y=600)
    

        Frame(root,bg="lightgray", bd=1,relief=GROOVE).place(x=750,y=70,width=550,height =45)
        Label(root,text="Search",bg="lightgray", font=("times new roman",13)).place(x=770,y=80)
        Combobox(root, state="readonly",value=['Name','Student No','Phone No','Email'], width = 12,height=10).place(x=830,y=80)
        Button(root,height=1,text="Search").place(x=940,y=80)
        Button(root,height=1,text="Show all").place(x=1000,y=80)

        scrollBar = Scrollbar(StndtListFrame,orient=VERTICAL)
        root.mainloop()

if __name__ == "__main__":
        root = Tk()
        testObj = UpdateStudentInfo(root)
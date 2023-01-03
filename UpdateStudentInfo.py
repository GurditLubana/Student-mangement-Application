from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
import mysql.connector
import random

month = ('JAN','FEB','MAR','APR','MAY','JUN', 'JUL','AUG','SEP','OCT','NOV','DEC')
dates = list(range(1,32))
year = list(range(1995, 2017))


class UpdateStudentInfo:
    def __init__(self, root):
        self.root = root
        self.root.title('Update Information')
        self.root.geometry("1340x700+100+45")
        # self.root.resizable(False,False)

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
        

        
        lblTitle = Label(self.root,text='UPDATE STUDENT DETAILS',bg = "DeepSkyBlue4",fg="white", font =("times new roman", 30,"bold"))
        lblTitle.place(x=0,y=0,width=1340,height=50)
        
        infoFrame = Frame(self.root,bd=4, relief=GROOVE)
        infoFrame.place(x=20,y=70,width=400,height =500)
        

        Label(root,text='Student Number ', font=("times new roman",13)).place(x=70,y=90)
        ttk.Entry(root,width=20,textvariable=self.studentNo,state='readonly',font=("times new roman",13)).place(x=190,y=90)
        Label(root,text='First Name ', font=("times new roman",13)).place(x=70,y=130)
        ttk.Entry(root,width=20,textvariable=self.firstName,font=("times new roman",13)).place(x=190,y=130)
        Label(root,text='Last Name ', font=("times new roman",13)).place(x=70,y=170)
        ttk.Entry(root,width=20,textvariable=self.lastName,font=("times new roman",13)).place(x=190,y=170)
        Label(root,text='Gender ', font=("times new roman",13)).place(x=70,y=210)
        Combobox(root, state="readonly",value= ['MALE','FEMALE','OTHERS'],font=("times new roman",13), textvariable=self.gender,width = 8,height=10).place(x=190,y=210)
        Label(root,text='Date of Birth:', font=("times new roman",13)).place(x=70,y=250)
        Label(root,text='Date', font=("times new roman",13)).place(x=70,y=280)
        Combobox(root, state="readonly",value=dates,font=("times new roman",13), textvariable=self.date,width = 2,height=10).place(x=110,y=280)
        Label(root,text='Month', font=("times new roman",13)).place(x=155,y=280)
        Combobox(root, state="readonly",value=month,font=("times new roman",13), textvariable=self.month,width = 4,height=10).place(x=210,y=280)
        Label(root,text='Year', font=("times new roman",13)).place(x=270,y=280)
        Combobox(root, state="readonly",value=year,font=("times new roman",13), textvariable=self.year,width = 5,height=10).place(x=310,y=280)
        Label(root,text='Phone No ', font=("times new roman",13)).place(x=70,y=320)
        ttk.Entry(root,textvariable=self.phone,width=20,font=("times new roman",13)).place(x=190,y=320)
        Label(root,text='Email ', font=("times new roman",13)).place(x=70,y=360)
        ttk.Entry(root,width=20,textvariable=self.email,font=("times new roman",13)).place(x=190,y=360)
        Label(root,text='Address ', font=("times new roman",13)).place(x=70,y=400)
        Entry(root,width=20,textvariable=self.address,font=("times new roman",13)).place(x=190,y=400,height=35)
        Label(root,text='Assigned Classroom:', font=("times new roman",13)).place(x=70,y=440)
        Label(root,text='Grade ', font=("times new roman",13)).place(x=70,y=470)
        Combobox(root, state="readonly",value=list(range(1, 13)), textvariable=self.grade,width = 4,height=10,font=("times new roman",13)).place(x=150,y=470)
        Label(root,text='Section ', font=("times new roman",13)).place(x=220,y=470)
        sectionCombo=ttk.Combobox(root, state="readonly",value= ['A','B','C','D','E'], textvariable=self.section,width = 4,height=10)
        sectionCombo.place(x=290,y=470)
        sectionCombo.current(0)
        Button(root,height=1,width=20,font=("times new roman",13), text="Update", activebackground = "navy blue", activeforeground = "white",bg="azure3", cursor="hand2").place(x=460,y=600)
        Button(root,height=1,width=20,font=("times new roman",13), text="Close", activebackground = "navy blue", activeforeground = "white", bg="azure3",command = root.withdraw,cursor="hand2").place(x=680,y=600)

        stdntListFrame = Frame(self.root,bd=4, relief=GROOVE)
        stdntListFrame.place(x=450,y=70,width=875,height =500)

        searchLabel= Label(stdntListFrame,text='Search By', font=("times new roman",13))
        searchLabel.grid(row=0,column=0,sticky=W)
        searchByCombo=ttk.Combobox(stdntListFrame, state="readonly",value= ['Student Number','First Name','Last Name','Gender','Classroom','Phone Number','Email','DOB'], width = 14,height=10,font=("times new roman",13))
        searchByCombo.grid(row=0,column=1,padx=4,pady=4)
        searchByCombo.current(0)
        searchEntry= ttk.Entry(stdntListFrame,width=20,font=("times new roman",13))
        searchEntry.grid(row=0,column=2,padx=4,pady=4)
        searchButton = Button(stdntListFrame,height=1,text="Search",font=("times new roman",11), activebackground = "navy blue", activeforeground = "white",bg="azure3", cursor="hand2")
        searchButton.grid(row=0,column=3,padx=4,pady=4)

        showAllButton = Button(stdntListFrame,height=1,text="Show All",font=("times new roman",11), activebackground = "navy blue", activeforeground = "white",bg="azure3", cursor="hand2")
        showAllButton.grid(row=0,column=4,padx=4,pady=4)

        listFrame = Frame(stdntListFrame,bd=4,relief=GROOVE)
        listFrame.place(x=10,y=50,width=850,height=435)

        scrollx= ttk.Scrollbar(listFrame,orient=HORIZONTAL)
        scrolly= ttk.Scrollbar(listFrame,orient=VERTICAL)

        self.studentsList = ttk.Treeview(listFrame,column=('stdnum','fname','lname','classroom','phone','gender','email','dob'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.studentsList.xview)
        scrolly.config(command=self.studentsList.yview)

        self.studentsList.heading('stdnum',text='Student No')
        self.studentsList.heading('fname',text='First Name')
        self.studentsList.heading('lname',text='Last Name')
        self.studentsList.heading('gender',text='Gender')
        self.studentsList.heading('classroom',text='Classroom')
        self.studentsList.heading('phone',text='Phone No')
        self.studentsList.heading('email',text='Email')
        self.studentsList.heading('dob',text='DOB')

        self.studentsList.column('stdnum',width=100)
        self.studentsList.column('fname',width=100)
        self.studentsList.column('lname',width=100)
        self.studentsList.column('gender',width=60)
        self.studentsList.column('classroom',width=60)
        self.studentsList.column('phone',width=100)
        self.studentsList.column('email',width=100)
        self.studentsList.column('dob',width=100)
       



        self.studentsList['show'] = 'headings'
        self.studentsList.pack(fill=BOTH,expand=True)

        # stdntNo = Label(infoFrame,font=("times new roman",13),text='Student Number',padx=4,pady=6)
        # stdntNo.grid(row=0,column=0,sticky=W,padx=4)
        # entry = ttk.ttk.Entry(infoFrame)
        # entry.grid(row=0,column=1)

        # stdntNo2 = Label(infoFrame,font=("times new roman",13),text='First Name',padx=4,pady=6)
        # stdntNo2.grid(row=1,column=0,sticky=W)
        # entry2 = ttk.ttk.Entry(infoFrame)
        # entry2.grid(row=1,column=1)
        
        # stdntNo3=Label(infoFrame,text='Last Name', font=("times new roman",13),padx=4,pady=6)
        # stdntNo3.grid(row=2,column=0,sticky=W) 
        # stdntNoEntry=ttk.ttk.Entry(infoFrame)
        # stdntNoEntry.grid(row=2,column=1)

        # gender=Label(infoFrame,text='Gender ', font=("times new roman",13),padx=4,pady=6)
        # gender.grid(row=3,column=0,sticky=W)
        # genderEntry=Combobox(infoFrame, state="readonly",value= ['MALE','FEMALE','OTHERS'], width = 8,height=10)
        # genderEntry.grid(row=3,column=1)

        # dob=Label(infoFrame,text='Date of Birth: ', font=("times new roman",13),padx=4,pady=6)
        # dob.grid(row=4,column=0,sticky=W) 

        # date=Label(infoFrame,text='Date', font=("times new roman",13),padx=2,pady=6)
        # date.grid(row=5,column=0,sticky=W)
        # dateEntry=Combobox(infoFrame, state="readonly",value=dates, width = 2,height=10)
        # dateEntry.grid(row=5,column=0)
        
        # monthLabel=Label(infoFrame,text='Month', font=("times new roman",13),padx=2,pady=6)
        # monthLabel.grid(row=5,column=1,sticky=W,padx=4)
        # monthEntry=Combobox(infoFrame, state="readonly",value=month, width = 5,height=10)
        # monthEntry.grid(row=5,column=1,padx=4)
        # lastName=Label(infoFrame,text='Last Name ', font=("times new roman",13),padx=2,pady=6)
        # lastNameEntry=ttk.ttk.Entry(infoFrame,width=20,font=("times new roman",13))
        # 
        # 
        # dob=Label(infoFrame,text='Date of Birth:', font=("times new roman",13),padx=2,pady=6)
        # date=Label(infoFrame,text='Date', font=("times new roman",13),padx=2,pady=6)
        # dateEntry=Combobox(infoFrame, state="readonly",value=dates, width = 2,height=10)
        # monthLabel=Label(infoFrame,text='Month', font=("times new roman",13),padx=2,pady=6)
        # monthEntry=Combobox(infoFrame, state="readonly",value=month, width = 5,height=10)
        # yearLabel=Label(infoFrame,text='Year', font=("times new roman",13),padx=2,pady=6)
        # yearEntry=Combobox(infoFrame, state="readonly",value=year, width = 5,height=10)
        # phone=Label(infoFrame,text='Phone No ', font=("times new roman",13),padx=2,pady=6)
        # phoneEntry=ttk.ttk.Entry(infoFrame,width=20,font=("times new roman",13))
        # email=Label(infoFrame,text='Email ', font=("times new roman",13),padx=2,pady=6)
        # emailEntry=ttk.ttk.Entry(infoFrame,width=20,font=("times new roman",13))
        # address=Label(infoFrame,text='Address ', font=("times new roman",13),padx=2,pady=6)
        # addressEntry=ttk.Text(infoFrame,width=20,font=("times new roman",13))
        # assigned=Label(infoFrame,text='Assigned Classroom:', font=("times new roman",13),padx=2,pady=6)
        # grade=Label(infoFrame,text='Grade ', font=("times new roman",13),padx=2,pady=6)
        # gradeEntry=Combobox(infoFrame, state="readonly",value=list(range(1, 13)), width = 4,height=10)
        # section=Label(infoFrame,text='Section ', font=("times new roman",13),padx=2,pady=6)
        # sectionEntry=Combobox(infoFrame, state="readonly",value= ['A','B','C','D','E'], width = 4,height=10)
        # update=Button(infoFrame,height=1,width=20,font=("times new roman",13), text="Update", activebackground = "navy blue", activeforeground = "white",bg="azure3", cursor="hand2")
        # close=Button(infoFrame,height=1,width=20,font=("times new roman",13), text="Close", activebackground = "navy blue", activeforeground = "white", bg="azure3",command = root.withdraw,cursor="hand2")
    
        
        

        
        

        # lastName.grid(row=2,column=0,sticky=W)
        # lastNameEntry.grid(rows=2,column=1)

        # gender.grid(row=3,column=0,sticky=W)
        # genderEntry.grid(rows=3,column=1)

        # dob.grid(row=4,column=0,sticky=W)

        # date.grid(row=5,column=0,sticky=W)
        # dateEntry.grid(rows=5,column=1)

        # monthLabel.grid(row=7,column=0,sticky=W)
        # monthEntry.grid(rows=7,column=1)

        # yearLabel.grid(row=8,column=0,sticky=W)
        # yearEntry.grid(rows=8,column=1)

        # phone.grid(row=9,column=0,sticky=W)
        # phoneEntry.grid(rows=9,column=1)

        # email.grid(row=10,column=0,sticky=W)
        # emailEntry.grid(rows=10,column=1)

        # address.grid(row=11,column=0,sticky=W)
        # addressEntry.grid(rows=11,column=1)

        # assigned.grid(row=12,column=0,sticky=W)

        # grade.grid(row=13,column=0,sticky=W)
        # gradeEntry.grid(rows=13,column=1)

        # section.grid(row=14,column=0,sticky=W)
        # sectionEntry.grid(rows=14,column=1)

        
        
        
        
       
        
        
        
        
        
        
    
        
        
        # update
        # close



        # Frame(stdntListFrame,bg="lightgray", bd=1,relief=GROOVE)
        # Label(stdntListFrame,text="Search",bg="lightgray", font=("times new roman",13),padx=2,pady=6)
        # Combobox(stdntListFrame, state="readonly",value=['Name','Student No','Phone No','Email'], width = 12,height=10)
        # Button(stdntListFrame,height=1,text="Search")
        # Button(stdntListFrame,height=1,text="Show all")

        # listFrame = Frame(stdntListFrame,bg="red",bd=1,relief=GROOVE).pack(fill=BOTH,expand=True)



        

if __name__ == "__main__":
        root = Tk()
        testObj = UpdateStudentInfo(root)
        root.mainloop()
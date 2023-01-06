from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk,messagebox
from tkinter.messagebox import askyesno
from AddNewStudent import AddNewStudent
from UpdateStudentInfo import UpdateStudentInfo
import mysql.connector




class Dashboard:
    def __init__(self, root):
        self.root = root
        root.title("Student Management System")
        root.geometry("1540x800+0+0")

        self.studentNo = StringVar()
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
       

#===========================================================================Header====================================================================================================================
        Label(root,text="STUDENT MANAGEMENT SYSTEM",bg = "DeepSkyBlue4",fg="white", font =("times new roman", 30,"bold")).place(x=0,y=0,width=1540,height=50)
        sideBar = Frame(root,bg = "DeepSkyBlue4", relief = RIDGE).place(x=0,y=50,width=240,height=750)
 
 #========================================================================== Side Nav Bar ============================================================================================================       
       
        Button(sideBar,height=2,width=20,text="Add new Student", activeforeground = "white", font =("times new roman", 14), bg="azure3",command = self.addStudent,cursor="hand2").place(x=10,y=100)
        Button(sideBar,height=2,width=20,text="Update Student", bg="azure3", font =("times new roman", 14),activeforeground = "white",command = self.updateStdntInfo,cursor="hand2").place(x=10,y=170)
        
#===========================================================================Student List ==============================================================================================================

        stdntListFrame = Frame(self.root)
        stdntListFrame.place(x=260,y=70,width=900,height =600)

        searchLabel= Label(stdntListFrame,text='Search By', font=("times new roman",13))
        searchLabel.grid(row=0,column=0,sticky=W)
        searchByCombo=ttk.Combobox(stdntListFrame, state="readonly",value= ['Student Number','First Name','Last Name','Gender','Classroom','Phone Number','Email','DOB'], width = 14,height=10,font=("times new roman",13))
        searchByCombo.grid(row=0,column=1,padx=4,pady=4)
        searchByCombo.current(0)
        searchEntry= ttk.Entry(stdntListFrame,width=20,font=("times new roman",13))
        searchEntry.grid(row=0,column=2,padx=4,pady=4)
        searchButton = Button(stdntListFrame,height=1,text="Search",font=("times new roman",11), activebackground = "navy blue", activeforeground = "white",bg="azure3", cursor="hand2")
        searchButton.grid(row=0,column=3,padx=4,pady=4)

        
        refreshButton = Button(stdntListFrame, text="Refresh List",font=("times new roman",11),borderwidth=1, activebackground = "navy blue", command=self.refreshList,activeforeground = "white",bg="azure3", cursor="hand2")
        refreshButton.grid(row=0,column=5,padx=4,pady=4)
        

        showAllButton = Button(stdntListFrame,height=1,text="Show All",font=("times new roman",11), borderwidth=1,activebackground = "navy blue", activeforeground = "white",bg="azure3", cursor="hand2")
        showAllButton.grid(row=0,column=4,padx=4,pady=4)

        listFrame = Frame(stdntListFrame)
        listFrame.place(x=10,y=50,width=850,height=650)

        scrollx= ttk.Scrollbar(listFrame,orient=HORIZONTAL)
        scrolly= ttk.Scrollbar(listFrame,orient=VERTICAL)

        self.studentsList = ttk.Treeview(listFrame,column=('stdnum','fname','lname','gender','classroom','phone','email','dob','address'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
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
        self.studentsList.heading('address',text='Address')



        self.studentsList.column('stdnum',width=100)
        self.studentsList.column('fname',width=100)
        self.studentsList.column('lname',width=100)
        self.studentsList.column('gender',width=60)
        self.studentsList.column('classroom',width=60)
        self.studentsList.column('phone',width=100)
        self.studentsList.column('email',width=100)
        self.studentsList.column('dob',width=100)
        self.studentsList.column('address',width=200)
       



        self.studentsList['show'] = 'headings'
        self.studentsList.pack(fill=BOTH,expand=True)
        self.studentsList.bind("<ButtonRelease-1>",self.getStudentDetails)
        self.showStudentList()

        deleteButton = Button(self.root,height=1,width=20,text="Delete Selection",font=("times new roman",11), command=self.deleteStudent,borderwidth=0,activebackground = "navy blue", activeforeground = "white",bg="azure3", cursor="hand2")
        deleteButton.place(x=300,y=700)
       
#================================================================= Preview ====================================================================================================
        previewFrame = Frame(self.root)
        previewFrame.place(x=1180,y=100,width=450,height =600)

        previewLabel= Label(previewFrame,text='Student Preview', font=("times new roman",17,"bold"))
        previewLabel.grid(row=0,column=1,sticky=W)
        
    def refreshList(self):
        self.showStudentList()

    def showStudentList(self):
        databaseConnection=mysql.connector.connect(host='localhost',username="root",password='9878059867gG@',database='student_list')
        commandSelected = databaseConnection.cursor()
        commandSelected.execute("SELECT * FROM student_list.student")
        studentDetail = commandSelected.fetchall()
        if(len(studentDetail)!=0):
            self.studentsList.delete(*self.studentsList.get_children())
            for everyStudent in studentDetail:
                self.studentsList.insert("",END,values = everyStudent)

        databaseConnection.commit()
        databaseConnection.close()
    
    def addStudent(self):
        self.addStudentWindow = Toplevel(self.root)
        self.app=AddNewStudent(self.addStudentWindow)

    def updateStdntInfo(self):
        self.updateStdntInfoWindow = Toplevel(self.root)
        self.newWindow=UpdateStudentInfo(self.updateStdntInfoWindow)

    def getStudentDetails(self,value=""):
        focusedStudent= self.studentsList.focus()
        tabelContent = self.studentsList.item(focusedStudent)
        studentDetailsRow =tabelContent['values']

        self.studentNo.set(studentDetailsRow[0])
        self.firstName.set(studentDetailsRow[1])
        self.lastName.set(studentDetailsRow[2])
        self.gender.set(studentDetailsRow[3])
        self.date.set(studentDetailsRow[-2][0])
        self.month.set(studentDetailsRow[-2][2:6])
        self.year.set(studentDetailsRow[-2][6:])
        self.phone.set(studentDetailsRow[5])
        self.email.set(studentDetailsRow[6])
        self.address.set(studentDetailsRow[-1])
        self.grade.set(studentDetailsRow[4][0])
        self.section.set(studentDetailsRow[4][-1])

        previewFrame = Frame(self.root)
        previewFrame.place(x=1200,y=150,width=430,height =580)

        fullName= "Full Name:  {fname} {lname}".format(fname = studentDetailsRow[1], lname = studentDetailsRow[2])
        gender = "Gender: {gender}".format(gender = studentDetailsRow[3])
        classroom = "Classroom: {classroom}".format(classroom=studentDetailsRow[4])
        phone="Phone Number: {phone}".format(phone=studentDetailsRow[5])
        email="Email: {email}".format(email=studentDetailsRow[6])
        dob="Date of Birth: {dob}".format(dob = studentDetailsRow[-2])

        previewName = Label(previewFrame,text=fullName, font=("times new roman",13))
        previewName.grid(row=0,column=0,sticky=W)

        genderPreview = Label(previewFrame,text=gender, font=("times new roman",13))
        genderPreview.grid(row=1,column=0,sticky=W)

        classroomPreview = Label(previewFrame,text=classroom, font=("times new roman",13))
        classroomPreview.grid(row=2,column=0,sticky=W)

        phonePreview = Label(previewFrame,text=phone, font=("times new roman",13))
        phonePreview.grid(row=3,column=0,sticky=W)
        
        
        emailPreview = Label(previewFrame,text=email, font=("times new roman",13))
        emailPreview.grid(row=4,column=0,sticky=W)

        phonePreview = Label(previewFrame,text=dob, font=("times new roman",13))
        phonePreview.grid(row=5,column=0,sticky=W)
       
       

        
    def deleteStudent(self):

        answer = askyesno(title='confirmation',
                    message='Do you want to delete the selected student?')
        if answer:
        
            databaseConnection=mysql.connector.connect(host='localhost',username="root",password='9878059867gG@',database='student_list')
            commandSelected = databaseConnection.cursor()
            commandSelected.execute("DELETE FROM student WHERE (`Student No` = %s)",(self.studentNo.get(),))
            
            databaseConnection.commit()
            self.showStudentList()
            databaseConnection.close()



if __name__ == "__main__":
        root = Tk()
        testObj = Dashboard(root)
        root.mainloop()









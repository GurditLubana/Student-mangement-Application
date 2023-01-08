from tkinter import*
from tkinter import ttk,messagebox



class Signup:
    def __init__(self, root):
        self.root = root
        root.title("Create new account")
        root.geometry("1000x700+400+100")
        root.configure(bg="#fff")
        root.resizable(False,False)

        self.img = PhotoImage(file='signupImage.png')
        Label(self.root,image=self.img,bg='white').place(x=50,y=50)
    
        loginLabel=Label(self.root,text='Sign Up',font=("times new roman",25,'bold'),bg='white',fg='#57a1f8')
        loginLabel.place(x=650,y=120)

        usernameLabel= Label(self.root,text='Username',font=("times new roman",13),bg='white')
        usernameLabel.place(x=600,y=200)

        usernameEntry = Entry(self.root,width=20,bd=0,font=("times new roman",13))
        usernameEntry.place(x=600,y=240)

        Frame(self.root,width=270,height=2,bg='#57a1f8').place(x=600,y=265)

        passwordLabel= Label(self.root,text='Password',font=("times new roman",13),bg='white')
        passwordLabel.place(x=600,y=300)

        passwordEntry = Entry(self.root,width=20,bd=0,font=("times new roman",13),show="*")
        passwordEntry.place(x=600,y=340)

        Frame(self.root,width=270,height=2,bg='#57a1f8').place(x=600,y=365)

        confirmpasswordLabel= Label(self.root,text='Confirm Password',font=("times new roman",13),bg='white')
        confirmpasswordLabel.place(x=600,y=395)

        confirmpasswordEntry = Entry(self.root,width=20,bd=0,font=("times new roman",13),show="*")
        confirmpasswordEntry.place(x=600,y=430)

        Frame(self.root,width=270,height=2,bg='#57a1f8').place(x=600,y=455)

        signinBtn= Button(self.root,text="Sign up",fg='white',bg="#57a1f8",font=("times new roman",13), command = root.withdraw, cursor="hand2",width=25)
        signinBtn.place(x=620,y=490)


if __name__ == "__main__":
    root = Tk()
    testObj = Signup(root)        
    root.mainloop()
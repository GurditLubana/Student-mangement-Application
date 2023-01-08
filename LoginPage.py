from tkinter import*
from tkinter import ttk,messagebox
from Dashboard import Dashboard
from Signup import Signup


class LoginPage:
    def __init__(self, root):
        self.root = root
        root.title("Login")
        root.geometry("1000x700+400+100")
        root.configure(bg="#fff")
        root.resizable(False,False)

        self.img = PhotoImage(file='login.png')
        self.img = self.img.subsample(4)
        Label(self.root,image=self.img,bg='white').place(x=50,y=50)
    
        loginLabel=Label(self.root,text='Log In',font=("times new roman",25,'bold'),bg='white',fg='#57a1f8')
        loginLabel.place(x=700,y=120)

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

        signinBtn= Button(self.root,text="Sign up",fg='white',bg="#57a1f8",font=("times new roman",13), command = self.openDashboard, cursor="hand2",width=25)
        signinBtn.place(x=620,y=400)

        Label(self.root,text="Don't have an account? ",font=("times new roman",13),bg='white').place(x=600,y=445)

        
        signupBtn= Button(self.root,text="Sign up", bd=0,fg='#57a1f8',command=self.signupWindow,bg="white",font=("times new roman",13), cursor="hand2")
        signupBtn.place(x=758,y=445)

    def openDashboard(self):
        self.openDashboardWindow = Toplevel(self.root)
        self.app=Dashboard(self.openDashboardWindow)

    def signupWindow(self):
        self.openDashboardWindow = Toplevel(self.root)
        self.app=Signup(self.openDashboardWindow)


if __name__ == "__main__":
    root = Tk()
    testObj = LoginPage(root)        
    root.mainloop()
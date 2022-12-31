from tkinter import *
import random
import time
import datetime
from tkinter import messagebox
# import mysql.connector

class Hospital:

    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        Label(self.root,text="HOSPITAL MANAGEMENT SYSTEM",relief = RIDGE,bd=2,bg = "navy blue",fg="white", font =("times new roman", 30,"bold")).pack(side=TOP,fill=X)
        Frame(self.root,bd=2,bg = "navy blue", relief = RIDGE).place(x=0,y=50,width=240,height=735)






root = Tk()
Hospital(root)
root.mainloop()


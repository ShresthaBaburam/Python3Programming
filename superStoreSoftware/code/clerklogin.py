from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
date = datetime.datetime.now().date()

conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()


class ClerkLogin:
    def __init__(self,root1):
        self.root1=root1
        self.root1.title(" Clerk Login Page")
        self.root1.geometry("600x350+380+200")
        self.root1.config(bg="#021e2f")
        self.root1.resizable(False,False)

        #creating a frame

        self.clerk_login_frame = Frame(self.root1, bg="white")
        self.clerk_login_frame.place(x=50, y=30, width=500, height=290)

        self.back_btn = Button(root1, text="<", command=self.back,bg="#021e2f", fg="green", font=("times new roman", 15, "bold"),width=2, )
        self.back_btn.place(x=0, y=0)

        self.label_title = Label(self.clerk_login_frame, text=" Clerk Login", font=("times new roman", 30, "bold"), bg="white", fg="green")
        self.label_title.place(x=100, y=10)

        #entry field
        self.label_user_name = Label(self.clerk_login_frame, text="User Name", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.label_user_name.place(x=120, y=80)
        self.entry_clerk_user_name = Entry(self.clerk_login_frame, font=("times new roman", 20), bg="lightgray", )
        self.entry_clerk_user_name.place(x=120, y=110)

        self.label_password = Label(self.clerk_login_frame, text="Password",  font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.label_password.place(x=120, y=150)
        self.entry_clerk_password = Entry(self.clerk_login_frame,show='*', font=("times new roman", 20), bg="lightgray", )
        self.entry_clerk_password.place(x=120, y=180)

        self.register_btn = Button(self.clerk_login_frame,  text="Register", command=self.register,bg="white", fg="blue", font=("times new roman", 15), bd=0, )
        self.register_btn.place(x= 50, y=240)

        sql= "SELECT clerk_id FROM clerk "
        result = c.execute(sql,)
        for r in result:
            self.r1=r[0]
            if self.r1 >=1:
                self.register_btn.destroy()
  
        conn.commit()

        self.forgot_password_btn = Button(self.clerk_login_frame,text="Forgot Password",command=self.forget_password, bg="white", fg="red", font=("times new roman", 15),bd=0, )
        self.forgot_password_btn.place(x= 160, y=240)
        
        self.login_btn = Button(self.clerk_login_frame, command=self.clerkLogin,text="Login", bg="white", fg="green", font=("times new roman", 15, "bold"),width=7, )
        self.login_btn.place(x=340, y=240)

        

    def back(self,*args,**kwargs):
        self.root1.destroy()
        import main


    def register(self,*args,**kwargs):
        self.root1.destroy()
        import clerkregister

    def forget_password(self,*args,**kwargs):
        #self.root1.destroy()
        import clerkforgotpassword

    def clerkLogin(self,*args,**kwargs):
        self.clerk_username= self.entry_clerk_user_name.get()
        self.clerk_password= self.entry_clerk_password.get()
        
        sql= "SELECT clerk_user_name, clerk_password FROM clerk "
        result = c.execute(sql,)
        for r in result:
            self.r1=r[0]
            self.r2=r[1]
        
        conn.commit()
        if self.clerk_username== self.r1 and self.clerk_password== self.r2:
                
            tkinter.messagebox.showinfo("welcome!","Login was successfull!")
            self.root1.destroy()
            import clerkmenu                
        else:
            tkinter.messagebox.showinfo("Error!","Incorrect User Name or Password.\nPlease Enter  Correct User Name and Password.")

        


root1 = Tk()
_ClerkLogin =ClerkLogin(root1)
root1.mainloop()
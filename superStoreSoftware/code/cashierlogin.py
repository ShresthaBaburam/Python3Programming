from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
date = datetime.datetime.now().date()

conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()


class CashierLogin:
    def __init__(self,root):
        self.root=root
        self.root.title(" Cashier Login Page")
        self.root.geometry("600x350+380+200")
        self.root.config(bg="#021e2f")
        self.root.resizable(False,False)

        #creating a frame

        self.cashier_login_frame = Frame(self.root, bg="white")
        self.cashier_login_frame.place(x=50, y=30, width=500, height=290)

        self.back_btn = Button(root, text="<", command=self.back,bg="#021e2f", fg="green", font=("times new roman", 15, "bold"),width=2, )
        self.back_btn.place(x=0, y=0)

        self.title = Label(self.cashier_login_frame, text=" Cashier Login", font=("times new roman", 30, "bold"), bg="white", fg="green")
        self.title.place(x=100, y=30)

        #entry field
        self.label_user_name = Label(self.cashier_login_frame, text="User Name", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.label_user_name.place(x=120, y=80)
        self.entry_cashier_user_name = Entry(self.cashier_login_frame, font=("times new roman", 20), bg="lightgray", )
        self.entry_cashier_user_name.place(x=120, y=110)

        self.label_password = Label(self.cashier_login_frame, text="Password",  font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.label_password.place(x=120, y=150)
        self.entry_cashier_password = Entry(self.cashier_login_frame,show='*', font=("times new roman", 20), bg="lightgray", )
        self.entry_cashier_password.place(x=120, y=180)


        self.cashier_forgot_password_btn = Button(self.cashier_login_frame,command=self.cashierForgetPassword,text="Forgot Password",bg="white", fg="red", font=("times new roman", 15),bd=0, )
        self.cashier_forgot_password_btn.place(x= 120, y=240)

        self.cashier_login_btn = Button(self.cashier_login_frame, command=self.cashierLogin,text="Login", bg="white", fg="green", font=("times new roman", 15, "bold"),width=7, )
        self.cashier_login_btn.place(x=290, y=240)

    def back(self,*args,**kwargs):
        self.root.destroy()
        import main

    def cashierForgetPassword(self,*args,**kwargs):
        self.root.destroy()

        import cashierforgotpassword

    def cashierLogin(self,*args,**kwargs):
        self.cashier_username= self.entry_cashier_user_name.get()
        self.cashier_password= self.entry_cashier_password.get()
        sql= "SELECT cashier_user_name, cashier_password FROM cashier "
        result = c.execute(sql,)
        for r in result:
            self.r1=r[0]
            self.r2=r[1]
        conn.commit()
        if self.cashier_username== self.r1 and self.cashier_password== self.r2:
                
            tkinter.messagebox.showinfo("welcome!","Login was successfull!")
            self.root.destroy()
            import cashiermenu
                
        else:
            tkinter.messagebox.showinfo("Error!","Incorrect User Name or Password.\nPlease Enter  Correct User Name and Password.")

        
    


root = Tk()
_CashierLogin =CashierLogin(root)
root.mainloop()
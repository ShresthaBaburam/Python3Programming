from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()


date = datetime.datetime.now().date()

class CashierForgotPasswordPage:
    def __init__(self,root):
        self.root=root
        self.root.title("Cashier Forgot Password Page")
        self.root.config(bg="#021e2f")
        self.root.geometry("700x450+330+100")

       # forgot password frame
        forgot_password_frame=Frame(self.root,bg="white")
        forgot_password_frame.place(x=75,y=50,width=550,height=350)

        back_btn = Button(root, text="<", command=self.back,bg="#021e2f", fg="green", font=("times new roman", 15, "bold"),width=2, )
        back_btn.place(x=0, y=0)

        label_heading = Label(forgot_password_frame, text="Enter Details For Reset Password", font=("times new roman", 20, "bold"), bg="grey", fg="black")
        label_heading.place(x=80, y=10)

        label_cashier_id = Label(forgot_password_frame, text="Cahier Id:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_cashier_id.place(x=50, y=50)
        self.entry_cashier_id = Entry(forgot_password_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_cashier_id.place(x=220, y=50)

        label_cashier_username = Label(forgot_password_frame, text="Cashier UserName:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_cashier_username.place(x=50, y=100)
        self.entry_cashier_username = Entry(forgot_password_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_cashier_username.place(x=220, y=100)

        label_cashier_phone = Label(forgot_password_frame, text="Cashier Phone:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_cashier_phone.place(x=50, y=150)
        self.entry_cashier_phone = Entry(forgot_password_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_cashier_phone.place(x=220, y=150)

        label_cashier_dob = Label(forgot_password_frame, text="Cahier E-mail:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_cashier_dob.place(x=50, y=200)
        self.entry_cashier_email = Entry(forgot_password_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_cashier_email.place(x=220, y=200)


        label_cashier_new_password = Label(forgot_password_frame, show='*',text="New Password:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_cashier_new_password.place(x=50, y=250)
        self.entry_cashier_new_password = Entry(forgot_password_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_cashier_new_password.place(x=220, y=250)

        self.reset_btn = Button(forgot_password_frame, command=self.cashierForgotPassword,text="Reset Password", bg="white", fg="green", font=("times new roman", 15, "bold"),width=15, )
        self.reset_btn.place(x=300, y=290)

    def back(self,*args,**kwargs):
        self.root.destroy()
        import cashierlogin

    def cashierForgotPassword(self,*args,**kwargs):
        self.id = int(self.entry_cashier_id.get())
        self.username=self.entry_cashier_username.get()
        self.phone=self.entry_cashier_phone.get()
        self.email = self.entry_cashier_email.get()
        self.newpassword= self.entry_cashier_new_password.get()

        sql= "SELECT cashier_id,cashier_user_name,cashier_phone,cashier_email FROM cashier"
        self.result = c.execute(sql).fetchall()
        for re in self.result:
            self.r1=re[0]
            self.r2=re[1]
            self.r3=re[2]
            self.r4=re[3]
            conn.commit()
            if self.id== self.r1 and self.username==self.r2 and self.phone==self.r3 and self.email==self.r4:
                sql = "UPDATE  cashier SET cashier_password=? WHERE cashier_id=?"
                c.execute(sql, (self.newpassword,self.id))        
                tkinter.messagebox.showinfo("Success!", "Successfully!!!\nThe Password Is\nNow Updated ")

                self.root.destroy()
                import cashierlogin
            else:
                tkinter.messagebox.showinfo("Error!", "You should Know all Four \nThings To Reset Password.")

        
        
        


root = Tk()
_CashierForgotPasswordPage =CashierForgotPasswordPage(root)
root.mainloop()
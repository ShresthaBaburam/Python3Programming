from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()


date = datetime.datetime.now().date()

class ClerkForgotPasswordPage:
    def __init__(self,root):
        self.root=root
        self.root.title("Clerk Forgot Password Page")
        self.root.config(bg="#021e2f")
        self.root.geometry("700x450+330+100")

       # forgot password frame
        forgot_password_frame=Frame(self.root,bg="white")
        forgot_password_frame.place(x=75,y=50,width=550,height=350)

        self.back_btn = Button(root, text="<", command=self.back,bg="#021e2f", fg="green", font=("times new roman", 15, "bold"),width=2, )
        self.back_btn.place(x=0, y=0)

        label_heading = Label(forgot_password_frame, text="Enter Details For Reset Password", font=("times new roman", 20, "bold"), bg="grey", fg="black")
        label_heading.place(x=80, y=10)

        label_clerk_id = Label(forgot_password_frame, text="Clerk Id:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_id.place(x=50, y=50)
        self.entry_clerk_id = Entry(forgot_password_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_id.place(x=210, y=50)

        label_clerk_username = Label(forgot_password_frame, text="Clerk UserName:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_username.place(x=50, y=100)
        self.entry_clerk_username = Entry(forgot_password_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_username.place(x=210, y=100)

        label_clerk_phone = Label(forgot_password_frame, text="Clerk Phone:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_phone.place(x=50, y=150)
        self.entry_clerk_phone = Entry(forgot_password_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_phone.place(x=210, y=150)

        label_clerk_email = Label(forgot_password_frame, text="Clerk E-mail:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_email.place(x=50, y=200)
        self.entry_clerk_email = Entry(forgot_password_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_email.place(x=210, y=200)


        label_clerk_new_password = Label(forgot_password_frame, text="New Password:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_new_password.place(x=50, y=250)
        self.entry_clerk_new_password = Entry(forgot_password_frame,show='*', font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_new_password.place(x=210, y=250)

        reset_btn = Button(forgot_password_frame, command=self.clerkForgotPassword,text="Reset Password", bg="white", fg="green", font=("times new roman", 15, "bold"),width=15, )
        reset_btn.place(x=290, y=290)

    def back(self,*args,**kwargs):
        self.root.destroy()
        import clerklogin

    def clerkForgotPassword(self,*args,**kwargs):
        self.id = int(self.entry_clerk_id.get())
        self.username=self.entry_clerk_username.get()
        self.phone=self.entry_clerk_phone.get()
        self.email = self.entry_clerk_email.get()
        self.newpassword= self.entry_clerk_new_password.get()

        sql= "SELECT clerk_id,clerk_user_name,clerk_phone,clerk_email FROM clerk"
        self.result = c.execute(sql).fetchall()
        for r in self.result:
            self.r1=r[0]
            self.r2=r[1]
            self.r3=r[2]
            self.r4=r[3]
            conn.commit()
            if self.id== self.r1 and self.username==self.r2 and self.phone==self.r3 and self.email==self.r4:
                sql = "UPDATE  clerk SET clerk_password=? WHERE clerk_id=?"
                c.execute(sql, (self.newpassword,self.id))        
                tkinter.messagebox.showinfo("Success!", "Successfully!!!\nThe Password Is\nNow Updated ")
                

                self.root.destroy()
        
                import clerklogin

            else:
                tkinter.messagebox.showinfo("Error!", "You should Know all Four \nThings To Reset Password.")

        


root = Tk()
_ClerkForgotPasswordPage =ClerkForgotPasswordPage(root)
root.mainloop()
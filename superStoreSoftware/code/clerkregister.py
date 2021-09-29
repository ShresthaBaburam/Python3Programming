from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
from tkcalendar import Calendar, DateEntry
conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()


date = datetime.datetime.now().date()

class ClerkRegister:
    def __init__(self,root):
        self.root=root
        self.root.title("Clerk Registration Page")
        self.root.config(bg="#021e2f")
        self.root.geometry("700x550+330+100")
        
        # register frame
        self.register_frame=Frame(self.root,bg="white")
        self.register_frame.place(x=75,y=50,width=550,height=450)

        self.back_btn = Button(root, text="<", command=self.back,bg="#021e2f", fg="green", font=("times new roman", 15, "bold"),width=2, )
        self.back_btn.place(x=0, y=0)

        label_heading = Label(self.register_frame, text="Enter Details For Clerk Register", font=("times new roman", 20, "bold"), bg="grey", fg="black")
        label_heading.place(x=80, y=10)

        label_clerk_name = Label(self.register_frame, text="Clerk Name:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_name.place(x=50, y=50)
        self.entry_clerk_name = Entry(self.register_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_name.place(x=210, y=50)

        label_clerk_username = Label(self.register_frame, text="Clerk UserName:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_username.place(x=50, y=100)
        self.entry_clerk_username = Entry(self.register_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_username.place(x=210, y=100)

        label_clerk_password = Label(self.register_frame, text="Clerk Password:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_password.place(x=50, y=150)
        self.entry_clerk_password = Entry(self.register_frame,show='*', font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_password.place(x=210, y=150)

        label_clerk_dob = Label(self.register_frame, text="Date Of Birth:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_dob.place(x=50, y=200)
        self.entry_clerk_dob = DateEntry(self.register_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_dob.place(x=210, y=200)

        label_clerk_address = Label(self.register_frame, text="Clerk Address:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_address.place(x=50, y=250)
        self.entry_clerk_address = Entry(self.register_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_address.place(x=210, y=250)

        label_clerk_phone= Label(self.register_frame, text="Clerk Phone:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_phone.place(x=50, y=300)
        self.entry_clerk_phone = Entry(self.register_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_phone.place(x=210, y=300)

        label_clerk_email = Label(self.register_frame, text="Clerk E-mail:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_clerk_email.place(x=50, y=350)
        self.entry_clerk_email = Entry(self.register_frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_clerk_email.place(x=210, y=350)

        self.register_btn = Button(self.register_frame,command=self.clerkRegister, text="Register", bg="white", fg="green", font=("times new roman", 15, "bold"),width=10, )
        self.register_btn.place(x=340, y=390)

    def back(self,*args,**kwargs):
        self.root.destroy()
        import clerklogin

    def clerkRegister(self,*args,**kwargs):
        self.name = self.entry_clerk_name.get()
        self.username=self.entry_clerk_username.get()
        self.password= self.entry_clerk_password.get()
        self.dob=self.entry_clerk_dob.get()
        self.address= self.entry_clerk_address.get()
        self.phone=self.entry_clerk_phone.get()
        self.email = self.entry_clerk_email.get()
        if self.name and self.username and self.password and self.dob and self.address and self.phone and self.email!='':
            sql="INSERT INTO clerk (clerk_name, clerk_user_name,clerk_password,clerk_dob, clerk_address,clerk_phone,clerk_email,added_date) VALUES(?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.name,self.username,self.password,self.dob,self.address,self.phone,self.email,date))
            conn.commit()

            tkinter.messagebox.showinfo("Success!,", "Successfully!!!\nThe Clerk Details are \nSaved in Database!!!")
            self.root.destroy()
            import clerklogin
        else:
            tkinter.messagebox.showinfo("Error!", "Please Fill All Fields\n All Fields are Required")

root=Tk()
_Clearkregister=ClerkRegister(root)
root.mainloop()
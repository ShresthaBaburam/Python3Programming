from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()


date = datetime.datetime.now().date()

class ClerkChangePassword:
    def __init__(self,root):
        self.root=root
        self.root.title("Clerk Password Change Page")
        self.root.config(bg="#021e2f")
        self.root.geometry("700x500+330+100")
        
        # register frame
        self.register_frame=Frame(self.root,bg="white")
        self.register_frame.place(x=75,y=50,width=550,height=400)

        self.back_btn = Button(root, text="<", command=self.back,bg="#021e2f", fg="green", font=("times new roman", 15, "bold"),width=2, )
        self.back_btn.place(x=0, y=0)

        self.label_heading = Label(self.register_frame, text="You Are Clerk And Change Your Password", font=("times new roman", 20, "bold"), bg="grey", fg="black")
        self.label_heading.place(x=10, y=10)

        self.label_clerk_id = Label(self.register_frame, text="Enter Your Id:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.label_clerk_id.place(x=50, y=60)

        self.entry_clerk_id = Entry(self.register_frame,font=("times new roman", 15), bg="lightgray", width=8)
        self.entry_clerk_id.place(x=210, y=60)


        self.id_btn = Button(self.register_frame, text="Proceed", command=self.view,bg="grey", fg="purple", font=("times new roman", 12, "bold"),width=8, )
        self.id_btn.place(x=330, y=56)

        

    def back(self,*args,**kwargs):
        self.root.destroy()
        
    def view(self,*args,**kwargs):

        sql= "SELECT clerk_id,clerk_password FROM clerk WHERE clerk_id=?"
        self.result = c.execute(sql,(self.entry_clerk_id.get())).fetchall()
        for r in self.result:
            self.r1=r[0]
            self.r2=r[1]
        

            if self.r1== int(self.entry_clerk_id.get()):
                self.label_clerk_current_password = Label(self.register_frame, text="Current Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                self.label_clerk_current_password.place(x=50, y=100)
                self.entry_clerk_current_password = Entry(self.register_frame, show='*',font=("times new roman", 15), bg="lightgray",width=25 )
                self.entry_clerk_current_password.place(x=230, y=100)

                self.label_clerk_new_password = Label(self.register_frame, text="Your New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                self.label_clerk_new_password.place(x=50, y=150)
                self.entry_clerk_new_password= Entry(self.register_frame, show='*', font=("times new roman", 15), bg="lightgray",width=25 )
                self.entry_clerk_new_password.place(x=230, y=150)
        
                self.label_clerk_re_new_password = Label(self.register_frame, text="Re New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                self.label_clerk_re_new_password.place(x=50, y=200)
                self.entry_clerk_re_new_password = Entry(self.register_frame, show='*', font=("times new roman", 15), bg="lightgray",width=25 )
                self.entry_clerk_re_new_password.place(x=230, y=200)

                self.change_btn = Button(self.register_frame,command=self.changePassword,text="Change Password", bg="white", fg="green", font=("times new roman", 15, "bold"),width=15, )
                self.change_btn.place(x=250, y=240)
            else:
                self.entry_clerk_id.delete(0,END)
                tkinter.messagebox.showinfo("Error!","Wrong Clerk Id Format.\nClerk Id Format:Number.\nEnter  Correct Clerk Id.")
        

    def changePassword(self,*args,**kwargs):

        self.current_password= self.entry_clerk_current_password.get()
        self.new_password=self.entry_clerk_new_password.get()
        self.re_new_password= self.entry_clerk_re_new_password.get()

        sql= "SELECT * FROM clerk WHERE clerk_id=?"
        self.result = c.execute(sql,(self.entry_clerk_id.get()))

        self.r1=0
        self.r2=0
        for r in self.result:
            self.r1=r[0]
            self.r2=r[3]
        conn.commit()

        if self.r2==self.current_password and self.new_password==self.re_new_password:
            sql = "UPDATE  clerk SET clerk_password=? WHERE clerk_id=?"
            c.execute(sql, (self.new_password,self.r1))
            tkinter.messagebox.showinfo("Success!","Passwords Changed\n Successfully!")
                
        elif self.r2==self.current_password and self.new_password!=self.re_new_password:
            tkinter.messagebox.showinfo("Error!","New Passwords Does not Match\n Enter Same Password!")

        elif self.r2!=self.current_password and self.new_password==self.re_new_password:
            tkinter.messagebox.showinfo("Error!","Current Password Does not Match\n Enter Correct Password!")
        else:
            tkinter.messagebox.showinfo("Error!","Current Password Does not Match\nOr\n New Passwords Does not Match\n Enter Same Password!")


        conn.commit()



root=Tk()
_ClerkChangePassword = ClerkChangePassword(root)
root.mainloop()
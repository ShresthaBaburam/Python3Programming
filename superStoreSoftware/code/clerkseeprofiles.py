from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()


date = datetime.datetime.now().date()

class ClerkSeeProfiles:
    def __init__(self,root):
        self.root=root
        self.root.title("clerk Details Page")
        self.root.config(bg="#021e2f")
        self.root.geometry("700x500+330+100")
        
        # register frame
        self.register_frame=Frame(self.root,bg="white")
        self.register_frame.place(x=75,y=50,width=550,height=400)

        self.back_btn = Button(root, text="<", command=self.back,bg="#021e2f", fg="green", font=("times new roman", 15, "bold"),width=2, )
        self.back_btn.place(x=0, y=0)

        label_heading = Label(self.register_frame, text="You Are Clerk And Your Details:", font=("times new roman", 20, "bold"), bg="grey", fg="black")
        label_heading.place(x=80, y=10)

        self.label_clerk_id = Label(self.register_frame, text="Enter Your Id:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.label_clerk_id.place(x=50, y=60)

        self.entry_clerk_id = Entry(self.register_frame,font=("times new roman", 15), bg="lightgray", width=8)
        self.entry_clerk_id.place(x=210, y=60)


        self.id_btn = Button(self.register_frame, text="View", command=self.view,bg="grey", fg="purple", font=("times new roman", 12, "bold"),width=8, )
        self.id_btn.place(x=330, y=60)

        self.label_clerk_name = Label(self.register_frame, text="Your Name:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.label_clerk_name.place(x=50, y=100)

        self.label_clerk_username = Label(self.register_frame, text="Your UserName:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.label_clerk_username.place(x=50, y=150)
 
        self.label_clerk_dob = Label(self.register_frame, text="Your DoB:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.label_clerk_dob.place(x=50, y=200)

        self.label_clerk_address = Label(self.register_frame, text="Your Address:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.label_clerk_address.place(x=50, y=250)

        self.label_clerk_phone= Label(self.register_frame, text="Your Phone:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.label_clerk_phone.place(x=50, y=300)

        self.label_clerk_email = Label(self.register_frame, text="Your E-mail:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.label_clerk_email.place(x=50, y=350)




    def back(self,*args,**kwargs):
        self.root.destroy()
        
    def view(self,*args,**kwargs):
        self.id=self.entry_clerk_id.get()
        sql= "SELECT * FROM clerk WHERE clerk_id=?"
        self.result = c.execute(sql,(self.id)).fetchall()
        for r in self.result:
            self.r1=r[1]
            self.r2=r[2]
            self.r4=r[4]
            self.r5=r[5]
            self.r6=r[6]
            self.r7=r[7]
            self.r8=r[8]
        
            
        conn.commit()
        self.label_clerk_name.configure(text="Your Name:\t"+str(self.r1))
        self.label_clerk_username.configure(text="Your UserName:\t"+str(self.r2))
        self.label_clerk_dob.configure(text="Your DoB:\t"+str(self.r4))
        self.label_clerk_address.configure(text="Your Address:\t"+str(self.r5))
        self.label_clerk_phone.configure(text="Your Phone:\t"+str(self.r6))
        self.label_clerk_email.configure(text="Your E-mail:\t"+str(self.r7))

root=Tk()
_ClerkSeeProfiles = ClerkSeeProfiles(root)
root.mainloop()
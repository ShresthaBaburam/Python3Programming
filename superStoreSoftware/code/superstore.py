from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()




class MainPage:
    def __init__(self,root):
        self.res = c.execute("SELECT * from superStore")
        for r in self.res:
            self.id=r[0]
            if self.id == 1:
                root.destroy()
                import main
        conn.commit()


        self.root=root
        self.root.title(" Welcome Page")
        self.root.geometry("600x350+380+200")
        self.root.config(bg="#021e2f")
        self.root.resizable(False,False)

        #creating a frame

        frame = Frame(self.root, bg="white")
        frame.place(x=50, y=50, width=500, height=250)

        title = Label(frame, text="Enter Superstore Details.", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title.place(x=30, y=10)

        self.label_superstore_name = Label(frame, text="Superstore Name:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.label_superstore_name.place(x=30, y=100)
        self.entry_superstore_name = Entry(frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_superstore_name.place(x=210, y=100)

        self.label_superstore_address = Label(frame, text="Superstore Address:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.label_superstore_address.place(x=30, y=150)
        self.entry_suprestore_address = Entry(frame, font=("times new roman", 15), bg="lightgray",width=25 )
        self.entry_suprestore_address.place(x=210, y=150)


        self.cashier_btn = Button(frame, text="Save and Goto Login Page", command= self.gotoMainPage,bg="white", fg="green", font=("times new roman", 14, "bold"),width=25, )
        self.cashier_btn.place(x=210, y=190)

    def gotoMainPage(self):
        

        self.name = self.entry_superstore_name.get()
        self.address= self.entry_suprestore_address.get()
        if self.name !='' and self.address !='':

            sql="INSERT INTO superStore(superstore_name,superstore_address) VALUES(?,?)"
            c.execute(sql,(self.name,self.address))
            conn.commit()
            tkinter.messagebox.showinfo("Success!", "Successfully!!!\nThe Superstore Details are \nSaved in Database!")
        else:
            tkinter.messagebox.showinfo("Error!", "Please Fill All Fields\n All Fields are Required")

        self.root.destroy()
        import main


root = Tk()
_MainPage =MainPage(root)
root.mainloop()
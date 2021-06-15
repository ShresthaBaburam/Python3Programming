from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("/home/shresthababu/G62/git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()

class ClerkLogin:
    def __init__(self,root):
        self.root= root
        self.root.geometry("800x500+280+100")
        self.root.title("Super Store  Software")
        self.root.resizable(False,False)

        # background images
        self.bg=PhotoImage(file='images/photo.png')
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)
        
        # login frame
        frameLogin = Frame(self.root, bg='lightblue')
        frameLogin.place(x=200,y=100,height=300,width=400)

        self.labal_login = Label(frameLogin, text="Login Here", font =("arial 20 bold"),bg='lightblue')
        self.labal_login.place(x = 130, y=10)

        self.labal_text = Label(frameLogin, text="Login According To Clerk Credentials", font =("arial 15 bold"),bg='lightblue')
        self.labal_text.place(x = 20, y=50)

        self.labal_clerk_id = Label(frameLogin, text="Clerk Id", font =("arial 12 bold"),bg='lightblue')
        self.labal_clerk_id.place(x = 50, y=80)

        self.entry_clerk_id = Entry(frameLogin,width= 20, font =("arial 13 bold"))
        self.entry_clerk_id.place(x=175, y=80)

        self.labal_clerk_name = Label(frameLogin, text="Clerk Name", font =("arial 12 bold"),bg='lightblue')
        self.labal_clerk_name.place(x = 50, y=120)

        self.entry_clerk_name = Entry(frameLogin,width= 20, font =("arial 13 bold"))
        self.entry_clerk_name.place(x=175, y=120)

        self.labal_password = Label(frameLogin, text="Password", font =("arial 12 bold"),bg='lightblue')
        self.labal_password.place(x = 50, y=160)

        self.entry_clerk_password = Entry(frameLogin,width= 20, font =("arial 13 bold"))
        self.entry_clerk_password.place(x=175, y=160)

        self.button_forgot_password = Button(frameLogin, text="Forgot Password", font =("arial 11 bold"), width=15, height=1, bg="steelblue", fg="white")
        self.button_forgot_password.place(x=100,y= 200)

        self.button_login = Button(frameLogin, text="Login", font =("arial 11 bold"), width=10, height=1, bg="steelblue", fg="white", command=self.clerklogin)
        self.button_login.place(x=270,y= 200)

    def clerklogin(self,*args,**kwargs):
        self.clerk_id=self.entry_clerk_id.get()
        self.clerk_name=self.entry_clerk_name.get()
        self.clerk_password = self.entry_clerk_password.get()

        if self.clerk_id =='' or self.clerk_name == '' or self.clerk_password =='':
            tkinter.messagebox.showinfo("Error!", "Sorry!!!\nAll Fields are required...")   
        else:
            clerksql= "SELECT * FROM clerk WHERE clerk_id=?"
            results = c.execute(clerksql,self.clerk_id)
            
            for r in results:
                self.r1 = r[1]
                self.r2 = r[2]
                if self.clerk_name == self.r1 and self.clerk_password == self.r2:
                    tkinter.messagebox.showinfo("Success!", "Successfully!!! Your Login Was Successful.")   
                else:
                    tkinter.messagebox.showinfo("Error!", "Sorry!! \nYour Credentials are not correct...") 
            conn.commit() 

root =Tk()
obj = ClerkLogin(root)
root.mainloop()
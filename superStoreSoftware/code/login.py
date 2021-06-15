from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("/home/shresthababu/G62/git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()

class Login:
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

        self.labal_product_name = Label(frameLogin, text="Login According To Cashier Credentials", font =("arial 15 bold"),bg='lightblue')
        self.labal_product_name.place(x = 8, y=50)

        self.labal_cashier_id = Label(frameLogin, text="User Id", font =("arial 12 bold"),bg='lightblue')
        self.labal_cashier_id.place(x = 50, y=80)

        self.entry_cashier_id = Entry(frameLogin,width= 20, font =("arial 13 bold"))
        self.entry_cashier_id.place(x=175, y=80)

        self.labal_cashier_name = Label(frameLogin, text="User Name", font =("arial 12 bold"),bg='lightblue')
        self.labal_cashier_name.place(x = 50, y=120)

        self.entry_cashier_name = Entry(frameLogin,width= 20, font =("arial 13 bold"))
        self.entry_cashier_name.place(x=175, y=120)

        self.labal_cashier_password = Label(frameLogin, text="Password", font =("arial 12 bold"),bg='lightblue')
        self.labal_cashier_password.place(x = 50, y=160)

        self.entry_cashier_password = Entry(frameLogin,width= 20, font =("arial 13 bold"))
        self.entry_cashier_password.place(x=175, y=160)

        self.button_cashier_forgot_password = Button(frameLogin, text="Forgot Password", font =("arial 11 bold"), width=15, height=1, bg="steelblue", fg="white")
        self.button_cashier_forgot_password.place(x=100,y= 200)

        self.button_cashier_login = Button(frameLogin, text="Login", font =("arial 11 bold"), width=10, height=1, bg="steelblue", fg="white",command=self.cashierlogin)
        self.button_cashier_login.place(x=270,y= 200)

        self.labal_admin_login = Label(frameLogin, text="Click 'Admin Login' Button & Go To Admin Login Page", font =("arial 10 bold"),bg='lightblue')
        self.labal_admin_login.place(x = 30, y=240)

        self.button_admin_login = Button(frameLogin, text="Admin Login", font =("arial 11 bold"), width=15, height=1, bg="steelblue", fg="white")
        self.button_admin_login.place(x=240,y= 260)
        

    def cashierlogin(self,*args,**kwargs):
        self.cashier_id=self.entry_cashier_id.get()
        self.cashier_name=self.entry_cashier_name.get()
        self.cashier_password = self.entry_cashier_password.get()

        if self.cashier_id =='' or self.cashier_name == '' or self.cashier_password =='':
            tkinter.messagebox.showinfo("Error!", "Sorry!!!\nAll Fields are required...")   
        else:
            sql= "SELECT * FROM cashier WHERE cashier_id=?"
            result = c.execute(sql,self.cashier_id)
            
            for r in result:
                self.r1 = r[1]
                self.r2 = r[2]
            
                if self.cashier_name == self.r1 and self.cashier_password == self.r2:
                    tkinter.messagebox.showinfo("Success!", "Successfully!!! Your Login Was Successful.")
                    
                else:
                    tkinter.messagebox.showinfo("Error!", "Sorry!! \nYour Credentials are not correct...") 
            conn.commit() 

root =Tk()
obj = Login(root)
root.mainloop()
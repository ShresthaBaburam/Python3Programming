from tkinter import *
import sqlite3
import tkinter.messagebox
import cashier
conn = sqlite3.connect("/home/babu/G62/Git/Python3-Programming/superStoreSoftware/database/store.db")
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
        self.labal_product_name.place(x = 8, y=70)

        self.labal_text = Label(frameLogin, text="Login According To Clerk Credentials", font =("arial 15 bold"),bg='lightblue')
        self.labal_text.place(x = 20, y=120)

        self.button_exit = Button(frameLogin, text="Exit", font =("arial 13 bold"), width=5, height=1, bg="steelblue", fg="blue",command=root.destroy)
        self.button_exit.place(x=10,y= 200)

        self.button_login = Button(frameLogin, text="Cashier Login", font =("arial 13 bold"), width=10, height=1, bg="steelblue", fg="blue", command=self.cashierLoginFrame)
        self.button_login.place(x=110,y= 200)

        self.button_login = Button(frameLogin, text="Clerk Login", font =("arial 13 bold"), width=10, height=1, bg="steelblue", fg="blue", command=self.clerkLoginFrame)
        self.button_login.place(x=260,y= 200)


    def clerkLoginFrame(self,*args,**kwargs):
        frameLogin = Frame(self.root, bg='lightblue')
        frameLogin.place(x=200,y=100,height=300,width=400)

        self.labal_login = Label(frameLogin, text="Login Here", font =("arial 20 bold"),bg='lightblue')
        self.labal_login.place(x = 130, y=10)

        self.labal_text = Label(frameLogin, text="Login According To Clerk Credentials", font =("arial 15 bold"),bg='lightblue')
        self.labal_text.place(x = 20, y=50)

        self.labal_clerk_id = Label(frameLogin, text="Clerk Id", font =("arial 12 bold"),bg='lightblue')
        self.labal_clerk_id.place(x = 50, y=90)

        self.entry_clerk_id = Entry(frameLogin,width= 20, font =("arial 13 bold"))
        self.entry_clerk_id.place(x=175, y=90)

        self.labal_clerk_name = Label(frameLogin, text="Clerk Name", font =("arial 12 bold"),bg='lightblue')
        self.labal_clerk_name.place(x = 50, y=140)

        self.entry_clerk_name = Entry(frameLogin,width= 20, font =("arial 13 bold"))
        self.entry_clerk_name.place(x=175, y=140)

        self.labal_clerk_password = Label(frameLogin, text="Password", font =("arial 12 bold"),bg='lightblue')
        self.labal_clerk_password.place(x = 50, y=190)

        self.entry_clerk_password = Entry(frameLogin,width= 20,show='*', font =("arial 13 bold"))
        self.entry_clerk_password.place(x=175, y=190)

        self.button_clerk_exit = Button(frameLogin, text="Exit", font =("arial 11 bold"), width=5, height=1, bg="steelblue", fg="blue",command=frameLogin.destroy)
        self.button_clerk_exit.place(x=10,y= 240)

        self.button_forgot_clerk_password = Button(frameLogin, text="Forgot Password", font =("arial 11 bold"), width=15, height=1, bg="steelblue", fg="red")
        self.button_forgot_clerk_password.place(x=100,y= 240)

        self.button_clerk_login = Button(frameLogin, text="Login", font =("arial 11 bold"), width=10, height=1, bg="steelblue", fg="blue", command=self.clerkLogin)
        self.button_clerk_login.place(x=272,y= 240)


    def cashierLoginFrame(self,*args,**kwargs):
        frameLogin = Frame(self.root, bg='lightblue')
        frameLogin.place(x=200,y=100,height=300,width=400)

        self.labal_login = Label(frameLogin, text="Login Here", font =("arial 20 bold"),bg='lightblue')
        self.labal_login.place(x = 130, y=10)

        self.labal_text = Label(frameLogin, text="Login According To Cashier Credentials", font =("arial 15 bold"),bg='lightblue')
        self.labal_text.place(x = 20, y=50)

        self.labal_cashier_id = Label(frameLogin, text="Cashier Id", font =("arial 12 bold"),bg='lightblue')
        self.labal_cashier_id.place(x = 50, y=90)

        self.entry_cashier_id = Entry(frameLogin,width= 20, font =("arial 13 bold"))
        self.entry_cashier_id.place(x=175, y=90)

        self.labal_cashier_name = Label(frameLogin, text="Cashier Name", font =("arial 12 bold"),bg='lightblue')
        self.labal_cashier_name.place(x = 50, y=140)

        self.entry_cashier_name = Entry(frameLogin,width= 20, font =("arial 13 bold"))
        self.entry_cashier_name.place(x=175, y=140)

        self.labal_cashier_password = Label(frameLogin, text="Password", font =("arial 12 bold"),bg='lightblue')
        self.labal_cashier_password.place(x = 50, y=190)

        self.entry_cashier_password = Entry(frameLogin,width= 20, show='*',font =("arial 13 bold"))
        self.entry_cashier_password.place(x=175, y=190)
            
        self.button_cashier_exit = Button(frameLogin, text="Exit", font =("arial 11 bold"), width=5, height=1, bg="steelblue", fg="blue",command=frameLogin.destroy)
        self.button_cashier_exit.place(x=10,y= 240)

        self.button_forgot_cashier_password = Button(frameLogin, text="Forgot Password", font =("arial 11 bold"), width=15, height=1, bg="steelblue", fg="red")
        self.button_forgot_cashier_password.place(x=100,y= 240)

        self.button_cashier_login = Button(frameLogin, text="Login", font =("arial 11 bold"), width=10, height=1, bg="steelblue", fg="blue", command=self.cashierLogin)
        self.button_cashier_login.place(x=272,y= 240)


    def clerkLogin(self,*args,**kwargs):
        self.clerk_id=int(self.entry_clerk_id.get())
        self.clerk_name=self.entry_clerk_name.get()
        self.clerk_password = self.entry_clerk_password.get()

        if self.clerk_id =='' or self.clerk_name == '' or self.clerk_password =='':
            tkinter.messagebox.showinfo("Error!", "Sorry!!!\nAll Fields are required...")   
        else:
            clerksql= "SELECT * FROM clerk WHERE clerk_id=?"
            results = c.execute(clerksql,self.entry_clerk_id.get())
            
            for r in results:
                self.r1 = r[1]
                self.r2 = r[2]
                if self.clerk_name == self.r1 and self.clerk_password == self.r2:
                    tkinter.messagebox.showinfo("Success!", "Successfully!!! Your Login Was Successful.")  
                    
                else:
                    tkinter.messagebox.showinfo("Error!", "Sorry!! \nYour Credentials are not correct...") 
            conn.commit()    

    def cashierLogin(self,*args,**kwargs):
        self.cashier_id=int(self.entry_cashier_id.get())
        self.cashier_name=self.entry_cashier_name.get()
        self.cashier_password = self.entry_cashier_password.get()

        if self.cashier_id =='' or self.cashier_name == '' or self.cashier_password =='':
            tkinter.messagebox.showinfo("Error!", "Sorry!!!\nAll Fields are required...")   
        else:
            sql= "SELECT * FROM cashier WHERE cashier_id=?"
            result = c.execute(sql,self.entry_cashier_id.get())
            
            for r in result:
                self.r1 = r[1]
                self.r2 = r[2]
            
                if self.cashier_name == self.r1 and self.cashier_password == self.r2:
                    tkinter.messagebox.showinfo("Success!", "Successfully!!! Your Login Was Successful.")
                else:
                    tkinter.messagebox.showinfo("Error!", "Sorry!! \nYour Credentials are not correct...") 
            conn.commit() 

root =Tk()
loginObject = Login(root)   
root.mainloop()
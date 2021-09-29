from tkinter import *


class MainPage:
    def __init__(self,root):
        self.root=root
        self.root.title(" Main Page")
        self.root.geometry("600x300+380+200")
        self.root.config(bg="#021e2f")
        self.root.resizable(False,False)

        #creating a frame

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=50, y=50, width=500, height=200)

        title = Label(login_frame, text="Select Your Role to Login.", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title.place(x=20, y=20)


        clerk_btn = Button(login_frame,text="Clerk", command=self.clerk_login,bg="white", fg="green", font=("times new roman", 15, "bold"),width=8, )
        clerk_btn.place(x= 100, y=100)

   
        cashier_btn = Button(login_frame, text="Cashier", command= self.cashier_login,bg="white", fg="green", font=("times new roman", 15, "bold"),width=8, )
        cashier_btn.place(x=300, y=100)

    def clerk_login(self):
        self.root.destroy()
        import clerklogin

    def cashier_login(self):
        self.root.destroy()
        import cashierlogin

root = Tk()
_MainPage =MainPage(root)
root.mainloop()
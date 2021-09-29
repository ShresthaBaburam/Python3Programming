from tkinter import *

root = Tk()
root.title("Cashier Menu Page")
root.geometry("600x350+380+200")
root.config(bg="#021e2f")
root.resizable(False,False)

my_menu= Menu(root)
root.config(menu=my_menu)

def seeProfiles():
    import cashierseeprofiles

def changePassword():
    import cashierchangepassword

def logout():
    root.destroy()
    import main

cashier_menu=Menu(my_menu)
my_menu.add_cascade(label="Profile", menu=cashier_menu)
cashier_menu.add_command(label='See Profiles', command=seeProfiles)
cashier_menu.add_command(label='Change passoword', command=changePassword)
cashier_menu.add_command(label='Logout', command=logout)

def manageProducts():
    import manageproduct

def sellProducts():
    import cashiersell

cashier_menu=Menu(my_menu)
my_menu.add_cascade(label="Product", menu=cashier_menu)
cashier_menu.add_command(label='Manage Product', command=manageProducts)
cashier_menu.add_command(label='Sell Product', command=sellProducts)

root.mainloop()
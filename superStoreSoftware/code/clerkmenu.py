from tkinter import *

root = Tk()
root.title("Clerk Menu Page")
root.geometry("600x350+380+200")
root.config(bg="#021e2f")
root.resizable(False,False)

my_menu= Menu(root)
root.config(menu=my_menu)

def seeProfiles():
    import clerkseeprofiles

def changePassword():
    import clerkchangepassword

def logout():
    root.destroy()
    import main

clerk_menu=Menu(my_menu)
my_menu.add_cascade(label="Profile", menu=clerk_menu)
clerk_menu.add_command(label='See Profiles', command=seeProfiles)
clerk_menu.add_command(label='Change passoword', command=changePassword)
clerk_menu.add_command(label='Logout', command=logout)

def manageProducts():
    import manageproduct

def sellProducts():
    import cashiersell

clerk_menu=Menu(my_menu)
my_menu.add_cascade(label="Product", menu=clerk_menu)
clerk_menu.add_command(label='Manage Product', command=manageProducts)
clerk_menu.add_command(label='Sell Product', command=sellProducts)

def histogram():
    pass
def bar():
    pass
def line():
    pass

clerk_menu=Menu(my_menu)
my_menu.add_cascade(label="Analyse", menu=clerk_menu)
clerk_menu.add_command(label='Histogram', command=histogram)
clerk_menu.add_command(label='Bar Diagram', command=bar)
clerk_menu.add_command(label='Line Diagram', command=line)

def manageCashier():
    import managecashier


clerk_menu=Menu(my_menu)
my_menu.add_cascade(label="Cashier", menu=clerk_menu)
clerk_menu.add_command(label='Manage Cashier', command=manageCashier)




root.mainloop()
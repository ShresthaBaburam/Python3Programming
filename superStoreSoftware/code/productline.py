from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()
date = datetime.datetime.now().date()

class ProductLineDiagram:
    def __init__(self,root):
        self.root=root
        self.root.title(" Main Page")
        self.root.geometry("600x300+380+200")
        self.root.config(bg="#021e2f")
        self.root.resizable(False,False)

        #creating a frame

        self.login_frame = Frame(self.root, bg="white")
        self.login_frame.place(x=50, y=50, width=500, height=200)

        options = [
            "Product Name x Number Of Sell",
            "Date Of Sell x Number Of Sell",
            "Product Name x Cost Price(Rs)",
            "Product Name x Maximum Retial Price(Rs)",
            "Product Name x Marked Price(Rs)",
            "Product Name x Selling Price(Rs)",
            "Product Name x Discount(Rs)",

            ]
        self.clicked = StringVar()
        self.clicked.set( "Product Name x Number Of Sell" )

        self.drop = OptionMenu( self.login_frame , self.clicked , *options )
        self.drop.place(x=10,y=10)

        self.generate_btn = Button( self.login_frame ,command=self.generateLineDiagram, text = "Generate" ,bg="white", fg="green", font=("times new roman", 13, "bold"),width=8,  )
        self.generate_btn.place(x=350,y=10)
        
    def generateLineDiagram(self,*argts,**kwargs):
        if self.clicked.get()=="Product Name x Number Of Sell":
            product=[]
            quantity=[]
            sql= "SELECT selling_price,quantity FROM transactions"
            self.result = c.execute(sql).fetchall()
            for r in self.result:
                self.r1=r[0]
                product.append(self.r1)
                self.r2=r[1]
                quantity.append(self.r2)
            conn.commit() 
            plt.plot(product,quantity)
            plt.xlabel("Selling Price")
            plt.ylabel("Number Of sell")
            plt.show()

       
        elif self.clicked=="Quanity x Date Of Sell":
            pass
        elif self.clicked=="Product Name x Cost Price(Rs)":
            pass
        elif self.clicked=="Product Name x Maximum Retial Price(Rs)":
            pass
        elif self.clicked=="Product Name x Marked Price(Rs)":
            pass
        elif self.clicked=="Product Name x Selling Price(Rs)":
            pass
        elif self.clicked=="Product Name x Discount(Rs)":
            pass
        else:
            tkinter.messagebox.showinfo("Error!", "Sorry!\n Incorrect Input..")


root = Tk()
_ProductLineDiagram =ProductLineDiagram(root)
root.mainloop()
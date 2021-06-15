from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime

conn = sqlite3.connect("/home/shresthababu/G62/git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()
res = c.execute("SELECT MAX(product_id) from product_details")
for r in res:
    id=r[0]

date = datetime.datetime.now().date()

class Add:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Add Product Details to Database", font=("arial 40 bold"), fg="steelblue")
        self.heading.place(x=100, y= 10)
        # labals
        self.labal_product_name = Label(master, text="Name of Product", font =("arial 15 bold"))
        self.labal_product_name.place(x = 100, y=100)

        self.labal_number_of_stocks = Label(master, text="Number of Stock", font =("arial 15 bold"))
        self.labal_number_of_stocks.place(x = 100, y=150)

        self.labal_cost_price= Label(master, text="Cost price Per Unit", font =("arial 15 bold"))
        self.labal_cost_price.place(x = 100, y=200)

        self.labal_vender_name = Label(master, text="Vender's Name", font =("arial 15 bold"))
        self.labal_vender_name.place(x = 100, y=250)

        self.labal_venderphone = Label(master, text="Vender's Phone", font =("arial 15 bold"))
        self.labal_venderphone.place(x = 100,y=300)

        self.labal_manufacture_date = Label(master, text="Manufacture Date", font =("arial 15 bold"))
        self.labal_manufacture_date.place(x = 100,y=350)

        self.labal_expiry_date = Label(master, text="Expiry Date", font =("arial 15 bold"))
        self.labal_expiry_date.place(x = 100,y=400)

        self.labal_maximum_retail_price = Label(master, text="Maximum Retail Price", font =("arial 15 bold"))
        self.labal_maximum_retail_price.place(x = 100,y=450)

        self.labal_marked_price = Label(master, text="Marked Price", font =("arial 15 bold"))
        self.labal_marked_price.place(x = 100,y=500)

        self.labal_remarks = Label(master, text="Remarks", font =("arial 15 bold"))
        self.labal_remarks.place(x = 100,y=550)

        #entry
        self.entry_product_name = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_product_name.place(x=350, y=100)

        self.entry_number_of_stocks = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_number_of_stocks.place(x=350, y=150)

        self.entry_cost_price = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_cost_price.place(x=350, y=200)

        self.entry_vender_name = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_vender_name.place(x=350, y=250)

        self.entry_vender_phone = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_vender_phone.place(x=350, y=300)

        self.entry_manufacture_date = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_manufacture_date.place(x=350, y=350)

        self.entry_expiry_date = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_expiry_date.place(x=350, y=400)

        self.entry_maximum_retail_price = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_maximum_retail_price.place(x=350, y=450)

        self.entry_marked_price = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_marked_price.place(x=350, y=500)

        self.entry_remarks = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_remarks.place(x=350, y=550)

        # button
        self.button_add = Button(master, text="Add to Database", font =("arial 13 bold"), width=15, height=1, bg="steelblue", fg="white", command=self.get_items)
        self.button_add.place(x=350,y= 590)


        # text box

        self.textbox_text= Text(master, width=75, height=28)
        self.textbox_text.place(x=650,y=100)

        self.textbox_text.insert(END, "\n Product ID has reached upto:"+ str(id) + " in the database.")


    #get values  from the entry
    def get_items(self,*args,**kwargs):
        self.product_name = self.entry_product_name.get()

        self.number_of_stocks= self.entry_number_of_stocks.get()

        self.cost_price = self.entry_cost_price.get()

        self.vender_name=self.entry_vender_name.get()

        self.vender_phone=self.entry_vender_phone.get()

        self.manufacture_date = self.entry_manufacture_date.get()

        self.expiry_date=self.entry_expiry_date.get()

        self.maximum_retail_price = self.entry_maximum_retail_price.get()

        self.marked_price = self.entry_marked_price.get()
        
        self.remarks = self.entry_remarks.get()
        

        if self.product_name =='' or self.number_of_stocks =='' or self.cost_price=='' or self.vender_name=='' or self.vender_phone=='' or self.manufacture_date=='' or self.expiry_date=='' or self.maximum_retail_price=='' or self.marked_price=='':
            tkinter.messagebox.showinfo("Error!", "Please Fill All Fields\n All Fields are Required") 
       
        else:
            sql="INSERT INTO product_details(product_name,number_of_stocks,cost_price,vender_name,vender_phone,manufacture_date, expiry_date,maximum_retail_price, marked_price,remarks,date) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.product_name,self.number_of_stocks,self.cost_price,self.vender_name,self.vender_phone,self.manufacture_date,self.expiry_date,self.maximum_retail_price,self.marked_price,self.remarks,date))
            conn.commit()

            self.textbox_text.insert(END, "\n Inserted! "+ str(self.product_name) + " into the database")
            tkinter.messagebox.showinfo("Success!", "Successfully!!!\nThe Product Details are \nSaved in Database!!!")
    
           # to clear the fields
            
            self.entry_product_name.delete(0,END)
            self.entry_number_of_stocks.delete(0,END)
            self.entry_cost_price.delete(0,END)
            self.entry_vender_name.delete(0,END)
            self.entry_vender_phone.delete(0,END)
            self.entry_manufacture_date.delete(0,END)
            self.entry_expiry_date.delete(0,END)
            self.entry_maximum_retail_price.delete(0,END)
            self.entry_marked_price.delete(0,END)
            self.entry_remarks.delete(0,END)
            
    

root = Tk()
b = Add(root)
root.geometry("1366x768+0+0")
root.title("Add to the Database")
root.mainloop()

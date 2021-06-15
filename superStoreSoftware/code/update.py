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
class Update:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Update Product Details in Database", font=("arial 40 bold"), fg="steelblue")
        self.heading.place(x=100, y= 10)

        # labals
        self.labal_product_id = Label(master, text="Enter Product ID", font =("arial 15 bold"))
        self.labal_product_id.place(x = 100, y=100)

        self.labal_product_name = Label(master, text="Name of Product", font =("arial 15 bold"))
        self.labal_product_name.place(x = 100, y=150)

        self.labal_number_of_stocks = Label(master, text="Number of Stock", font =("arial 15 bold"))
        self.labal_number_of_stocks.place(x = 100, y=200)

        self.labal_cost_price= Label(master, text="Cost price Per Unit", font =("arial 15 bold"))
        self.labal_cost_price.place(x = 100, y=250)

        self.labal_vender_name = Label(master, text="Vender's Name", font =("arial 15 bold"))
        self.labal_vender_name.place(x = 100, y=300)

        self.labal_venderphone = Label(master, text="Vender's Phone", font =("arial 15 bold"))
        self.labal_venderphone.place(x = 100,y=350)

        self.labal_manufacture_date = Label(master, text="Manufacture Date", font =("arial 15 bold"))
        self.labal_manufacture_date.place(x = 100,y=400)

        self.labal_expiry_date = Label(master, text="Expiry Date", font =("arial 15 bold"))
        self.labal_expiry_date.place(x = 100,y=450)

        self.labal_maximum_retail_price = Label(master, text="Maximum Retail Price", font =("arial 15 bold"))
        self.labal_maximum_retail_price.place(x = 100,y=500)

        self.labal_marked_price = Label(master, text="Marked Price", font =("arial 15 bold"))
        self.labal_marked_price.place(x = 100,y=550)

        self.labal_remarks = Label(master, text="Remarks", font =("arial 15 bold"))
        self.labal_remarks.place(x = 100,y=600)

        #entry
        self.entry_product_id = Entry(master,width= 8, font =("arial 15 bold"))
        self.entry_product_id.place(x=350, y=100)

        self.entry_product_name = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_product_name.place(x=350, y=150)

        self.entry_number_of_stocks = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_number_of_stocks.place(x=350, y=200)

        self.entry_cost_price = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_cost_price.place(x=350, y=250)

        self.entry_vender_name = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_vender_name.place(x=350, y=300)

        self.entry_vender_phone = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_vender_phone.place(x=350, y=350)

        self.entry_manufacture_date = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_manufacture_date.place(x=350, y=400)

        self.entry_expiry_date = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_expiry_date.place(x=350, y=450)

        self.entry_maximum_retail_price = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_maximum_retail_price.place(x=350, y=500)

        self.entry_marked_price = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_marked_price.place(x=350, y=550)

        self.entry_remarks = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_remarks.place(x=350, y=600)

        # button
        self.button_search = Button(master, text="Search", font =("arial 11 bold"), width=11, height=1, bg="steelblue", fg="white", command=self.search_items)
        self.button_search.place(x=460,y= 100)

        self.button_update = Button(master, text="Update to Database", font =("arial 13 bold"), width=15, height=1, bg="steelblue", fg="white", command=self.update_items)
        self.button_update.place(x=350,y= 650)


        # text box

        self.textbox_text= Text(master, width=75, height=31)
        self.textbox_text.place(x=650,y=100)

        self.textbox_text.insert(END, "\n Product ID has reached upto:"+ str(id) + " in the database.")
   
    def search_items(self,*args,**kwargs):
        sql= "SELECT * FROM product_details WHERE product_id=?"
        result = c.execute(sql, (self.entry_product_id.get(),))
            
        for r in result:
            self.r1= r[1]
            self.r2=r[2]
            self.r3=r[3]
            self.r4=r[4]
            self.r5=r[5]
            self.r6=r[6]
            self.r7=r[7]
            self.r8=r[8]
            self.r9=r[9]
            self.r10=r[10]
        conn.commit()

        # deleting previous value and getting  new values to the entry fields

        self.entry_product_name.delete(0,END)
        self.entry_product_name.insert(0,str(self.r1))

        self.entry_number_of_stocks.delete(0,END)
        self.entry_number_of_stocks.insert(0, str(self.r2))

        self.entry_cost_price.delete(0,END)
        self.entry_cost_price.insert(0,str(self.r3))

        self.entry_vender_name.delete(0,END)
        self.entry_vender_name.insert(0,str(self.r4))

        self.entry_vender_phone.delete(0,END)
        self.entry_vender_phone.insert(0,str(self.r5))
        
        self.entry_manufacture_date.delete(0,END)
        self.entry_manufacture_date.insert(0,str(self.r6))

        self.entry_expiry_date.delete(0,END)
        self.entry_expiry_date.insert(0,str(self.r7))

        self.entry_maximum_retail_price.delete(0,END)
        self.entry_maximum_retail_price.insert(0,str(self.r8))

        self.entry_marked_price.delete(0,END)
        self.entry_marked_price.insert(0,str(self.r9))

        self.entry_remarks.delete(0,END)
        self.entry_remarks.insert(0, str(self.r10))


    #get values  from the entry
    def update_items(self,*args,**kwargs):

        self.u1 = self.entry_product_name.get()
        self.u2= self.entry_number_of_stocks.get()
        self.u3 = self.entry_cost_price.get()
        self.u4=self.entry_vender_name.get()
        self.u5=self.entry_vender_phone.get()
        self.u6 = self.entry_manufacture_date.get()
        self.u7=self.entry_expiry_date.get()
        self.u8 = self.entry_maximum_retail_price.get()
        self.u9 = self.entry_marked_price.get()   
        self.u10 = self.entry_remarks.get()
        
        sql = "UPDATE  product_details SET product_name=?,number_of_stocks=?,cost_price=?,vender_name=?,vender_phone=?,manufacture_date=?,expiry_date=?,maximum_retail_price=?,marked_price=?,remarks=?, date =? WHERE product_id=?"
        c.execute(sql, (self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.u7,self.u8,self.u9,self.u10,date, self.entry_product_id.get()))        
        self.textbox_text.insert(END, "\n Updated! "+ str(self.u1) + " into the database")
        tkinter.messagebox.showinfo("Success!", "Successfully!!!\nThe Product Details are\nUpdated in Database!!!")
           
        # to clear the fields
        self.entry_product_id.delete(0,END)
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
b = Update(root)
root.geometry("1366x768+0+0")
root.title("Update to the Database")
root.mainloop()

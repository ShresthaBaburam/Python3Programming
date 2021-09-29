from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
from tkcalendar import Calendar, DateEntry
conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()
res = c.execute("SELECT MAX(product_id) from product_details")
for r in res:
    id=r[0]

date = datetime.datetime.now().date()

class ManageProduct:
    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.heading = Label(master, text="Manage Product Details", font=("arial 30 bold"), fg="steelblue")
        self.heading.place(x=50, y= 10)
        # labals
        self.labal_product_id = Label(master, text="Product Id", font =("arial 15 bold"))
        self.labal_product_id.place(x = 50, y=70)

        self.labal_product_name = Label(master, text="Name of Product", font =("arial 15 bold"))
        self.labal_product_name.place(x = 50, y=120)

        self.labal_number_of_stocks = Label(master, text="Number of Stock", font =("arial 15 bold"))
        self.labal_number_of_stocks.place(x = 50, y=170)

        self.labal_cost_price= Label(master, text="Cost price Per Unit", font =("arial 15 bold"))
        self.labal_cost_price.place(x = 50, y=220)

        self.labal_vender_name = Label(master, text="Vender's Name", font =("arial 15 bold"))
        self.labal_vender_name.place(x = 50, y=270)

        self.labal_venderphone = Label(master, text="Vender's Phone", font =("arial 15 bold"))
        self.labal_venderphone.place(x = 50,y=320)

        self.labal_manufacture_date = Label(master, text="Manufacture Date", font =("arial 15 bold"))
        self.labal_manufacture_date.place(x = 50,y=370)

        self.labal_expiry_date = Label(master, text="Expiry Date", font =("arial 15 bold"))
        self.labal_expiry_date.place(x = 50,y=420)

        self.labal_maximum_retail_price = Label(master, text="Max. Retail Price", font =("arial 15 bold"))
        self.labal_maximum_retail_price.place(x = 50,y=470)

        self.labal_marked_price = Label(master, text="Marked Price", font =("arial 15 bold"))
        self.labal_marked_price.place(x = 50,y=520)

        self.labal_remarks = Label(master, text="Remarks", font =("arial 15 bold"))
        self.labal_remarks.place(x = 50,y=570)

        #entry
        self.entry_product_id = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_product_id.place(x=250, y=70)
        

        self.entry_product_name = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_product_name.place(x=250, y=120)

        self.entry_number_of_stocks = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_number_of_stocks.place(x=250, y=170)

        self.entry_cost_price = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_cost_price.place(x=250, y=220)

        self.entry_vender_name = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_vender_name.place(x=250, y=270)

        self.entry_vender_phone = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_vender_phone.place(x=250, y=320)

        self.entry_manufacture_date = DateEntry(master,width= 20, font =("arial 15 bold"))
        self.entry_manufacture_date.place(x=250, y=370)

        self.entry_expiry_date = DateEntry(master,width= 20, font =("arial 15 bold"))
        self.entry_expiry_date.place(x=250, y=420)

        self.entry_maximum_retail_price = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_maximum_retail_price.place(x=250, y=470)

        self.entry_marked_price = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_marked_price.place(x=250, y=520)

        self.entry_remarks = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_remarks.place(x=250, y=570)

        # button
        self.button_add = Button(master, text="Add", font =("arial 13 bold"), width=8, height=1, bg="steelblue", fg="white", command=self.addProduct)
        self.button_add.place(x=50,y= 640)

        self.button_add = Button(master, text="Search", font =("arial 13 bold"), width=8, height=1, bg="steelblue", fg="white", command=self.searchProduct)
        self.button_add.place(x=155,y= 640)

        self.button_add = Button(master, text="Update", font =("arial 13 bold"), width=8, height=1, bg="steelblue", fg="white", command=self.updateProduct)
        self.button_add.place(x=260,y= 640)

        self.button_add = Button(master, text="Delete", font =("arial 13 bold"), width=8, height=1, bg="steelblue", fg="white", command=self.deleteProduct)
        self.button_add.place(x=365,y= 640)

    #table for tha detail view of the propduct
        self.table_frame = Frame(master, width=820, height=490, bg="steelblue")
        self.table_frame.place(x=500,y=50)

        self.labal_id = Label(self.table_frame,text=("Product Id"), font=("arial 15 bold"), bg="steelblue", fg="black" )
        self.labal_id.place(x=40,y=12)

        self.entry_id = Entry(self.table_frame, width="10",font=("arial 15 bold"), bg="lightblue", fg="black" )
        self.entry_id.place(x=150,y=10)

        self.btn_show_detail= Button(self.table_frame, text=" Show",width ="7",height=1,font=("arial 12 bold"),bg="green", fg="black", command=self.show_detail)
        self.btn_show_detail.place(x=300,y=10)

        self.btn_show_detailAll= Button(self.table_frame, text=" Show All",width ="7",height=1,font=("arial 12 bold"),bg="green", fg="black",command=self.show_detailAll)
        self.btn_show_detailAll.place(x=430,y=10)

        self.labal_date_today= Label(self.table_frame, text= "Today's Date:"+ str(date), font=(" arial 14 bold"), bg="steelblue", fg="black")        
        self.labal_date_today.place(x=600, y=20)

        self.trv_frame = Frame(master, width=800, height=420, bg="grey")
        self.trv_frame.place(x=510,y=100)

        

        self.horizontalScrollbar = ttk.Scrollbar(self.trv_frame,orient='horizontal')
        self.verticalScrollbar = ttk.Scrollbar(self.trv_frame,orient='vertical')

        self.trv = ttk.Treeview(self.trv_frame,height="20",xscrollcommand=self.horizontalScrollbar,yscrollcommand=self.verticalScrollbar)
        self.trv.place(x=20,y=50)
        self.trv['columns']=('Id','Product','Stocks','CostPrice','Vender','Phone','Mfd.Date','Exp.Date','Max.Ret.Price','MarkedPrice','Remarks','AddedOn','ModifiedOn')
        

        self.horizontalScrollbar.pack(fill = X, side=BOTTOM)
        self.verticalScrollbar.pack(fill = BOTH, side=RIGHT)
        self.horizontalScrollbar.configure(command=self.trv.xview)
        self.verticalScrollbar.configure(command=self.trv.yview)

        self.trv['show']= 'headings'
        self.trv.column('Id',width=30,minwidth=20,anchor=tk.CENTER)
        self.trv.column('Product',width=90,minwidth=80,anchor=tk.CENTER)
        self.trv.column('Stocks',width=50,minwidth=40,anchor=tk.CENTER)
        self.trv.column('CostPrice',width=40,minwidth=40,anchor=tk.CENTER)
        self.trv.column('Vender',width=50,minwidth=70,anchor=tk.CENTER)
        self.trv.column('Phone',width=70,minwidth=70,anchor=tk.CENTER)
        self.trv.column('Mfd.Date',width=70,minwidth=70,anchor=tk.CENTER)
        self.trv.column('Exp.Date',width=70,minwidth=70,anchor=tk.CENTER)
        self.trv.column('Max.Ret.Price',width=60,minwidth=60,anchor=tk.CENTER)
        self.trv.column('MarkedPrice',width=40,minwidth=40,anchor=tk.CENTER)
        self.trv.column('Remarks',width=80,minwidth=60,anchor=tk.CENTER)
        self.trv.column('AddedOn',width=50,minwidth=50,anchor=tk.CENTER)
        self.trv.column('ModifiedOn',width=80,minwidth=70,anchor=tk.CENTER)

        self.trv.heading('Id',text='Id',anchor=tk.CENTER)
        self.trv.heading('Product',text='Product',anchor=tk.CENTER)
        self.trv.heading('Stocks',text='Stock',anchor=tk.CENTER)
        self.trv.heading('CostPrice',text='C.P.',anchor=tk.CENTER)
        self.trv.heading('Vender',text='Vender',anchor=tk.CENTER)
        self.trv.heading('Phone',text='V.Phone',anchor=tk.CENTER)
        self.trv.heading('Mfd.Date',text='Mfd.Date',anchor=tk.CENTER)
        self.trv.heading('Exp.Date',text='Exp.Date',anchor=tk.CENTER)
        self.trv.heading('Max.Ret.Price',text='M.R.P.',anchor=tk.CENTER)
        self.trv.heading('MarkedPrice',text='M.P.',anchor=tk.CENTER)
        self.trv.heading('Remarks',text='Remarks.',anchor=tk.CENTER)
        self.trv.heading('AddedOn',text='AddedOn',anchor=tk.CENTER)
        self.trv.heading('ModifiedOn',text='ModifiedOn',anchor=tk.CENTER)
        self.trv.pack(fill=BOTH)
        self.show_detailAll()

         # text box
        self.textbox_text= Text(master, width=102, height=7)
        self.textbox_text.place(x=500,y=550)

        self.textbox_text.insert(END, "Product ID has reached upto:"+ str(id) + " in the database.\n")

    #get values  from the entry
    def addProduct(self,*args,**kwargs):
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
        
        if self.product_name !='' and self.number_of_stocks !='' and self.cost_price!='' and self.vender_name!='' and self.vender_phone!='' and self.manufacture_date!='' and self.expiry_date!='' and self.maximum_retail_price!='' and self.marked_price!='':
            sql="INSERT INTO product_details(product_name,number_of_stocks,cost_price,vender_name,vender_phone,manufacture_date, expiry_date,maximum_retail_price, marked_price,remarks,added_date) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.product_name,self.number_of_stocks,self.cost_price,self.vender_name,self.vender_phone,self.manufacture_date,self.expiry_date,self.maximum_retail_price,self.marked_price,self.remarks,date))
            conn.commit()

            self.textbox_text.insert(END, "\n Inserted! "+ str(self.product_name) + " into the database")
            tkinter.messagebox.showinfo("Success!", "Successfully!!!\nThe Product Details are \nSaved in Database!!!")
        else:
            tkinter.messagebox.showinfo("Error!", "Please Fill All Fields\n All Fields are Required")
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

    def searchProduct(self,*args,**kwargs):
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

        sql= "SELECT product_id FROM product_details"
        self.result = c.execute(sql).fetchall()
        if self.entry_product_id.get() !='' and [self.result for self.result in self.result if self.result[0]==int(self.entry_product_id.get())]:
            sql= "SELECT * FROM product_details WHERE product_id=?"
            result = c.execute(sql, (self.entry_product_id.get()),)
            for r in result:
                self.r1=r[1]
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
            self.textbox_text.insert(END, "\n Searched!,\tProduct with id "+ self.entry_product_id.get() + " in the database")
        else:
            self.entry_product_id.delete(0,END)
            tkinter.messagebox.showinfo("Error!","Wrong Product Id Format.\nProduct Id Format:Number.\nEnter  Correct Product Id.") 
        
            

    #get values  from the entry

    def updateProduct(self,*args,**kwargs):
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
        if self.product_name !='' and self.number_of_stocks !='' and self.cost_price!='' and self.vender_name!='' and self.vender_phone!='' and self.manufacture_date!='' and self.expiry_date!='' and self.maximum_retail_price!='' and self.marked_price!='':
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
            
            sql = "UPDATE  product_details SET product_name=?,number_of_stocks=?,cost_price=?,vender_name=?,vender_phone=?,manufacture_date=?,expiry_date=?,maximum_retail_price=?,marked_price=?,remarks=?, modified_date =? WHERE product_id=?"
            c.execute(sql, (self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.u7,self.u8,self.u9,self.u10,date, self.entry_product_id.get()))        
            self.textbox_text.insert(END, "\n Updated!, "+ str(self.u1) + " into the database")
            tkinter.messagebox.showinfo("Success!", "Successfully!!!\nThe Product Details are\nUpdated in Database!!!")
            conn.commit()

            

        else:
            tkinter.messagebox.showinfo("Error!", "Product Before Updating.\nProduct Searching Required.")
        
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


        # to delete the product delete
    def deleteProduct(self,*args,**kwargs):
        sql= "SELECT product_id FROM product_details"
        self.result = c.execute(sql).fetchall()

        if self.entry_product_id.get() !='' and [self.result for self.result in self.result if self.result[0]==int(self.entry_product_id.get())]:
            sql = "DELETE FROM  product_details WHERE product_id=?"
            c.execute(sql, (self.entry_product_id.get(),))        
            self.textbox_text.insert(END, "\n Deleted!\tproduct with id "+ self.entry_product_id.get() + " from the database")
            tkinter.messagebox.showinfo("Success!,", "Successfully!!!\nThe Product Details are\nDeleted form Database!!!")
            conn.commit()

        else:
            tkinter.messagebox.showinfo("Error!", "Product Before Deleting.\nProduct Searching Required.")
            
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
        
    def show_detail(self,*argts,**kwargs):
        self.get_id = self.entry_id.get()
        sql = "SELECT * FROM product_details WHERE  product_id=? "
        c.execute(sql,(self.get_id,))
        self.rows=c.fetchall()
        self.trv.delete(*self.trv.get_children())
        if len(self.rows)!=0:

            self.i =0
            for row in self.rows:
                if row[2] < 5:
                    self.trv.insert('',self.i,text='',values=(row[0],row[1]+('(!)'),row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
                self.i+=1
            else:
                tkinter.messagebox.showinfo("Error!", "No Such Product Found in database.\nEnter correct product_id...")

        conn.commit()

    def show_detailAll(self,*argts,**kwargs):
        self.entry_id.delete(0,END)
        sql = "SELECT * FROM product_details "
        c.execute(sql)
        self.rows=c.fetchall()
        self.trv.delete(*self.trv.get_children())
        if len(self.rows)!=0:
            
            self.i =0
            for row in self.rows:

                if row[2] < 5:
                    self.trv.insert('',self.i,text='',values=(row[0],row[1]+('(!)'),row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
                else:
                    self.trv.insert('',self.i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
                self.i+=1
            
        conn.commit()

    
root = Tk()
_ManageProduct = ManageProduct(root)
root.geometry("1356x768+0+0")
root.title("Add to the Database")
root.resizable(False,False)
root.mainloop()

from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
import os
import random
import math


pid=[]
pname=[]
pdiscount=[]
prate=[]
pquantity=[]
pamount=[]
product_list=[]



conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()

date = datetime.datetime.now().date()

class Application:
    def __init__(self,master,*args,**kwargs):
        self.master  = master

        self.heading = Label(master, text="ABC Super Store", font=("arial 30 bold"), fg="steelblue")
        self.heading.place(x=500, y= 10)

        #frames
        # left frame  to search anda  entry product details
        self.left_frame = Frame(master, width=350, height=600, bg="lightblue")
        self.left_frame.pack(side=LEFT,)
        self.left_frame.place(x=30,y=75)

        # middle frame for detailsview
        self.middle_frame = Frame(master, width=570, height=600, bg="grey")
        self.middle_frame.pack(side=RIGHT )
        self.middle_frame.place(x=390,y=75)


        # right frame to show bill
        self.right_frame = Frame(master, width=370, height=600, bg="lightblue")
        self.right_frame.pack(side=RIGHT )
        self.right_frame.place(x=970,y=75)

        # for left frame
        self.heading = Label(self.left_frame, text="Search for the product", font=("arial 20 bold"), bg="lightblue",fg="steelblue")
        self.heading.place(x=5, y= 20)

        self.labal_product_id = Label(self.left_frame,text=("Enter Product Id"), font=("arial 15 bold"), bg="lightblue", fg="black" )
        self.labal_product_id.place(x=10,y=70)

        self.entry_product_id = Entry(self.left_frame, width ="7",font=("arial 15 bold"),bg="white", fg="black")
        self.entry_product_id.place(x=150,y=70)

        self.btn_search= Button(self.left_frame, text=" Search",width ="7",height=1,font=("arial 12 bold"),bg="green", fg="black", command=self.see_details)
        self.btn_search.place(x=250,y=70)


        #getting details after calling the function
        self.labal_product_name = Label(self.left_frame,text=(""), font=("arial 15 bold"), bg="lightblue", fg="black" )
        self.labal_product_name.place(x=10,y=150)

        self.labal_number_of_stocks = Label(self.left_frame,text=(""), font=("arial 15 bold"), bg="lightblue", fg="black" )
        self.labal_number_of_stocks.place(x=10,y=200)

        self.labal_marked_price = Label(self.left_frame,text=(""), font=("arial 15 bold"), bg="lightblue", fg="black" )
        self.labal_marked_price.place(x=10,y=250)


        self.labal_change_amount = Label(self.left_frame,text="", font=("arial 13 bold"), bg="lightblue", fg="black" )
        self.labal_change_amount.place(x=10,y=470)

        # for middle frame 

        self.table_frame = Frame(master, width=550, height=530, bg="white")
        self.table_frame.place(x=400,y=130)

        

        self.labal_id = Label(self.middle_frame,text=("Product Id"), font=("arial 15 bold"), bg="grey", fg="black" )
        self.labal_id.place(x=10,y=10)

        self.entry_id = Entry(self.middle_frame, width="10",font=("arial 15 bold"), bg="lightblue", fg="black" )
        self.entry_id.place(x=150,y=10)

        self.btn_show_detail= Button(self.middle_frame, text=" Show",width ="7",height=1,font=("arial 12 bold"),bg="green", fg="black", command=self.show_detail)
        self.btn_show_detail.place(x=300,y=10)

        self.btn_show_detailAll= Button(self.middle_frame, text=" Show All",width ="7",height=1,font=("arial 12 bold"),bg="green", fg="black",command=self.show_detailAll)
        self.btn_show_detailAll.place(x=450,y=10)

        

        self.horizontalScrollbar = ttk.Scrollbar(self.table_frame,orient='horizontal')
        self.verticalScrollbar = ttk.Scrollbar(self.table_frame,orient='vertical')

        self.trv = ttk.Treeview(self.table_frame,height="25",xscrollcommand=self.horizontalScrollbar,yscrollcommand=self.verticalScrollbar)

        self.trv['columns']=('Id','Product','Stocks','CostPrice','Mfd.Date','Exp.Date','Max.Ret.Price','MarkedPrice')
        

        self.horizontalScrollbar.pack(fill = X, side=BOTTOM)
        self.verticalScrollbar.pack(fill = BOTH, side=RIGHT)
        self.horizontalScrollbar.configure(command=self.trv.xview)
        self.verticalScrollbar.configure(command=self.trv.yview)

        self.trv['show']= 'headings'
        self.trv.column('Id',width=20,minwidth=20,anchor=tk.CENTER)
        self.trv.column('Product',width=125,minwidth=100,anchor=tk.CENTER)
        self.trv.column('Stocks',width=50,minwidth=50,anchor=tk.CENTER)
        self.trv.column('CostPrice',width=60,minwidth=50,anchor=tk.CENTER)
        self.trv.column('Mfd.Date',width=80,minwidth=70,anchor=tk.CENTER)
        self.trv.column('Exp.Date',width=80,minwidth=70,anchor=tk.CENTER)
        self.trv.column('Max.Ret.Price',width=60,minwidth=60,anchor=tk.CENTER)
        self.trv.column('MarkedPrice',width=60,minwidth=60,anchor=tk.CENTER)


        self.trv.heading('Id',text='Id',anchor=tk.CENTER)
        self.trv.heading('Product',text='Product',anchor=tk.CENTER)
        self.trv.heading('Stocks',text='Stock',anchor=tk.CENTER)
        self.trv.heading('CostPrice',text='C.P.',anchor=tk.CENTER)
        self.trv.heading('Mfd.Date',text='Mfd.Date',anchor=tk.CENTER)
        self.trv.heading('Exp.Date',text='Exp.Date',anchor=tk.CENTER)
        self.trv.heading('Max.Ret.Price',text='M.R.P.',anchor=tk.CENTER)
        self.trv.heading('MarkedPrice',text='M.P.',anchor=tk.CENTER)
        self.trv.pack(fill=BOTH)
        self.show_detailAll()
        
        # for the right frame
        self.labal_date_today= Label(self.right_frame, text= "Today's Date:"+ str(date), font=(" arial 10 bold"), bg="lightblue", fg="black")        
        self.labal_date_today.place(x=200, y=10)


        self.tab_product = Label(self.right_frame, text= "Products",font=(" arial 11 bold"), bg="lightblue", fg="black")
        self.tab_product.place(x=20,y=50)

        self.tab_rate = Label(self.right_frame, text= "Rate",font=(" arial 11 bold"), bg="lightblue", fg="black")
        self.tab_rate.place(x=160,y=50)

        self.tab_quantity = Label(self.right_frame, text= "Quantity",font=(" arial 11 bold"), bg="lightblue", fg="black")
        self.tab_quantity.place(x=230,y=50)

        self.tab_amount = Label(self.right_frame, text= "Amount",font=(" arial 11 bold"), bg="lightblue", fg="black")
        self.tab_amount.place(x=310,y=50)



        self.labal_total_bill = Label(self.right_frame,text=(""), font=("arial 11 bold"), bg="lightgrey", fg="black" )
        self.labal_total_bill.place(x=190,y=450)



    def see_details(self,*args, **kwargs):
        

        self.get_id = self.entry_product_id.get()
        # getting the value from the data base nad filling the labal
        sql = "SELECT  product_id, product_name, number_of_stocks, marked_price FROM product_details WHERE  product_id=?"
        result = c.execute(sql,(self.get_id,))

        for self.r in result:
            if self.r[2]>0:
                self.get_product_id= self.r[0]
                self.get_product_name= self.r[1]
                self.get_number_of_stocks= self.r[2]
                self.get_marked_price= self.r[3]


            else:
                tkinter.messagebox.showinfo("Error!","Sorry!\nWe have no such Product...")


            self.labal_product_name.configure(text="Product Name:"+ str(self.get_product_name))
            self.labal_number_of_stocks.configure(text="Number of Stocks:"+ str(self.get_number_of_stocks))
            self.labal_marked_price.configure(text="Marked Price:"+ str(self.get_marked_price))

        # to enter the details of the product to sell.
        self.labal_quantity = Label(self.left_frame,text=("Quantity of Product"), font=("arial 13 bold"), bg="lightblue", fg="black" )
        self.labal_quantity.place(x=10,y=300)
        self.entry_quantity = Entry(self.left_frame, width ="10",font=("arial 15 bold"),bg="white", fg="black")
        self.entry_quantity.place(x=225,y=300)
        self.entry_quantity.focus()

        self.labal_discount = Label(self.left_frame,text=("Discount Amount"), font=("arial 13 bold"), bg="lightblue", fg="black" )
        self.labal_discount.place(x=10,y=340)
        self.entry_discount = Entry(self.left_frame, width ="10",font=("arial 15 bold"),bg="white", fg="black")
        self.entry_discount.place(x=225,y=340)
        self.entry_discount.insert(END,0)

        # to add to bill
        self.btn_add_to_cart= Button(self.left_frame, text=" Add to Cart",width ="11",height=1,font=("arial 11 bold"),bg="green", fg="black", command=self.add_to_cart)
        self.btn_add_to_cart.place(x=225,y=380)

        # for the amount change
        self.labal_given_amount = Label(self.left_frame,text=("Given Amount"), font=("arial 13 bold"), bg="lightblue", fg="black" )
        self.labal_given_amount.place(x=10,y=420)
        self.entry_given_amount = Entry(self.left_frame, width ="8",font=("arial 15 bold"),bg="white", fg="black")
        self.entry_given_amount.place(x=150,y=420)

        self.btn_make_change= Button(self.left_frame, text=" Change",width ="7",height=1,font=("arial 11 bold"),bg="yellow", fg="black", command=self.change)
        self.btn_make_change.place(x=255,y=420)

        # to generate the bill
        self.btn_generate_bill= Button(self.left_frame, text=" Generate Bill",width ="25",height=2,font=("arial 15 bold"),bg="red", fg="black", command=self.generate_bill)
        self.btn_generate_bill.place(x=25,y=520)

    def add_to_cart(self, *args, **kwargs):
        
        if int(self.entry_discount.get())>0:
            self.get_marked_price -=int(self.entry_discount.get())

        self.quantity = int(self.entry_quantity.get())
        
        if self.quantity > int(self.get_number_of_stocks):
           tkinter.messagebox.showinfo("Error!"," We have only limited Products.\n Number of" + str(self.get_product_name)+ " is "+ str(self.get_number_of_stocks))
        else:
            pid.append(self.get_product_id)
            pname.append(self.get_product_name)
            pdiscount.append(self.entry_discount.get())
            prate.append(self.get_marked_price)
            pquantity.append(self.entry_quantity.get())
            amount= int(self.entry_quantity.get()) * int(self.get_marked_price)
            pamount.append(amount)
            self.xin=20
            self.yin=70
            self.coun =0
            self.total_amount=0

            for self.p in pname:
                self.tempname= Label(self.right_frame, text=str(pname[self.coun]), font=("arial 10 bold"), bg="lightgreen", fg="black")
                self.tempname.place(x=20, y= self.yin)
                product_list.append(self.tempname)

                self.temprate= Label(self.right_frame, text=str(prate[self.coun]), font=("arial 10 bold"), bg="lightgreen", fg="black")
                self.temprate.place(x=160, y= self.yin)
                product_list.append(self.temprate)

                self.tempquantity= Label(self.right_frame, text=str(pquantity[self.coun]), font=("arial 10 bold"), bg="lightgreen", fg="black")
                self.tempquantity.place(x=230, y= self.yin)
                product_list.append(self.tempquantity)

                self.tempamount= Label(self.right_frame, text=str(pamount[self.coun]), font=("arial 10 bold"), bg="lightgreen", fg="black")
                self.tempamount.place(x=310, y= self.yin)
                product_list.append(self.tempamount)
    
                self.total_amount += pamount[self.coun]
                self.labal_total_bill.configure(text="Your Total Bill: Rs."+ str(self.total_amount))

                self.yin+=20
                self.coun +=1

            self.labal_product_name.configure(text="")
            self.labal_number_of_stocks.configure(text="")
            self.labal_marked_price.configure(text="")

            self.labal_quantity.place_forget()
            self.entry_quantity.place_forget()

            self.labal_discount.place_forget()
            self.entry_discount.place_forget()

            self.btn_add_to_cart.destroy()

            self.entry_product_id.focus()
            self.entry_product_id.delete(0,END)



    def change(self, *args, **kwargs):
        self.bill_given_amount= float(self.entry_given_amount.get())
        self.bill_total_amount = float(self.total_amount) 
        
        if  self.bill_total_amount <= self.bill_given_amount:
            self.bill_change_amount = float(self.bill_given_amount- self.bill_total_amount)
            self.labal_change_amount.configure(text=" Your Change Amount:"+str(self.bill_change_amount))

        elif self.bill_total_amount > self.bill_given_amount:
            self.bill_change_amount = self.bill_total_amount-float(self.bill_given_amount)
            self.entry_given_amount.focus()
            self.entry_given_amount.delete(0,END)
            tkinter.messagebox.showinfo("Error!","The Given Amount is insufficient.\n Rs." + str(self.bill_change_amount)+ " is Required!")
        else:
            self.entry_given_amount.focus()
            self.entry_given_amount.delete(0,END)
            tkinter.messagebox.showinfo("Error!","The Given Amount is insufficient.\n Or \n More Amount is Required!  ")
   
    def generate_bill(self, *args, **kwargs):
        
        # create the bill before updating the database
        directory ="/home/babucode/Git/Python3-Programming/superStoreSoftware/bill/bill_"+str(date)+".docx"
        if os.path.exists(directory):
            os.makedirs(directory)
        
        # tempalte for the bill
        comapny = "\n\t\t\t\t\tABC Super Store \n"
        address = "\t\t\t\t\tKathmandu-19, Nepal\n"
        phone =   "\t\t\t\t\tPhone:015161741\n"
        sample =  "\t\t\t\t\tInvoice\n"
        dt=       "\t\t\t\t\t"+str(date)

        table_header = "\n\n\t---------------------------------------------------------------------------\n\tS.n.\tProduct name\t\t Rate\t\tQuantity\tAmount\n\t---------------------------------------------------------------------------"
        final = comapny+address+phone+sample+dt+"\n"+table_header

        file_name =str(directory)+str(random.randrange(5000,10000))

        f = open(file_name,'w')

        f.write(final)
        r = 0
        for t in pname:
            f.write("\n\t"+str(r+1)+"\t"+str(pname[r][:10])+"\t\t"+str(prate[r])+"\t\t"+str(pquantity[r])+"\t\t"+str(pamount[r]))
            r+=1
        f.write("\n\t---------------------------------------------------------------------------\n\t\t\t\t\t\tYour Total bill is Rs."+ str(sum(pamount)))
        f.write("\n\t\tThank you! for visiting Us.........\t\tUser:")
        # os.startfile(file_name, "print")
        f.close()

        # to make change quantity
        self.x=0
        sql= "SELECT * FROM product_details WHERE product_id=?"
        result=c.execute(sql,(pid[self.x],))
        for i in pname:
            
            for r in result:
                self.old_stock = r[2]
            
            self.new_stock= int(self.old_stock)-int(pquantity[self.x])
            sql = "UPDATE product_details SET number_of_stocks=? WHERE product_id=?"
            c.execute(sql,(self.new_stock,pid[self.x]))
            conn.commit()
            

            sql2 = "INSERT INTO transactions (product_id, product_name,discount,selling_price,quantity, amount, date) VALUES (?,?,?,?,?,?,?)"
            c.execute(sql2,(pid[self.x],pname[self.x],pdiscount[self.x],prate[self.x], pquantity[self.x],pamount[self.x],date))
            conn.commit()

            self.x+=1

        for a in product_list:
            a.destroy()
        
        del(pid[:])
        del(pname[:])
        del(pdiscount[:])
        del(prate[:])
        del(pquantity[:])
        del(pamount[:])
        self.labal_total_bill.configure(text="")
        self.entry_given_amount.delete(0,END)
        self.labal_change_amount.configure(text="")
        del self.total_amount
        
        tkinter.messagebox.showinfo("Success","Done!\nCompletelly...")

    def show_detail(self, *args, **kwargs):
        self.get_id = self.entry_id.get()
        # getting the value from the data base nad filling the labal
        sql = "SELECT  product_id, product_name, number_of_stocks,cost_price, manufacture_date,expiry_date,maximum_retail_price, marked_price,remarks FROM product_details WHERE  product_id=?"

        c.execute(sql,(self.get_id,))
        
        self.rows=c.fetchall()
        if len(self.rows)!=0:
            self.trv.delete(*self.trv.get_children())
            self.i =0
            for row in self.rows:
            
                self.trv.insert('',self.i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
                self.i+=1
        self.entry_id.delete(0,END)

    def show_detailAll(self, *args, **kwargs):

        sql = "SELECT  product_id, product_name, number_of_stocks,cost_price, manufacture_date,expiry_date,maximum_retail_price, marked_price,remarks FROM product_details "
        c.execute(sql)
        self.rows=c.fetchall()
        
        
        if len(self.rows)!=0:
            self.trv.delete(*self.trv.get_children())
            self.i =0
            for row in self.rows:
            
                self.trv.insert('',self.i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
                self.i+=1
        conn.commit()
        
        
          


root = Tk()
b = Application(root)
root.geometry("1356x768+0+0")
root.title("Sell Product Page")
root.resizable(False,False)
root.mainloop()


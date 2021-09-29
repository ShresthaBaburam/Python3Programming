from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
from tkcalendar import Calendar, DateEntry
conn = sqlite3.connect("/home/babucode/Git/Python3-Programming/superStoreSoftware/database/store.db")
c = conn.cursor()
res = c.execute("SELECT MAX(cashier_id) FROM cashier")
for r in res:
    id=r[0]

date = datetime.datetime.now().date()

class CashierRegistration:
    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.heading = Label(master, text="Manage Cashier Details", font=("arial 30 bold"), fg="steelblue")
        self.heading.place(x=50, y= 10)

        # labals and entries
        self.labal_cashier_id = Label(master, text="Cashier Id", font =("arial 15 bold"))
        self.labal_cashier_id.place(x = 50, y=70)
        self.entry_cashier_id = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_cashier_id.place(x=250, y=70)

        self.labal_cashier_name = Label(master, text="Cashier Name", font =("arial 15 bold"))
        self.labal_cashier_name.place(x = 50, y=120)
        self.entry_cashier_name = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_cashier_name.place(x=250, y=120)

        self.labal_cashier_username = Label(master, text="Cashier Username", font =("arial 15 bold"))
        self.labal_cashier_username.place(x = 50, y=170)
        self.entry_cashier_username = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_cashier_username.place(x=250, y=170)

        self.labal_cashier_password= Label(master, text="Cashier Password", font =("arial 15 bold"))
        self.labal_cashier_password.place(x = 50, y=220)
        self.entry_cashier_password = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_cashier_password.place(x=250, y=220)

        self.labal_cashier_dob = Label(master, text="Cashier DoB:", font =("arial 15 bold"))
        self.labal_cashier_dob.place(x = 50, y=270)
        self.entry_cashier_dob = DateEntry(master,width= 20, font =("arial 15 bold"))
        self.entry_cashier_dob.place(x=250, y=270)

        self.labal_cashier_address = Label(master, text="Cashier Address:", font =("arial 15 bold"))
        self.labal_cashier_address.place(x = 50, y=320)
        self.entry_cashier_address = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_cashier_address.place(x=250, y=320)

        self.labal_cashier_phone = Label(master, text="Cashier Phone", font =("arial 15 bold"))
        self.labal_cashier_phone.place(x = 50,y=370)
        self.entry_cashier_phone = Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_cashier_phone.place(x=250, y=370)

        self.labal_cashier_email = Label(master, text="Cashier Email:", font =("arial 15 bold"))
        self.labal_cashier_email.place(x = 50,y=420)
        self.entry_cashier_email= Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_cashier_email.place(x=250, y=420)

        self.labal_cashier_remarks = Label(master, text="Remarks:", font =("arial 15 bold"))
        self.labal_cashier_remarks.place(x = 50,y=470)
        self.entry_cashier_remarks= Entry(master,width= 20, font =("arial 15 bold"))
        self.entry_cashier_remarks.place(x=250, y=470)
        


        # button
        self.button_add = Button(master, text="Add",command=self.addCashier, font =("arial 13 bold"), width=8, height=1, bg="steelblue", fg="white", )
        self.button_add.place(x=50,y= 510)

        self.button_search = Button(master, text="Search",command=self.searchCashier, font =("arial 13 bold"), width=8, height=1, bg="steelblue", fg="white",)
        self.button_search.place(x=155,y= 510)

        self.button_update = Button(master, text="Update",command=self.updateCashier, font =("arial 13 bold"), width=8, height=1, bg="steelblue", fg="white", )
        self.button_update.place(x=260,y= 510)

        self.button_delete = Button(master, text="Delete",command=self.deleteCashier, font =("arial 13 bold"), width=8, height=1, bg="steelblue", fg="white", )
        self.button_delete.place(x=365,y= 510)

    #table for tha detail view of the propduct
        self.table_frame = Frame(master, width=820, height=490, bg="steelblue")
        self.table_frame.place(x=500,y=50)

        self.labal_id = Label(self.table_frame,text=("Cashier Id"), font=("arial 15 bold"), bg="steelblue", fg="black" )
        self.labal_id.place(x=40,y=12)

        self.entry_cash_id = Entry(self.table_frame, width="10",font=("arial 15 bold"), bg="lightblue", fg="black" )
        self.entry_cash_id.place(x=150,y=10)

        self.btn_show_detail= Button(self.table_frame, command=self.cashierDetail,text=" Show",width ="7",height=1,font=("arial 12 bold"),bg="green", fg="black", )
        self.btn_show_detail.place(x=300,y=10)

        self.btn_show_detailAll= Button(self.table_frame,command=self.cashierDetailAll, text=" Show All",width ="7",height=1,font=("arial 12 bold"),bg="green", fg="black",)
        self.btn_show_detailAll.place(x=430,y=10)

        self.labal_date_today= Label(self.table_frame, text= "Today's Date:"+ str(date), font=(" arial 14 bold"), bg="steelblue", fg="black")        
        self.labal_date_today.place(x=600, y=20)

        self.trv_frame = Frame(master, width=800, height=420, bg="grey")
        self.trv_frame.place(x=510,y=100)

        

        self.horizontalScrollbar = ttk.Scrollbar(self.trv_frame,orient='horizontal')
        self.verticalScrollbar = ttk.Scrollbar(self.trv_frame,orient='vertical')

        self.trv = ttk.Treeview(self.trv_frame,height="20",xscrollcommand=self.horizontalScrollbar,yscrollcommand=self.verticalScrollbar)
        self.trv.place(x=20,y=50)
        self.trv['columns']=('Id','Name','Username','Password','BirthDate','Address','Phone','Email','Remarks','AddedOn','ModifiedOn')
        

        self.horizontalScrollbar.pack(fill = X, side=BOTTOM)
        self.verticalScrollbar.pack(fill = BOTH, side=RIGHT)
        self.horizontalScrollbar.configure(command=self.trv.xview)
        self.verticalScrollbar.configure(command=self.trv.yview)

        self.trv['show']= 'headings'
        self.trv.column('Id',width=30,minwidth=20,anchor=tk.CENTER)
        self.trv.column('Name',width=70,minwidth=70,anchor=tk.CENTER)
        self.trv.column('Username',width=80,minwidth=50,anchor=tk.CENTER)
        self.trv.column('Password',width=80,minwidth=50,anchor=tk.CENTER)
        self.trv.column('BirthDate',width=80,minwidth=70,anchor=tk.CENTER)
        self.trv.column('Address',width=80,minwidth=70,anchor=tk.CENTER)
        self.trv.column('Phone',width=50,minwidth=40,anchor=tk.CENTER)
        self.trv.column('Email',width=60,minwidth=60,anchor=tk.CENTER)
        self.trv.column('Remarks',width=80,minwidth=60,anchor=tk.CENTER)
        self.trv.column('AddedOn',width=80,minwidth=60,anchor=tk.CENTER)
        self.trv.column('ModifiedOn',width=90,minwidth=60,anchor=tk.CENTER)

        self.trv.heading('Id',text='Id',anchor=tk.CENTER)
        self.trv.heading('Name',text='Name',anchor=tk.CENTER)
        self.trv.heading('Username',text='Username',anchor=tk.CENTER)
        self.trv.heading('Password',text='Password',anchor=tk.CENTER)
        self.trv.heading('BirthDate',text='Birth Date ',anchor=tk.CENTER)
        self.trv.heading('Address',text='Address',anchor=tk.CENTER)
        self.trv.heading('Phone',text='Phone',anchor=tk.CENTER)
        self.trv.heading('Email',text='Email',anchor=tk.CENTER)
        self.trv.heading('Remarks',text='Remarks',anchor=tk.CENTER)
        self.trv.heading('AddedOn',text='AddedOn',anchor=tk.CENTER)
        self.trv.heading('ModifiedOn',text='ModifiedOn.',anchor=tk.CENTER)
        self.trv.pack(fill=BOTH)
        self.cashierDetailAll()
    
                 # text box
        self.textbox_text= Text(master, width=102, height=7)
        self.textbox_text.place(x=500,y=550)

        self.textbox_text.insert(END, "Cashier ID has reached upto:"+ str(id) + " in the database.\n")

    def cashierDetail(self,*args,**kwargs):
        self.get_id = self.entry_cash_id.get()
        sql = "SELECT * FROM cashier WHERE  cashier_id=? "
        c.execute(sql,(self.get_id,))
        self.rows=c.fetchall()
        self.trv.delete(*self.trv.get_children())
        if len(self.rows)!=0:

            self.i =0
            for row in self.rows:
                
                self.trv.insert('',self.i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
                self.i+=1
        else:
                tkinter.messagebox.showinfo("Error!", "No Such Cashier Found in database.\nEnter correct cashier_id...")


    def cashierDetailAll(self,*args,**kwargs):
        self.entry_cash_id.delete(0,END)
        sql = "SELECT * FROM cashier "
        c.execute(sql)
        self.rows=c.fetchall()
        self.trv.delete(*self.trv.get_children())
        if len(self.rows)!=0:
            
            self.i =0
            for row in self.rows:
                self.trv.insert('',self.i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
                self.i+=1
            
        conn.commit()

    def addCashier(self,*args,**kwargs):
        self.cashier_name=self.entry_cashier_name.get()
        self.cashier_username= self.entry_cashier_username.get()
        self.cashier_password=self.entry_cashier_password.get()
        self.cashier_dob = self.entry_cashier_dob.get()
        self.cashier_address= self.entry_cashier_address.get()
        self.cashier_phone= self.entry_cashier_phone.get()
        self.cashier_email = self.entry_cashier_email.get()
        self.cashier_remarks = self.entry_cashier_remarks.get()

        if self.cashier_name !='' and self.cashier_username!='' and  self.cashier_password!='' and self.cashier_dob!="" and self.cashier_address!="" and self.cashier_phone!='' and self.cashier_email!="":
            sql="INSERT INTO cashier(cashier_name,cashier_user_name,cashier_password,cashier_dob,cashier_address,cashier_phone, cashier_email,cashier_remarks,added_date) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.cashier_name,self.cashier_username,self.cashier_password,self.cashier_dob,self.cashier_address,self.cashier_phone,self.cashier_email,self.cashier_remarks,date))
            conn.commit()

            self.textbox_text.insert(END, "\n Inserted! "+ str(self.cashier_name) + " into the database")
            tkinter.messagebox.showinfo("Success!", "The Cashier Details Are Saved\nSuccessfully!")
        else:
            tkinter.messagebox.showinfo("Error!", "Please Fill All Fields\n All Fields are Required")


        self.entry_cashier_id.delete(0,END)
        self.entry_cashier_name.delete(0,END)
        self.entry_cashier_username.delete(0,END)
        self.entry_cashier_password.delete(0,END)
        self.entry_cashier_dob.delete(0,END)
        self.entry_cashier_address.delete(0,END)
        self.entry_cashier_phone.delete(0,END)
        self.entry_cashier_email.delete(0,END)
        self.entry_cashier_remarks.delete(0,END)



    def searchCashier(self,*args,**kwargs):
        self.entry_cashier_name.delete(0,END)
        self.entry_cashier_username.delete(0,END)
        self.entry_cashier_password.delete(0,END)
        self.entry_cashier_dob.delete(0,END)
        self.entry_cashier_address.delete(0,END)
        self.entry_cashier_phone.delete(0,END)
        self.entry_cashier_email.delete(0,END)
        self.entry_cashier_remarks.delete(0,END)

        sql= "SELECT cashier_id FROM cashier"
        self.result = c.execute(sql).fetchall()
        if self.entry_cashier_id.get() !='' and [self.result for self.result in self.result if self.result[0]==int(self.entry_cashier_id.get())]:
            sql= "SELECT * FROM cashier WHERE cashier_id=?"
            result = c.execute(sql, (self.entry_cashier_id.get()),)
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
            conn.commit()

            self.entry_cashier_name.delete(0,END)
            self.entry_cashier_name.insert(0,str(self.r1))
            self.entry_cashier_username.delete(0,END)
            self.entry_cashier_username.insert(0,str(self.r2))
            self.entry_cashier_password.delete(0,END)
            self.entry_cashier_password.insert(0,str(self.r3))
            self.entry_cashier_dob.delete(0,END)
            self.entry_cashier_dob.insert(0,str(self.r4))
            self.entry_cashier_address.delete(0,END)
            self.entry_cashier_address.insert(0,str(self.r5))
            self.entry_cashier_phone.delete(0,END)
            self.entry_cashier_phone.insert(0,str(self.r6))
            self.entry_cashier_email.delete(0,END)
            self.entry_cashier_email.insert(0,str(self.r6))
            self.entry_cashier_remarks.delete(0,END)
            self.entry_cashier_remarks.insert(0,str(self.r8))
            self.textbox_text.insert(END, "\n Searched!,\tCashier with id "+ self.entry_cashier_id.get() + " in the database")
        else:
            self.entry_cashier_id.delete(0,END)
            tkinter.messagebox.showinfo("Error!","Wrong Cashier Id Format.\nCashier Id Format:Number.\nEnter  Correct Cashier Id.") 

    def updateCashier(self,*args,**kwargs):
        self.cashier_name=self.entry_cashier_name.get()
        self.cashier_username= self.entry_cashier_username.get()
        self.cashier_password=self.entry_cashier_password.get()
        self.cashier_dob = self.entry_cashier_dob.get()
        self.cashier_address= self.entry_cashier_address.get()
        self.cashier_phone= self.entry_cashier_phone.get()
        self.cashier_email = self.entry_cashier_email.get()
        self.cashier_remarks = self.entry_cashier_remarks.get()

        if self.cashier_name !='' and self.cashier_username!='' and  self.cashier_password!='' and self.cashier_dob!="" and self.cashier_address!="" and self.cashier_phone!='' and self.cashier_email!="":
            self.u1=self.cashier_name
            self.u2=self.cashier_username
            self.u3=self.cashier_password
            self.u4=self.cashier_dob
            self.u5=self.cashier_address
            self.u6=self.cashier_phone
            self.u7=self.cashier_email
            self.u8=self.cashier_remarks
            

            sql = "UPDATE  cashier SET cashier_name=?,cashier_user_name=?,cashier_password=?,cashier_dob=?,cashier_address=?,cashier_phone=?,cashier_email=?,cashier_remarks=?,modified_date=? WHERE cashier_id=?"
            c.execute(sql, (self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.u7,self.u8,date, self.entry_cashier_id.get()))        
            self.textbox_text.insert(END, "\n Updated! "+ str(self.u1) + " into the database")
            tkinter.messagebox.showinfo("Success!,", "Successfully!!!\nThe Cashier Details are\nUpdated in Database!!!")
            conn.commit()
        else:
            tkinter.messagebox.showinfo("Error!", "Before Updating,\nCashier Searching Required.")


        self.entry_cashier_id.delete(0,END)
        self.entry_cashier_name.delete(0,END)
        self.entry_cashier_username.delete(0,END)
        self.entry_cashier_password.delete(0,END)
        self.entry_cashier_dob.delete(0,END)
        self.entry_cashier_address.delete(0,END)
        self.entry_cashier_phone.delete(0,END)
        self.entry_cashier_email.delete(0,END)
        self.entry_cashier_remarks.delete(0,END)

    def deleteCashier(self,*args,**kwargs):
        sql= "SELECT cashier_id FROM cashier"
        self.result = c.execute(sql).fetchall()

        if self.entry_cashier_id.get() !='' and [self.result for self.result in self.result if self.result[0]==int(self.entry_cashier_id.get())]:
            sql = "DELETE FROM  cashier WHERE cashier_id=?"
            c.execute(sql, (self.entry_cashier_id.get(),))        
            self.textbox_text.insert(END, "\n Deleted!\tCashier with id "+ self.entry_cashier_id.get() + " from the database")
            tkinter.messagebox.showinfo("Success!,", "Successfully!!!\nThe Cashier Details are\nDeleted form Database!!!")
            conn.commit()

        else:
            tkinter.messagebox.showinfo("Error!", " Before Deleting,\nCashier Searching Required.")
       
        self.entry_cashier_id.delete(0,END)
        self.entry_cashier_name.delete(0,END)
        self.entry_cashier_username.delete(0,END)
        self.entry_cashier_password.delete(0,END)
        self.entry_cashier_dob.delete(0,END)
        self.entry_cashier_address.delete(0,END)
        self.entry_cashier_phone.delete(0,END)
        self.entry_cashier_email.delete(0,END)
        self.entry_cashier_remarks.delete(0,END)




    
root = Tk()
_CashierRegistration = CashierRegistration(root)
root.geometry("1356x768+0+0")
root.title("Cashier Registration Page")
root.mainloop()

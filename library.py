from tkinter import*
import tkinter as tk 
from tkinter import ttk

import cx_Oracle

from tkinter import messagebox

import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")


        #---------------------------vaiables------------------------------

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.city_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM" ,bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        #------------------------DataFrameLeft---------------------------
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information" ,bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",10,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"]=("Admin staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN_No",font=("times new roman",12,"bold"),padx=2)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblId_No=Label(DataFrameLeft,bg="powder blue",text="ID_No",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblId_No.grid(row=2,column=0,sticky=W)
        txtId_No=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.id_var,width=29)
        txtId_No.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="FirstName",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="LastName",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress=Label(DataFrameLeft,bg="powder blue",text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.address_var,width=29)
        txtAddress.grid(row=5,column=1)

        lblCity=Label(DataFrameLeft,bg="powder blue",text="City",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblCity.grid(row=6,column=0,sticky=W)
        txtCity=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.city_var,width=29)
        txtCity.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="powder blue",text="Book ID:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuther=Label(DataFrameLeft,bg="powder blue",text="Author Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.auther_var,width=29)
        txtAuther.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Date Due:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days on Book:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lateratefine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverdate=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverdate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)

       

        #----------------------------DataFrameRight----------------------------------
        DataFrameRight=LabelFrame(frame,text="Book Details" ,bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight, font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['The C++ Programming Language','The Practice of Programming','The Art of Computer Programming',
                    'Close to the Machine','Fundamentals of Computer Algorithms','The Art of Unix Programming',
                    'The Psychology of Computer Programming','The Java Programming Language','The Best Software Writing I',
                    'After the Software Wars','Free Software, Free Society','Patterns of Software',
                    'Innovation Happens Elsewhere']
        
        def SelectBook(event=""):
            index=listBox.curselection()
            if index:
                value=listBooks[index[0]]
                x=value
                if x==("The C++ Programming Language"):
                        self.bookid_var.set("BKID5454")
                        self.booktitle_var.set("C++ Programming")
                        self.auther_var.set("Bjarne Stroustrup")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 899")
                elif x==("The Practice of Programming"):
                        self.bookid_var.set("BKID8863")
                        self.booktitle_var.set("The Practice of Programming")
                        self.auther_var.set("Brian W. Kernighan, Rob Pike")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 450")
                elif x==("The Art of Computer Programming"):
                        self.bookid_var.set("BKID1223")
                        self.booktitle_var.set("The Art of Computer Programming")
                        self.auther_var.set("Donald Knuth")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 800")
                elif x==("Close to the Machine"):
                        self.bookid_var.set("BKID8775")
                        self.booktitle_var.set("Close to the Machine")
                        self.auther_var.set("Ellen Ullman")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 950")
                elif x==("Fundamentals of Computer Algorithms"):
                        self.bookid_var.set("BKID7776")
                        self.booktitle_var.set("Fundamentals of Computer Algorithms")
                        self.auther_var.set("Ellis Horowitz")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 555")
                elif x==("The Art of Unix Programming"):
                        self.bookid_var.set("BKID7419")
                        self.booktitle_var.set("The Art of Unix Programming")
                        self.auther_var.set("Eric Raymond")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 999")
                elif x==("The Psychology of Computer Programming"):
                        self.bookid_var.set("BKID2154")
                        self.booktitle_var.set("The Psychology of Computer Programming")
                        self.auther_var.set("Gerald M. Weinberg ")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 780")
                elif x==("The Java Programming Language"):
                        self.bookid_var.set("BKID5778")
                        self.booktitle_var.set("The Java Programming Language")
                        self.auther_var.set("James Gosling")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 499")
                elif x==("The Best Software Writing I"):
                        self.bookid_var.set("BKID7844")
                        self.booktitle_var.set("The Best Software Writing I")
                        self.auther_var.set("Joel Spolsky")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 550")
                elif x==("After the Software Wars"):
                        self.bookid_var.set("BKID9854")
                        self.booktitle_var.set("After the Software Wars")
                        self.auther_var.set("Keith Curtis")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 599")
                elif x==("Free Software, Free Society"):
                        self.bookid_var.set("BKID6352")
                        self.booktitle_var.set("Free Software, Free Society")
                        self.auther_var.set("Richard M. Stallman ")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 799")
                elif x==("Patterns of Software"):
                        self.bookid_var.set("BKID5959")
                        self.booktitle_var.set("Patterns of Software")
                        self.auther_var.set("Richard P. Gabriel ")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 850")
                elif x==("Innovation Happens Elsewhere"):
                        self.bookid_var.set("BKID7878")
                        self.booktitle_var.set("Innovation Happens Elsewhere")
                        self.auther_var.set("Richard P. Gabriel")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateratefine_var.set("Rs. 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs. 750")


        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)
               # ---------------------------Buttons Frame------------------------------------
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

         # ---------------------------Information Frame------------------------------------
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)


        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=170)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","idno","firstname","lastname","address",
                                                             "city","postid","mobile","bookid","booktitle","auther","dateborrowed",
                                                             "datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("idno",text="ID No")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("city",text="City")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date OverDue")
        self.library_table.heading("finalprice",text="Final Price")
        


        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("idno",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address",width=100)
        self.library_table.column("city",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


def add_data(self):
            try:
                conn=cx_Oracle.connect('NILESH/nilesh@localhost:1521/xe')
                cursor=conn.cursor()
                cursor.execute("insert into LIBRARY_MEMBER_DETAILS values(:membertype, :prnno, :idno, :firstname, :lastname, :address, :city, :postcode, :mobile, :bookid, :booktitle, :auther, :dateborrowed, :datedue, :days, :latereturnfine, :dateoverdue, :finalprice)",( self.member_var.get(),
                                                                                                                                   self.prn_var.get(),
                                                                                                                                   self.id_var.get(),
                                                                                                                                   self.firstname_var.get(),
                                                                                                                                   self.lastname_var.get(),
                                                                                                                                   self.address_var.get(),
                                                                                                                                   self.city_var.get(),
                                                                                                                                   self.postcode_var.get(),
                                                                                                                                   self.mobile_var.get(),
                                                                                                                                   self.bookid_var.get(),
                                                                                                                                   self.booktitle_var.get(),
                                                                                                                                   self.auther_var.get(),
                                                                                                                                   self.dateborrowed_var.get(),
                                                                                                                                   self.datedue_var.get(),
                                                                                                                                   self.daysonbook_var.get(),
                                                                                                                                   self.lateratefine_var.get(),
                                                                                                                                   self.dateoverdue_var.get(),
                                                                                                                                   self.finalprice_var.get()

                    
                                                                                                                                     ))
                
                conn.commit()
                self.fatch_data()
                messagebox.showinfo("success !!! Member has been inserted successfully ")

            except cx_Oracle.DatabaseError as e:
                print("Database error",e)

            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
def update(self):
                conn=cx_Oracle.connect('NILESH/nilesh@localhost:1521/xe')
                cursor=conn.cursor()
                cursor.execute("update LIBRARY_MEMBER_DETAILS set MEMBER=:membertype, PRN_NO=:prnno, FIRSTNAME= :firstname, LASTNAME=:lastname, ADDRESS=:address, CITY=:city,POSTID= :postcode,MOBILE= :mobile, BOOK_ID=:bookid,BOOK_TITLE = :booktitle, AUTHER=:auther, DATEBORROWED=:dateborrowed, DUEDATE=:datedue, DAYS=:days, LATERETUENFINE=:latereturnfine, DATEOVERDUE=:dateoverdue, FINAL_PRICE=:finalprice where ID=:idno",(
                      self.member_var.get(),
                      self.prn_var.get(),
                      self.firstname_var.get(),
                      self.lastname_var.get(),
                      self.address_var.get(),
                      self.city_var.get(),
                      self.postcode_var.get(),
                      self.mobile_var.get(),
                      self.bookid_var.get(),
                      self.booktitle_var.get(),
                      self.auther_var.get(),
                      self.dateborrowed_var.get(),
                      self.datedue_var.get(),
                      self.daysonbook_var.get(),
                      self.lateratefine_var.get(),
                      self.dateoverdue_var.get(),
                      self.finalprice_var.get(),
                      self.id_var.get()
                ))
                conn.commit()
                self.fatch_data()
                self.reset()
                conn.close()

                messagebox.showinfo("Data Updated Sucessful !!!")

def delete(self):
          if self.id_var.get()=="" :
                messagebox.showerror("Error!! First select the member")
          else:
               conn=cx_Oracle.connect('NILESH/nilesh@localhost:1521/xe')
               cursor=conn.cursor()
               query="delete from LIBRARY_MEMBER_DETAILS where ID=:id_var"
               value=(self.id_var.get(),)
               cursor.execute (query,value)

               conn.commit()
               self.fatch_data()
               self.reset()
               conn.close()

               messagebox.showinfo("Member deleted Successfully !!!")
def fatch_data(self):
          conn=cx_Oracle.connect('NILESH/nilesh@localhost:1521/xe')
          cursor=conn.cursor()
          cursor.execute("select * from LIBRARY_MEMBER_DETAILS")
          rows=cursor.fetchall()

          if len(rows)!=0:
                self.library_table.delete(*self.library_table.get_children())
                for i in rows:
                      self.library_table.insert("",END,values=i)
                conn.commit()
          conn.close()


def get_cursor(self,event=""):
          cursor_row=self.library_table.focus()
          content=self.library_table.item(cursor_row)
          row=content['values']

          self.member_var.set(row[0]),
          self.prn_var.set(row[1]),
          self.id_var.set(row[2]),
          self.firstname_var.set(row[3]),
          self.lastname_var.set(row[4]),
          self.address_var.set(row[5]),
          self.city_var.set(row[6]),
          self.postcode_var.set(row[7]),
          self.mobile_var.set(row[8]),
          self.bookid_var.set(row[9]),
          self.booktitle_var.set(row[10]),
          self.auther_var.set(row[11]),
          self.dateborrowed_var.set(row[12]),
          self.datedue_var.set(row[13]),
          self.daysonbook_var.set(row[14]),
          self.lateratefine_var.set(row[15]),
          self.dateoverdue_var.set(row[16]),
          self.finalprice_var.set(row[17])

def showData(self):
          self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get() + "\n")
          self.txtBox.insert(END,"PRN No:\t\t"+self.prn_var.get() + "\n")
          self.txtBox.insert(END,"ID No:\t\t"+self.id_var.get() + "\n")
          self.txtBox.insert(END,"FirstName:\t\t"+self.firstname_var.get() + "\n")
          self.txtBox.insert(END,"LastName:\t\t"+self.lastname_var.get() + "\n")
          self.txtBox.insert(END,"Address:\t\t"+self.address_var.get() + "\n")
          self.txtBox.insert(END,"City:\t\t"+self.city_var.get() + "\n")
          self.txtBox.insert(END,"Post Code:\t\t"+self.postcode_var.get() + "\n")
          self.txtBox.insert(END,"Mobile No.:\t\t"+self.mobile_var.get() + "\n")
          self.txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get() + "\n")
          self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get() + "\n")
          self.txtBox.insert(END,"Auther:\t\t"+self.auther_var.get() + "\n")
          self.txtBox.insert(END,"DateBorrowed:\t\t"+self.dateborrowed_var.get() + "\n")
          self.txtBox.insert(END,"DateDue:\t\t"+self.datedue_var.get() + "\n")
          self.txtBox.insert(END,"DaysOnBook:\t\t"+self.daysonbook_var.get() + "\n")
          self.txtBox.insert(END,"LateRateFine:\t\t"+self.lateratefine_var.get() + "\n")
          self.txtBox.insert(END,"DateOverDue:\t\t"+self.dateoverdue_var.get() + "\n")
          self.txtBox.insert(END,"FinalPrice:\t\t"+self.finalprice_var.get() + "\n")
    

def reset(self):
          self.member_var.set(""),
          self.prn_var.set(""),
          self.id_var.set(""),
          self.firstname_var.set(""),
          self.lastname_var.set(""),
          self.address_var.set(""),
          self.city_var.set(""),
          self.postcode_var.set(""),
          self.mobile_var.set(""),
          self.bookid_var.set(""),
          self.booktitle_var.set(""),
          self.auther_var.set(""),
          self.dateborrowed_var.set(""),
          self.datedue_var.set(""),
          self.daysonbook_var.set(""),
          self.lateratefine_var.set(""),
          self.dateoverdue_var.set(""),
          self.finalprice_var.set(""),
          self.txtBox.delete("1.0",END)


def iExit(self):
          iExit=tk.messagebox.askyesno("DO you want to exit")
          if iExit>0:
                self.root.destroy()
                return
          
if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()


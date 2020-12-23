from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
root=Tk()
root.title("main page ")
import psycopg2
conn = psycopg2.connect(
    database ="suppliers",
    user="postgres",
    password="chirag2020",
    host="localhost",
    port="5432"
)
# for create acoount
password=StringVar() 
usern=StringVar()
Email=StringVar()
def database6():
    name1=usern.get()
    email=Email.get()
    passeordd= password.get()
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS top (Fullname TEXT primary key,Email TEXT,password TEXT)')
    cursor.execute('INSERT INTO top (FullName,Email,password) VALUES(%s,%s,%s)',(name1,email,passeordd))
    conn.commit()
    messagebox.showinfo("Purnima", "Your Account is Created Succesfully ")
    ## these delete commands are for deleting labels of create account click event
    label_0.place_forget() 
    label_1.place_forget()
    entry_1.place_forget()
    label_2.place_forget()
    entry_2.place_forget()
    label_p.place_forget()
    entry_p.place_forget()
    s.place_forget()
    b1.place_forget()
    c1.place_forget()
    project_data()
def create_account():
    Cline = Canvas(root, height= 400, width=400, bg ="yellow")  
    line = Cline.create_line(390, 40, 390, 4000,  fill ="green") 
    Cline.place(relx=0.0 , rely=0.2)
    global  label_0 
    label_0 = Label(root, text="Registration form", width=18, height= 1, font=("bold", 20))
    label_0.place(relx=0.0, rely=0.3)
    global    label_1
    label_1 = Label(root, text="FullName",width=15, height=2 , font=("bold", 10))
    label_1.place(relx=0.0, rely=0.4) 
    global  entry_1
    entry_1 = Entry(root, textvar=usern, width=20)
    entry_1.place(relx=0.12, rely=0.4)
    global  label_2 
    label_2 = Label(root, text="Email", width=15, height=2, font=("bold", 10))
    label_2.place(relx=0.0,rely=0.5)
    global entry_2 
    entry_2 = Entry(root, textvar=Email)
    entry_2.place(relx=0.12,rely=0.5)
    global  label_p
    label_p = Label(root, text="password", width=15, height=2, font=("bold", 10))
    label_p.place(relx=0.0,rely=0.6) 
    global  entry_p 
    entry_p = Entry(root,textvar=password)
    entry_p.place(relx=0.12,rely=0.6)
    global  s
    s=Button(root, text='Submit', width=40, height=2, bg='brown', fg='white', command=database6)
    s.place(relx=0.0,rely=0.7)
############################
epid= StringVar()
epname= StringVar()
choice= StringVar()
epprice = StringVar()
epmyear= StringVar()
essprice= StringVar()
def database():
    dbid= epid.get()
    dbpname= epname.get()
    dbquality= choice.get()
    dbprice= epprice.get()
    dbmyear= epmyear.get()
    dbsprice= essprice.get()
    if epid.get() == str() :         
         messagebox.showwarning("Purnima ", "Neccesary to Fill  " + "\n" + "\n" + " Product ID")
    elif epname.get() == str() :
        messagebox.showwarning("Purnima ", "Neccesary to Fill  " + "\n" + "\n" + " Product Name")
    elif choice.get() == str() :
        messagebox.showwarning("Purnima ", "Neccesary to Fill  " + "\n" + "\n" + " Product Quality")
    elif epprice.get() == str() :
        messagebox.showwarning("Purnima ", "Neccesary to Fill  " + "\n" + "\n" + " Product Price")
    elif epmyear.get()  == str() :
        messagebox.showwarning("Purnima ", "Neccesary to Fill  " + "\n" + "\n" + " Model year")    
    elif essprice.get() == str() :
        messagebox.showwarning("Purnima ", "Neccesary to Fill  " + "\n" + "\n" + " Sale Price")
    else:    
        try:
            with conn:
                cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS last1 (Product_id VARCHAR(100) PRIMARY KEY,Product_name VARCHAR(45),Product_quality VARCHAR(45),Price VARCHAR(10),Model_year VARCHAR(34),Sale_price VARCHAR(87) )')
            cursor.execute('INSERT INTO last1 (Product_id,Product_name,Product_quality,Price,Model_year,Sale_price) VALUES(%s, %s, %s, %s, %s, %s)',(dbid,dbpname,dbquality,dbprice,dbmyear,dbsprice ))
            conn.commit() 
            cursor.close()
            messagebox.showinfo("Purnima", "Your Data is Entered Succesfully ")    
        except Exception:
            messagebox.showinfo("Purnima", "You have Enterd --> " +  epid.get() +  "\n" + "\n"  + " Not Valid")
def databasecall():
    from tkinter.ttk import Progressbar
    import time
    # global pgbar
    # pgbar= Progressbar(root, length= 400,value= 30, orient = HORIZONTAL, mode = 'indeterminate')   
    # pgbar.place(relx= 0.3, rely= 0.45)
    # pgbar.start(5)  
    #pgbar.stop()    
    cursor=conn.cursor()
    if conn:       
        cursor.execute("SELECT * FROM last1")        
        list0=cursor.fetchall()       
        cursor.close()
        output= ""         
        for x in list0:
            output= output + "product id  "  + str(x[0]) + "  " + "| Product name " + x[1] + " | product Quality " + x[2] + " | Product Price " + str(x[3]) + " | Model Year  " + x[4] + " | Sale Price   " + str(x[5])  + "\n"
        
        text.delete(1.0, END) 
        text.insert(INSERT, "----------")      
        text.insert(END, output)                 
    else:
        messagebox.showinfo("Purnima", "System error occurs ")
def delte_data():    
     if entry_data_deleted.get() == str() :        
         messagebox.showwarning("Purnima ", "Warning ! you Have Entered Nothing")        
     else:
         try:
           with conn:
                 cursor=conn.cursor()
                 messagebox.askquestion("askquestion", "Are you sure? you have lost your data")                 
                 cursor.execute("DELETE FROM last1 WHERE Product_id = " + entry_data_deleted.get())
                 conn.commit() 
                 cursor.close()
                 messagebox.showinfo("Purnima", "Your Data is Dleted Succesfulluy ")
         except Exception:
                 messagebox.showinfo("Purnima", "You have Enterd --> " +  entry_data_deleted.get() +  "\n" + "\n"  + " Not Valid")

scrollbar12 = Scrollbar(root, bg="green")
scrollbar12.pack( side = RIGHT, fill = Y )
def update_data():
         afterp.place_forget()
         displayb123.place_forget()
         lll.place_forget()
         sss.place_forget()    
         project_data()
         print(click.get())
         print(type(click.get()))
         if click.get() == "Product Name":
            if  sss.get() == str() :        
                    messagebox.showwarning("Purnima ", "Warning ! you Have Entered Nothing")        
            else:
                try:
                    with conn:
                         cursor=conn.cursor()
                    messagebox.showinfo("Purnima", "click ok to update data ") 
                    upname=sss.get()                   
                    sql="UPDATE LAST1 SET Product_name = %s WHERE  Product_id  = %s" 
                    cursor.execute("SELECT Product_id  FROM last1")                  
                    cursor.execute(sql,(upname,idpu))                   
                    conn.commit() 
                    cursor.close()
                    messagebox.showinfo("Purnima", "Product Name  Updated Succesfully ")
                except Exception:
                        messagebox.showinfo("Purnima", "You have Enterd --> " + sss.get()  +  "\n" + "\n"  + " Not Valid")       
         elif click.get() == "Product Quality":
            if  sss.get() == str() :        
                    messagebox.showwarning("Purnima ", "Warning ! you Have Entered Nothing")        
            else:
                try:
                    with conn:
                         cursor=conn.cursor()
                    messagebox.showinfo("Purnima", "click ok to update data ") 
                    upname=sss.get()                    
                    sql="UPDATE LAST1 SET Product_quality = %s WHERE  Product_id  = %s"
                    cursor.execute(sql,(upname,idpu))                    
                    conn.commit() 
                    cursor.close()
                    messagebox.showinfo("Purnima", "Product Quality Updated Succesfully ")
                except Exception:
                        messagebox.showinfo("Purnima", "You have Enterd --> " + sss.get()  +  "\n" + "\n"  + " Not Validid")
         elif  click.get() == "Product Price":
                if  sss.get() == str() :        
                    messagebox.showwarning("Purnima ", "Warning ! you Have Entered Nothing")        
                else:
                    try:
                        with conn:
                             cursor=conn.cursor()
                        messagebox.showinfo("Purnima", "click ok to update data ") 
                        upname=sss.get()                    
                        sql="UPDATE LAST1 SET Price = %s WHERE  Product_id  = %s"
                        cursor.execute(sql,(upname,idpu))                    
                        conn.commit() 
                        cursor.close()
                        messagebox.showinfo("Purnima", "Product Price Updated Succesfully ")
                    except Exception:
                        messagebox.showinfo("Purnima", "You have Enterd --> " + sss.get()  +  "\n" + "\n"  + " Not Validid")
         elif  click.get() == "Model Year":
                if  sss.get() == str() :        
                    messagebox.showwarning("Purnima ", "Warning ! you Have Entered Nothing")        
                else:
                    try:
                        with conn:
                             cursor=conn.cursor()
                        messagebox.showinfo("Purnima", "click ok to update data ") 
                        upname=sss.get()                    
                        sql="UPDATE LAST1 SET Model_year  = %s WHERE  Product_id  = %s"
                        cursor.execute(sql,(upname,idpu))                    
                        conn.commit() 
                        cursor.close()
                        messagebox.showinfo("Purnima", "Product Price Updated Succesfully ")
                    except Exception:
                        messagebox.showinfo("Purnima", "You have Enterd --> " + sss.get()  +  "\n" + "\n"  + " Not Validid")
         elif  click.get() == "Sale Price":
                if  sss.get() == str() :        
                    messagebox.showwarning("Purnima ", "Warning ! you Have Entered Nothing")        
                else:
                    try:
                        with conn:
                             cursor=conn.cursor()
                        messagebox.showinfo("Purnima", "click ok to update data ") 
                        upname=sss.get()                    
                        sql="UPDATE LAST1 SET Sale_price = %s WHERE  Product_id  = %s"
                        cursor.execute(sql,(upname,idpu))                    
                        conn.commit() 
                        cursor.close()
                        messagebox.showinfo("Purnima", "Product Price Updated Succesfully ")
                    except Exception:
                        messagebox.showinfo("Purnima", "You have Enterd --> " + sss.get()  +  "\n" + "\n"  + " Not Validid")
         else:
              messagebox.showinfo("Purnima", " Something went Wrong")    
def delupdate2():
         project_data()
         #click.place_forget()
         displayb123.place_forget()
         displayp.place_forget()
         afterp.place_forget()
         ero.place_forget()
         lll.place_forget()
         sss.place_forget()
def more():
        displayp.place_forget()
        ero.place_forget()
        Euplebl.place_forget()
        uplebl.place_forget()
        click.place_forget()
        global lll
        global sss
        if  Euplebl.get() == str() :        
            messagebox.showwarning("Purnima ", "Warning ! you Have Entered Nothing")
            
             
           
        else:
            try:
              with conn:
                   cursor=conn.cursor()              
              global idpu
              idpu= Euplebl.get()
              sql= "SELECT * FROM LAST1 WHERE Product_id = %s"           
              cursor.execute(sql,(idpu,)) 
              data=cursor.fetchall()                     
              conn.commit() 
              cursor.close()            
            except Exception:
                   messagebox.showinfo("Purnima", "You have Enterd --> " +  Euplebl.get()  +  "\n" + "\n"  + " Not Valid")

            if click.get() == "Product Name":           
                 lll = Label(root, text="Enter New Product name  ", width= 30, height= 3)
                 lll.place(relx=0.3 , rely=0.6)            
                 sss = Entry(root,bd= 5)
                 sss.place(relx =0.5, rely=0.6, height=50, width= 250)
            elif click.get() == "Product Quality":            
                 lll = Label(root, text="Enter New Product Quality ", width= 30, height= 3)
                 lll.place(relx=0.3 , rely=0.6)
                 sss = Entry(root, bd= 5)
                 sss.place(relx =0.5, rely=0.6,height=50, width= 250)
            elif click.get() == "Product Price":
                 lll = Label(root, text="Enter New Product Price ", width= 30, height= 3)
                 lll.place(relx=0.3 , rely=0.6)           
                 sss = Entry(root, bd= 5)
                 sss.place(relx =0.5, rely=0.6,height=50, width= 250)
            elif click.get() == "Model Year":           
                 lll = Label(root, text="Enter New Model Year  ", width= 30, height= 3)
                 lll.place(relx=0.3 , rely=0.6)           
                 sss = Entry(root, bd= 5)
                 sss.place(relx =0.5, rely=0.6,height=50, width= 250)
            elif click.get() == "Sale Price":            
                 lll = Label(root, text="Enter New Sale Price  ", width= 30, height= 3)
                 lll.place(relx=0.3, rely=0.6)        
                 sss = Entry(root, bd= 5)
                 sss.place(relx =0.5, rely=0.6,height=50, width= 250)    
        global afterp
        afterp = Button(root, text = " <  --  go back ",height = 2, width = 30, bg='azure', command=delupdate2 ) 
        afterp.place(relx = 0.7, rely = 0.8)
        global displayb123
        displayb123 = Button(root, text = "update it",height = 2, width = 30, bg='azure', command= update_data ) 
        displayb123.place(relx = 0.3, rely = 0.8)
def project_data():   
    c= Canvas(root, height= 3000, width=3000 , bg="azure")
    c.pack()

    def delete_all():
         project_data()
        
         Lid.place_forget()
         Eid.place_forget()
         Lpname.place_forget()
         Epname.place_forget()
         Lpquality.place_forget()
         droplist.place_forget()
         droplist2.place_forget()
         Lprice.place_forget()
         Eprice.place_forget()
         Lmyear.place_forget()
         Lsprice.place_forget()
         Esprice.place_forget()
         bsubmit.place_forget()
         ssubmit.place_forget()
         b1.place_forget()
         c1.place_forget()
        ## these delete commands are for display data click event
    def del_display():
         project_data()

         text.place_forget()
         displayb.place_forget()
         dback.place_forget()
         b1.place_forget()
         c1.place_forget()
         #ssubmit.place_forget()
    def del_delete():
        project_data()

        label_of_enter_delete_product_id_to_delete.place_forget()
        entry_data_deleted.place_forget()
        button_to_delete_data.place_forget()
        delete_page_back_button.place_forget()
        b1.place_forget()
        c1.place_forget()
    def update_delete():
         project_data()

         
         uplebl.place_forget()
         Euplebl.place_forget()
         ero.place_forget()
         displayp.place_forget()
         click.place_forget()
         
         
    def call_insert():       
        insert_button.config(state = DISABLED)
        display_button.config(state = DISABLED)
        delete_button.config(state = DISABLED)
        update_button.config(state = DISABLED)
        global Lid
        Lid = Label(root, text="Product id  ")
        Lid.place(relx=0.01 , rely=0.5)
        global Eid
        Eid = Entry(root,textvar= epid, bd= 5)
        Eid.place(relx =0.098, rely=0.5,height=30, width= 150)
        Eid.focus()
        global Lpname
        Lpname = Label(root, text="Product name  ")
        Lpname.place(relx=0.01 , rely=0.6)
        global Epname
        Epname = Entry(root, textvar= epname, bd= 5)
        Epname.place(relx =0.098, rely=0.6,height=30, width= 150)
        global Lpquality
        Lpquality = Label(root, text="Product Quality  ")
        Lpquality.place(relx=0.01 , rely=0.7)
        list1 = ["Good", "Bad", "Nice", "Exellent","sad"];
        global droplist
        droplist=OptionMenu(root, choice, *list1)
        droplist.config(width=15)
        choice.set(" select your quality")   
        droplist.place(relx =0.0999, rely=0.7,height=30, width= 150)
        global Lprice
        Lprice = Label(root, text="Product Price  ")
        Lprice.place(relx=0.01 , rely=0.8)
        global Eprice
        Eprice = Entry(root, textvar= epprice, bd= 5)
        Eprice.place(relx =0.0999, rely=0.8, height=30, width= 150)
        global Lmyear
        list2 = ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"];
        global droplist2        
        droplist2=OptionMenu(root, epmyear, *list2)
        droplist2.config(width=150, height= 200)
        droplist2.place(relx =0.5, rely=0.7, height=30, width= 150)
        epmyear.set(" select model year")
        Lmyear = Label(root, text="Model Year  ")
        Lmyear.place(relx=0.4 , rely=0.7)
        global Lsprice
        Lsprice = Label(root, text="Sale Price  ")
        Lsprice.place(relx=0.4 , rely=0.8)
        global Esprice
        Esprice = Entry(root, textvar= essprice, bd= 5)
        Esprice.place(relx =0.5, rely=0.8, height=30, width= 150)
        global bsubmit
        bsubmit = Button(root, text = "Insert Data", height = 2, width = 100,  bg='slateblue1', fg='black' , command = database)  
        bsubmit.place(relx = 0.1, rely = 0.9, anchor = S)
        global ssubmit
        ssubmit = Button(root, text = "go Back", height = 2, width = 100,  bg='slateblue1', fg='black',command=delete_all)  
        ssubmit.place(relx = 0.9, rely = 0.9, anchor = S) 
    def call_display(): 
        insert_button.config(state = DISABLED)
        display_button.config(state = DISABLED)
        delete_button.config(state = DISABLED)
        update_button.config(state = DISABLED)
        global text
        text = Text(root, heigh= 15, width= 140)
        text.place(relx= 0.01, rely= 0.5)
        global displayb
        displayb = Button(root, text = "Show Data", bd= 5,height = 2, width = 14, bg='blue', command= databasecall)
        displayb.place(relx = 0.94, rely = 0.7, anchor = S)
        global dback
        dback = Button(root, text = "go Back", bd= 5, height = 2, width = 14,  bg='slateblue1', fg='black',command=del_display)  
        dback.place(relx = 0.94, rely = 0.8,anchor = S) 
    def call_delete():
        insert_button.config(state = DISABLED)
        display_button.config(state = DISABLED)
        delete_button.config(state = DISABLED)
        update_button.config(state = DISABLED)
        global label_of_enter_delete_product_id_to_delete
        label_of_enter_delete_product_id_to_delete= Label(root, text="Enter product ID",width=13 , height= 2)
        label_of_enter_delete_product_id_to_delete.place(relx=0.72 , rely=0.6 , anchor = S)
        global entry_data_deleted
        entry_data_deleted= Entry(root, bd= 5)
        entry_data_deleted.place(relx =0.86, rely=0.6, height=30, width= 180 , anchor = S)
        global button_to_delete_data
        button_to_delete_data = Button(root, text = "Delete",height = 2, width = 45, bg='azure', command=delte_data) 
        button_to_delete_data.place(relx = 0.8, rely = 0.72, anchor = S)
        global delete_page_back_button
        delete_page_back_button = Button(root, text = "go Back", height = 2, width = 100,  bg='slateblue1', fg='black',command=del_delete)  
        delete_page_back_button.place(relx = 0.9, rely = 0.9, anchor = S) 
    def call_update():
        insert_button.config(state = DISABLED)
        display_button.config(state = DISABLED)
        delete_button.config(state = DISABLED)
        update_button.config(state = DISABLED)
        global uplebl
        uplebl = Label(root, text="Enter Product ID  " , height = 2, width = 20, bd= 2)
        uplebl.place(relx=0.3 , rely=0.5)
        uplebl.focus()
        global Euplebl
        Euplebl = Entry(root, bd= 5)
        Euplebl.place(relx =0.43, rely=0.5, height=40, width= 170)
        vlist = ["Product Name", "Product Quality", "Product Price","Model Year", "Sale Price"]
        global click
        click = ttk.Combobox(root, value=vlist, width= 39, height= 5)
        click.current(0)
        click.place(relx = 0.3, rely = 0.6)
        global ero
        ## use an unicode sample to 
        ero = Button(root, text = "Proceed " +u"\u00BB", bd= 5, height = 2, width = 30, bg='azure',font= ("Helvetica", 10) ,command= more ) 
        ero.place(relx = 0.7, rely = 0.5)
        global displayp
        displayp = Button(root, text = " <  --  go back ", bd= 5,height = 2, width = 30, bg='azure', command= update_delete ) 
        displayp.place(relx = 0.7, rely = 0.8)
    global insert_button
    insert_button = Radiobutton(root, text = "insert data", bd= 5,height = 2, width = 14, bg='gray63' , fg='black', command=call_insert)
    insert_button.place(relx = 0.2, rely = 0.4, anchor = W)  
    global display_button
    display_button = Radiobutton(root, text = "display data", bd= 5,height = 2, width = 14, bg='gray63' , fg='black', command=call_display)
    display_button.place(relx = 0.4, rely = 0.4, anchor = W)
    global delete_button
    delete_button = Radiobutton(root, text = "delete data", bd= 5,height = 2, width = 14, bg='gray63' , fg='black', command=call_delete)
    delete_button.place(relx = 0.6, rely = 0.4, anchor = W)
    global update_button
    update_button = Radiobutton(root, text = "update data", bd= 5,height = 2, width = 14, bg='gray63' , fg='black', command= call_update)
    update_button.place(relx = 0.8, rely = 0.4, anchor = W) 
def buth(e):##### on button
    b1["bg"] = "green"
    c1["bg"] = "blue"
    l1["bg"] = "deep sky blue"
def lev(e):#  leave button 
    b1["bg"] = "black"
    c1["bg"] = "black"
    l1["bg"] = "black"
global b1   
b1 = Radiobutton(root, text = "Join For Free", bd= 5, height = 2, width = 14, bg='azure' , fg='white', command=project_data)
b1.place(relx = 0.9, rely = 0.1, anchor = NE)  
b1.bind("<Enter>", buth)
b1.bind("<Leave>", lev)
global c1   
c1= Radiobutton(root, text = "create account", bd= 5 ,height = 2, width = 14, bg='black' , fg='azure', command=create_account)
c1.place(relx = 0.2, rely = 0.1, anchor = NE) 
c1.bind("<Enter>", buth)
c1.bind("<Leave>", lev)
global l1   
l1= Radiobutton(root, text = "Login", height = 2, width = 14, bg='black' , fg='azure', command=NONE, bd= 5)
l1.place(relx = 0.5, rely = 0.1, anchor = NE) 
l1.bind("<Enter>", buth)
l1.bind("<Leave>", lev)
root.configure(bg='cyan')
root.geometry("9500x7700")   
root.mainloop()
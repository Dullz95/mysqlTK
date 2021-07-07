import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import datetime, timedelta, date

# create GUI
master = tk.Tk()
master.title("Login Page")
master.geometry("420x250")
master.configure(bg="skyblue")
users=["intern","lecturer","admin","visitor"]
records=[]
identification =""



class Login_system:
    def __init__(self,master):
        self.usern=Label(master,text="Username",bg="skyblue")
        self.usern.place(x=50,y=50)
        self.usere=Entry(master,textvariable="name")
        self.usere.place(x=250,y=50)
        self.passe=Label(master,text="Password",bg="skyblue")
        self.passe.place(x=50,y=100)
        self.passwe=Entry(master,textvariable="pass")
        self.passwe.place(x=250,y=100)
        self.users_cb = Combobox(master)
        self.users_cb['values'] = users
        self.users_cb['state'] = 'readonly'
        self.users_cb.set('Select User')
        self.users_cb.place(x=50, y=150)
        self.text=Label(master, text="visiting life choices?",bg="skyblue")
        self.text.place(x=50,y=200)

        def register():
            root = tk.Tk()
            root.title("register")
            root.geometry("420x650")
            root.configure(bg="skyblue")
            usern = Label(root, text="name", bg="skyblue")
            usern.place(x=50, y=50)
            name = Entry(root, textvariable="name", bg="skyblue")
            name.place(x=250, y=50)
            sname = Label(root, text="surname", bg="skyblue")
            sname.place(x=50, y=100)
            surname = Entry(root, textvariable="surname", bg="skyblue")
            surname.place(x=250, y=100)
            id_no = Label(root, text="ID no", bg="skyblue")
            id_no.place(x=50, y=150)
            id_ = Entry(root, textvariable="ID", bg="skyblue")
            id_.place(x=250, y=150)
            phonel = Label(root, text="Phone", bg="skyblue")
            phonel.place(x=50, y=200)
            phone = Entry(root, textvariable="phone")
            phone.place(x=250, y=200)
            next_of = Label(root, text="Next of kin details below: ")
            next_of.place(x=50, y=250)
            next_name = Label(root, text="name")
            next_name.place(x=50, y=300)
            name_entry = Entry(root, textvariable="kin name")
            name_entry.place(x=250, y=300)
            next_phone = Label(root, text="Phone Number")
            next_phone.place(x=50, y=350)
            phone_entry = Entry(root, textvariable="kin phone")
            phone_entry.place(x=250, y=350)
            passlabel = Label(root, text="Select password")
            passlabel.place(x=50, y=400)
            passwordl = Entry(root, textvariable="pass")
            passwordl.place(x=250, y=400)
            role_label = Label(root, text="Insert visitor into blank field ")
            role_label.place(x=50, y=450)
            role = Entry(root, textvariable="role")
            role.place(x=250, y=450)

            def register_new_user():
                if name.get() == "" or surname.get() == "" or id_.get() == "" or phone.get() == "" or name_entry.get() == "" or phone_entry.get() == "" or role.get() == "":
                    messagebox.showerror("Error", "Please fill all fields")

                else:
                    mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1',
                                                   database='lc_online',
                                                   auth_plugin='mysql_native_password')
                    mycursor = mydb.cursor()
                    sql_one = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"
                    val_one = (id_.get(), name.get(), surname.get(), phone.get(), passwordl.get(), role.get())
                    sql_two = "INSERT INTO next_of_kin (id, Name, Phone) VALUES (%s, %s, %s)"
                    val_two = (id_.get(), name_entry.get(), phone_entry.get())
                    mycursor.execute(sql_one, val_one)
                    mycursor.execute(sql_two, val_two)
                    mydb.commit()
                    messagebox.showinfo("Successful", "Your account is registered. You may now sign in.")
                    root.destroy()

            new_user = Button(root, text="register", command=register_new_user)
            new_user.place(x=150, y=600)


        def general_log_in_screen():
            window = tk.Tk()
            window.title("intern loggin")
            window.geometry("420x250")
            window.configure(bg="skyblue")
            date_now = datetime.now().date().strftime("%Y-%m-%d")
            time_now = datetime.now().time().strftime('%H:%M:%S')

            def sign_in():
                mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1', database='lc_online',
                                               auth_plugin='mysql_native_password')
                mycursor = mydb.cursor()
                first = "INSERT INTO signing(id, sign_in, sign_in_date) VALUES (%s, %s, %s)"
                data_one = (identification, time_now, date_now)
                mycursor.execute(first, data_one)
                mydb.commit()

            def sign_out():
                mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1', database='lc_online',
                                               auth_plugin='mysql_native_password')
                mycursor = mydb.cursor()
                data = "UPDATE signing SET sign_out= %s WHERE id='"+identification+"' AND sign_in_date='"+date_now+"'"
                val = time_now
                mycursor.execute(data, val)
                mydb.commit()

            log_in=Button(window,text="Sign in", command=sign_in)
            log_in.place(x=100,y=100)
            log_in = Button(window, text="Sign out", command=sign_out)
            log_in.place(x=200, y=100)
        def admin_screen():
            window = tk.Tk()
            window.title("admin")
            window.geometry("420x250")
            window.configure(bg="skyblue")
            usern = Label(window, text="Please enter username")
            usern.place(x=50, y=50)
            usere = Entry(window, textvariable="name")
            usere.place(x=250, y=50)
            passe = Label(window, text="Please enter password")
            passe.place(x=50, y=100)
            passwe = Entry(window, textvariable="pass")
            passwe.place(x=250, y=100)


        def signing_in():
            mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1', database='lc_online',auth_plugin='mysql_native_password')
            mycursor=mydb.cursor()
            mycursor.execute("select * from users where name='" + self.usere.get() + "'")
            records=mycursor.fetchall()
            global identification
            if records == []:
                messagebox.showerror("Error", "User do not exist")
            else:
                if self.usere.get() == records[0][1] and self.passwe.get() == records[0][4]:
                    identification=records[0][0]
                    if self.users_cb.get() != "admin":
                        general_log_in_screen()
                    elif self.users_cb.get() == "admin":
                        admin_screen()
                elif  self.passwe.get() != records[0][4]:
                    messagebox.showerror("Erro","User and password do not match")

        gen_log = Button(master, text="Sign in", command=signing_in)
        gen_log.place(x=250, y=150)
        reg=Button(master,text="register user", command=register)
        reg.place(x=250,y=200)

l=Login_system(master)
master.mainloop()

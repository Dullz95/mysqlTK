import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import datetime, timedelta, date


#
# mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1', database='lc_online',
#                                auth_plugin='mysql_native_password')
# mycursor=mydb.cursor()
# xy=mycursor.execute('select * from users')
# for i in mycursor:
# print(i)


root = tk.Tk()
root.title("register")
root.geometry("420x650")
root.configure(bg="skyblue")
usern = Label(root, text="name")
usern.place(x=50, y=50)
name = Entry(root, textvariable="name")
name.place(x=250, y=50)
sname = Label(root, text="surname")
sname.place(x=50, y=100)
surname = Entry(root, textvariable="surname")
surname.place(x=250, y=100)
id_no = Label(root, text="ID no")
id_no.place(x=50, y=150)
id_ = Entry(root, textvariable="ID")
id_.place(x=250, y=150)
phonel = Label(root, text="Phone")
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
passwordl=Entry(root,textvariable="pass")
passwordl.place(x=50,y=400)
role=Entry(root,textvariable="role")
role.place(x=50, y=450)


def register_new_user():
    if name.get() == "" or surname.get() == "" or id_.get() == "" or phone.get() == "" or name_entry.get() == "" or phone_entry.get()== "" or role.get() == "":
        messagebox.showerror("Error", "Please fill all fields")

    else:
        mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1', database='lc_online',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        data = "INSERT INTO users (id, name, surname, phone, password, roles) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (id_.get(), name.get(), surname.get(), phone.get(), passwordl.get(), role.get())
        mycursor.execute(data, val)
        mydb.commit()
        data="INSERT INTO signing (id) VALUES (%s)"
        val = (id_.get())
        mycursor.execute(data, val)
        mydb.commit()
        messagebox.showinfo("Welcome", "Successfully registered")


new_user = Button(root, text="register", command=register_new_user)
new_user.place(x=150, y=200)
root.mainloop()
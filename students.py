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
passlabel=Label(root,text="Select password")
passlabel.place(x=50,y=400)
passwordl=Entry(root,textvariable="pass")
passwordl.place(x=250,y=400)
role_label=Label(root,text="Insert visitor into blank field ")
role_label.place(x=50,y=450)
role=Entry(root,textvariable="role")
role.place(x=250, y=450)



def register_new_user():
    if name.get() == "" or surname.get() == "" or id_.get() == "" or phone.get() == "" or name_entry.get() == "" or phone_entry.get()== "" or role.get() == "":
        messagebox.showerror("Error", "Please fill all fields")

    else:
        mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1', database='lc_online',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        sql_one = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"
        val_one = (id_.get(), name.get(), surname.get(), phone.get(), passwordl.get(), role.get())
        sql_two= "INSERT INTO next_of_kin (id, Name, Phone) VALUES (%s, %s, %s)"
        val_two = (id_.get(), name_entry.get(), phone_entry.get())
        mycursor.execute(sql_one, val_one)
        mycursor.execute(sql_two, val_two)
        mydb.commit()
        messagebox.showinfo("Successful", "Your account is registered. You may now sign in.")
        root.destroy()

new_user = Button(root, text="register", command=register_new_user)
new_user.place(x=150, y=600)
root.mainloop()
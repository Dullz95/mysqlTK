import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = tk.Tk()
root.title("Login Page")
root.geometry("500x400")
root.configure(bg="skyblue")


usern=Label(root,text="Please enter username")
usern.place(x=50,y=50)
usere=Entry(root,textvariable="name")
usere.place(x=250,y=50)
passe=Label(root,text="Please enter password")
passe.place(x=50,y=100)
passwe=Entry(root,textvariable="pass")
passwe.place(x=250,y=100)

def register():
    if usere.get() == "" or passwe.get() == "":
         messagebox.showerror("Error","Please fill all fields")

    else:
        mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1', database='hospital', auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        data= "INSERT INTO login(user, password) VALUES (%s, %s)"
        val= (usere.get(), passwe.get())
        mycursor.execute(data, val)
        mydb.commit()
        messagebox.showinfo("Welcome","Successfully registered")



def loginbutton():
    mydb = mysql.connector.connect(user='root',password='yolo0909',host='127.0.0.1',database='hospital',auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    xy=mycursor.execute('select * from login')
    for i in mycursor:
        if usere.get() == i[0] and passwe.get() == i[1]:
            messagebox.showinfo("Welcome","Successfully logged in")
            import second
    if usere.get() not in i[0] or passwe.get() not in i[1]:
         messagebox.showerror("Error", "User does  not exist")
         usere.delete(0,END)
         passwe.delete(0,END)


reg=Button(root,text="register user", command=register)
reg.place(x=300,y=300)
login_b=Button(root,text="loginnn", command=loginbutton)
login_b.place(x=200,y=300)





root.mainloop()

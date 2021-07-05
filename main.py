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
users=["interns","staff","admin","visitors"]
employees=[]

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
            root.geometry("420x250")
            root.configure(bg="skyblue")
            usern = Label(root, text="Please enter username")
            usern.place(x=50, y=50)
            usere = Entry(root, textvariable="name")
            usere.place(x=250, y=50)
            passe = Label(root, text="Please enter password")
            passe.place(x=50, y=100)
            passwe = Entry(root, textvariable="pass")
            passwe.place(x=250, y=100)

            def register_new_user():
                if self.usere.get() == "" or self.passwe.get() == "":
                     messagebox.showerror("Error","Please fill all fields")

                else:
                    mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1', database='hospital', auth_plugin='mysql_native_password')
                    mycursor = mydb.cursor()
                    data= "INSERT INTO login(user, password) VALUES (%s, %s)"
                    val= (self.usere.get(), self.passwe.get())
                    mycursor.execute(data, val)
                    mydb.commit()
                    messagebox.showinfo("Welcome","Successfully registered")

            new_user = Button(root, text="register", command=register_new_user)
            new_user.place(x=150,y=200)
        def intern():
            window = tk.Tk()
            window.title("intern loggin")
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



            def loginbutton():
                mydb = mysql.connector.connect(user='root',password='yolo0909',host='127.0.0.1',database='hospital',auth_plugin='mysql_native_password')
                mycursor=mydb.cursor()
                xy=mycursor.execute('select * from login')
                timenow= datetime.now()
                for i in mycursor:
                    if self.usere.get() == i[0] and self.passwe.get() == i[1]:
                        messagebox.showinfo("Welcome","Successfully logged in")

                        import second
                if self.usere.get() not in i[0] or self.passwe.get() not in i[1]:
                     messagebox.showerror("Error", "User does  not exist")
                     self.usere.delete(0,END)
                     self.passwe.delete(0,END)

            login_b = Button(master, text="loginnn", command=loginbutton)
            login_b.place(x=150, y=200)


        reg=Button(master,text="register user", command=register)
        reg.place(x=250,y=200)
        intern_log = Button(master, text="Sign in", command=intern)
        intern_log.place(x=250, y=150)





l=Login_system(master)
master.mainloop()

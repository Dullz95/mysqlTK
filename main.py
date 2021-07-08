import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
from datetime import datetime


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
            master.destroy()
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
            phone = Entry(root, textvariable="phone", bg="skyblue")
            phone.place(x=250, y=200)
            next_of = Label(root, text="Next of kin details below: ")
            next_of.place(x=50, y=250)
            next_name = Label(root, text="name", bg="skyblue")
            next_name.place(x=50, y=300)
            name_entry = Entry(root, textvariable="kin name", bg="skyblue")
            name_entry.place(x=250, y=300)
            next_phone = Label(root, text="Phone Number", bg="skyblue")
            next_phone.place(x=50, y=350)
            phone_entry = Entry(root, textvariable="kin phone", bg="skyblue")
            phone_entry.place(x=250, y=350)
            passlabel = Label(root, text="Select password", bg="skyblue")
            passlabel.place(x=50, y=400)
            passwordl = Entry(root, textvariable="pass", bg="skyblue")
            passwordl.place(x=250, y=400)
            role_label = Label(root, text="Reason for visiting Life Choices: ", bg="skyblue")
            role_label.place(x=50, y=450)
            role = Label(root, text="visitor", bg="skyblue")
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
                mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1',
                                               database='lc_online',
                                               auth_plugin='mysql_native_password')
                mycursor = mydb.cursor()
                data = "UPDATE signing SET sign_out=%s WHERE id='" + identification + "' AND sign_in_date='" + date_now + "'"
                val = [time_now]
                mycursor.execute(data, val)
                mydb.commit()

            log_in=Button(window,text="Sign in", command=sign_in)
            log_in.place(x=100,y=100)
            log_in = Button(window, text="Sign out", command=sign_out)
            log_in.place(x=250, y=200)
        def admin_screen():
            admin = tk.Tk()
            admin.title("Admin")
            admin.configure(bg="skyblue")
            admin.attributes('-fullscreen',True)
            main_frame=Frame(admin, width=1350,height=450,bg="black",highlightbackground="lightgreen", highlightthickness=15)
            main_frame.place(x=80,y=50)

            def delete_user():
                mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1',
                                               database='lc_online',
                                               auth_plugin='mysql_native_password')
                mycursor = mydb.cursor()
                tree_data= tree.focus()
                value = tree.item(tree_data)
                value= value['values']
                mycursor.execute("DELETE FROM next_of_kin WHERE id='" + str(value[0]) + "'")
                mycursor.execute("DELETE FROM signing WHERE id='" + str(value[0]) + "'")
                mycursor.execute("DELETE FROM users WHERE id='" + str(value[0]) + "'")
                mydb.commit()
                tree.delete(*tree.get_children())
                tree_two.delete(*tree_two.get_children())
                mycursor.execute("SELECT * FROM users")
                records = mycursor.fetchall()
                for i in records:
                    tree.insert("",'end',values=i)
                mycursor.execute("SELECT * FROM signing")
                records_two = mycursor.fetchall()
                for i in records_two:
                    tree_two.insert("",'end',values=i)

            delete_button=Button(admin,text="delete user",command=delete_user)
            delete_button.place(x=500,y=750)

            def selected_data(table):
                cur_item = table.focus()
                value = table.item(cur_item, "values")
                frame = Frame(admin, width=400, height=320, bg="black")
                frame.place(x=100, y=150)
                l2 = Label(frame, text="name", width=8)
                name_entry = Entry(frame, textvariable="name", width=25)
                l2.place(x=50, y=30)
                name_entry.place(x=170, y=30)

                l1 = Label(frame, text="ID number", width=8)
                id_entry = Entry(frame, textvariable="person_id", width=25)
                l1.place(x=50, y=70)
                id_entry.place(x=170, y=70)

                l4 = Label(frame, text="Surname", width=8)
                l4.place(x=50, y=110)
                surname_entry = Entry(frame, textvariable="surname", width=25)
                surname_entry.place(x=170, y=110)

                l5 = Label(frame, text="Phone number", width=11)
                l5.place(x=50, y=150)
                phone_entry = Entry(frame, textvariable="phone", width=25)
                phone_entry.place(x=170, y=150)
                # e5.delete(0, END)

                l3 = Label(frame, text="Password", width=8)
                l3.place(x=50, y=190)
                password_entry = Entry(frame, textvariable="password", width=25)
                password_entry.place(x=170, y=190)

                l6 = Label(frame, text="role", width=6)
                l6.place(x=50, y=230)
                role_entry = Entry(frame, textvariable="role", width=25)
                role_entry.place(x=170, y=230)

                name_entry.delete(0, END)
                id_entry.delete(0, END)
                surname_entry.delete(0, END)
                phone_entry.delete(0, END)
                role_entry.delete(0, END)
                password_entry.delete(0, END)

                id_entry.insert(0, value[0])
                name_entry.insert(0, value[1])
                surname_entry.insert(0, value[2])
                phone_entry.insert(0, value[3])
                password_entry.insert(0, value[4])
                role_entry.insert(0,value[5])


                def update_data():
                    nonlocal id_entry, name_entry, surname_entry, phone_entry, password_entry, role_entry, cur_item, value
                    updated_id = id_entry.get()
                    updated_name = name_entry.get()
                    updated_surname = surname_entry.get()
                    updated_password= password_entry.get()
                    updated_phone = phone_entry.get()
                    updated_role = role_entry.get()
                    table.item(cur_item, value=( updated_id, updated_name, updated_surname, updated_phone, updated_password,  updated_role))
                    data="UPDATE users SET id=%s, name=%s, " \
                         "surname=%s, phone=%s, password=%s, roles=%s WHERE id='" + value[0] + "'"
                    val= (updated_id, updated_name, updated_surname, updated_phone, updated_password, updated_role)
                    cursor.execute(data, val)


                    conn.commit()
                    messagebox.showinfo("Success", "Students Updated")
                    name_entry.delete(0, END)
                    id_entry.delete(0, END)
                    surname_entry.delete(0, END)
                    phone_entry.delete(0, END)
                    role_entry.delete(0, END)
                    password_entry.delete(0, END)
                    frame.destroy()

                submit_btn = Button(frame, text="submit", command=update_data)
                submit_btn.configure(bg='white', fg='black')
                submit_btn.place(x=100, y=280)
                cancel_btn = Button(frame, text="cancel", command=frame.destroy)
                cancel_btn.configure(bg='white', fg='black')
                cancel_btn.place(x=240, y=280)

            update_entries = Button(admin, text="Update", bg="white", fg="black",
                                    command=lambda: selected_data(tree))
            update_entries.place(x=250, y=750)

            def sign_out_admin():
                date_now = datetime.now().date().strftime("%Y-%m-%d")
                time_now = datetime.now().time().strftime('%H:%M:%S')
                mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1',
                                               database='lc_online',
                                               auth_plugin='mysql_native_password')
                mycursor = mydb.cursor()
                data = "UPDATE signing SET sign_out=%s WHERE id='" + identification + "' AND sign_in_date='" + date_now + "'"
                val = [time_now]
                mycursor.execute(data, val)
                mydb.commit()
                messagebox.showinfo("Error","Successfully signed out. Enjoy the rest of your day")
                admin.destroy()
            admin_sign_out=Button(admin,text="Sign out", command=sign_out_admin)
            admin_sign_out.place(x=200,y=750)

            def create_user():
                master = tk.Tk()
                master.title("Login Page")
                master.geometry("600x600")
                master.configure(bg="skyblue")
                usern = Label(master, text="name", bg="skyblue")
                usern.place(x=50, y=50)
                name = Entry(master, textvariable="name", bg="skyblue")
                name.place(x=250, y=50)
                sname = Label(master, text="surname", bg="skyblue")
                sname.place(x=50, y=100)
                surname = Entry(master, textvariable="surname", bg="skyblue")
                surname.place(x=250, y=100)
                id_no = Label(master, text="ID no", bg="skyblue")
                id_no.place(x=50, y=150)
                id_ = Entry(master, textvariable="ID", bg="skyblue")
                id_.place(x=250, y=150)
                phonel = Label(master, text="Phone", bg="skyblue")
                phonel.place(x=50, y=200)
                phone = Entry(master, textvariable="phone")
                phone.place(x=250, y=200)
                passlabel = Label(master, text="Select password")
                passlabel.place(x=50, y=400)
                passwordl = Entry(master, textvariable="pass")
                passwordl.place(x=250, y=400)
                role_label = Label(master, text="Insert visitor into blank field ")
                role_label.place(x=50, y=450)
                role = Entry(master, textvariable="role")
                role.place(x=250, y=450)

                def new_user():
                    if name.get() == "" or surname.get() == "" or id_.get() == "" or phone.get() == "" or role.get() == "":
                        messagebox.showerror("Error", "Please fill all fields")
                    else:
                        mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1',
                                                   database='lc_online',
                                                   auth_plugin='mysql_native_password')
                        mycursor = mydb.cursor()
                        sql_one = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"
                        val_one = (id_.get(), name.get(), surname.get(), phone.get(), passwordl.get(), role.get())
                        mycursor.execute(sql_one, val_one)
                        mydb.commit()
                        messagebox.showinfo("Successful", "New account registered.")
                        master.destroy()
                create_ = Button(master,text="Create User", command=new_user)
                create_.place(x=50,y=500)

            new_user_button = Button(admin, text="Create new user", command=create_user)
            new_user_button.place(x=350,y=750)


            tree = Treeview(admin, columns=(1, 2, 3, 4, 5, 6), show='headings', height=6)
            tree.place(x=150,y=100)

            tree.heading(1, text="ID")
            tree.heading(2, text="Name")
            tree.heading(3, text="Surname")
            tree.heading(4,text="Phone")
            tree.heading(5, text="Password")
            tree.heading(6,text="Role")

            conn = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1',
                                           database='lc_online', auth_plugin='mysql_native_password')
            cursor = conn.cursor()
            sql = "SELECT id, name, surname, phone, password, roles FROM users"
            cursor.execute(sql)

            rows = cursor.fetchall()
            total = cursor.rowcount
            def populate():
                for i in rows:
                    tree.insert("",'end',values=i)
            populate()

            tree_two = Treeview(admin, columns=(1, 2, 3, 4, 5), show='headings', height=6)
            tree_two.place(x=230, y=300)

            tree_two.heading(1, text="number")
            tree_two.heading(2, text="ID")
            tree_two.heading(3, text="Sign_in")
            tree_two.heading(4, text="Sign_out")
            tree_two.heading(5, text="Sign_in_date")


            conn = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1',
                                           database='lc_online', auth_plugin='mysql_native_password')
            cursor = conn.cursor()
            sql = "SELECT number, id, sign_in, sign_out, sign_in_date FROM signing"
            cursor.execute(sql)

            rows = cursor.fetchall()
            total = cursor.rowcount
            def populate_two():
                for i in rows:
                    tree_two.insert("", 'end', values=i)
            populate_two()



        def signing_in():
            mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1', database='lc_online',auth_plugin='mysql_native_password')
            mycursor=mydb.cursor()
            mycursor.execute("select * from users where name='" + self.usere.get() + "'")
            records=mycursor.fetchall()
            global identification
            date_now = datetime.now().date().strftime("%Y-%m-%d")
            time_now = datetime.now().time().strftime('%H:%M:%S')
            if records == []:
                messagebox.showerror("Error", "User do not exist")
            else:
                if self.usere.get() == records[0][1] and self.passwe.get() == records[0][4]:
                    identification=records[0][0]
                    if self.users_cb.get() != "admin":
                        general_log_in_screen()
                        master.destry()
                    elif self.users_cb.get() == "admin":
                        first = "INSERT INTO signing(id, sign_in, sign_in_date) VALUES (%s, %s, %s)"
                        data_one = (identification, time_now, date_now)
                        mycursor.execute(first, data_one)
                        mydb.commit()
                        admin_screen()
                        master.destroy()
                elif  self.passwe.get() != records[0][4]:
                    messagebox.showerror("Error","User and password do not match")

        gen_log = Button(master, text="Sign in", command=signing_in)
        gen_log.place(x=250, y=150)
        reg=Button(master,text="register user", command=register)
        reg.place(x=250,y=200)

l=Login_system(master)
master.mainloop()

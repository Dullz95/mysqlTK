import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import datetime, timedelta, date

mydb = mysql.connector.connect(user='root', password='yolo0909', host='127.0.0.1', database='lc_online',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
xy = mycursor.execute('select * from users')
for i in mycursor:
    print(i)
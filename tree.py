from tkinter import *
import tkinter as ttk


ws = Tk()
ws.title("PythonGuides")

tree = ttk.Treeview(ws, columns=(1, 2, 3), show='headings', height=20)
tree.pack()

tree.heading(1, text="ID")
tree.heading(2, text="Name")
tree.heading(3, text="Surname")
tree.heading(4, text="Phone")
tree.heading(1, text="Password")
tree.heading(4, text="Role")

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

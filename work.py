if self.usere.get() == "" or self.passwe.get() == "" or self.users_cb.get() == "":
    messagebox.showerror("Error", "Enter all fields")
else:
    for i in mycursor:
        if self.usere.get() not in i[1] and self.passwe.get() not in i[4]:
            messagebox.showerror("Error")

        else:

            for i in mycursor:
                if self.usere.get() == i[1] and self.passwe.get() == i[
                    4] and self.users_cb.get() == "lecturer" or "intern" or "visitor":
                    general_log_in_screen()
                    break
            for i in mycursor:
                if self.usere.get() == i[1] and self.passwe.get() == i[4] and self.users_cb.get() == "admin":
                    admin_screen()
                    break

                    heading = Label(administrator, text="Administrator", font=("Courier", 26, "italic"), bg="grey")
                    heading.place(x=210, y=10)

                    user_lbl = Label(administrator, text="Please enter username: ", bg="grey")
                    user_lbl.place(x=50, y=80)
                    user_entry = Entry(administrator)
                    user_entry.place(x=450, y=80)

                    frame1 = Frame(administrator, bg="grey", highlightbackground="white", highlightthickness=5,
                                   width=450, height=300)
                    frame1.place(x=25, y=190)

                    table = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6), show="headings")
                    table.pack()
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
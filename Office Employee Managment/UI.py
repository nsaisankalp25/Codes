def main():    
    rt = Tk()
    rt.title("Employee DataBase Manager")
    rt.geometry("1000x615")

    def backButton():
        def backmain():
            rt.destroy()
            main()
        Button(rt, text = "Back - Main Page", font = ('cambria', 12), fg = 'cyan', command = backmain).place(x = 800, y = 10)
    def loadfunc():
        for i in rt.winfo_children(): i.destroy()
        backButton()
        Label(rt, text = "SN", font = ("roboto mono", 12, "bold"), fg = "orange").place(x = 40, y = 10)
        Label(rt, text = "ID", font = ("roboto mono", 12, "bold"), fg = "orange").place(x = 90, y = 10)
        Label(rt, text = "NAME", font = ("roboto mono", 12, "bold"), fg = "orange").place(x = 150, y = 10)
        Label(rt, text = "AGE", font = ("roboto mono", 12, "bold"), fg = "orange").place(x = 255, y = 10)
        Label(rt, text = "GENDER", font = ("roboto mono", 12, "bold"), fg = "orange").place(x = 310, y = 10)
        Label(rt, text = "SECTOR", font = ("roboto mono", 12, "bold"), fg = "orange").place(x = 390, y = 10)
        Label(rt, text = "ROLE", font = ("roboto mono", 12, "bold"), fg = "orange").place(x = 500, y = 10)
        Label(rt, text = "DATE OF JOINING", font = ("roboto mono", 12, "bold"), fg = "orange").place(x = 600, y = 10)
        values = backend.DB.EmployeeInfo()
        if values[0] == "NONE":
            backend.erase_func()
            Label(rt, text = "DATABASE NOT FOUND: Created a new one, Hence, Data Lost...",
             fg = "red", font = ('consolas', 14, "bold")).place(x = 60, y = 50)
            Label(rt, text = "Kindly Enter New set of data, refer to Help Menu by pressing INFO Button",
             fg = "red", font = ('arial', 13)).place(x = 60, y = 100)
            Label(rt, text = "Please EXIT/TERMINATE the program before adding in employees data.", 
            fg = 'red', font = ("segoe ui", 14)).place(x = 60, y = 150)
            Button(rt, text = "Close", font = ('cambria', 12), fg = 'cyan', 
            command = lambda: rt.destroy()).place(x = 800, y = 45)
        else:       
            a = 0
            values = values[2:]
            for i in range(len(values)):
                Label(rt, text = values[i][0]).place(x = 50, y = 50+a)
                Label(rt, text = values[i][1]).place(x = 75, y = 50+a)
                Label(rt, text = values[i][2]).place(x = 145, y = 50+a)
                Label(rt, text = values[i][3]).place(x = 255, y = 50+a)
                Label(rt, text = values[i][4]).place(x = 330, y = 50+a)
                Label(rt, text = values[i][5]).place(x = 395, y = 50+a)
                Label(rt, text = values[i][6]).place(x = 505, y = 50+a)
                Label(rt, text = values[i][7]).place(x = 620, y = 50+a)
                a += 20
           
    def addfunc():
        for i in rt.winfo_children(): i.destroy()
        backButton()
        Label(rt, text = "Add Employee's Information", font = ("montserrat", 16),
         fg = 'blue').place(x = 100, y = 10)
        keys = backend.DB.EmployeeInfoParam()
        values = backend.DB.EmployeeInfo()
        a = 40
        for i in range(len(keys)):
            a += 40
            Label(rt, text = keys[i], font = ('calibri', 14), fg = 'brown').place(x = 40, y = a)
        def resure():
            showsmg = messagebox.askyesno("Confirm Submission", 'Are you sure?\nPlease recheck and confirm')
            if showsmg == 1:
                info_list = (SN_entry.get(), ID_entry.get(),NAME_entry.get(),
                AGE_entry.get(),GENDER_entry.get(),SECTOR_entry.get(),ROLE_entry.get(),
                DOJ_entry.get(),SALARY_entry.get(),ACCESS_entry.get() , 
                AWARDS_entry.get(),OTHERINFO_entry.get())
                backend.DB.AddEmployeeInfo(info_list)
                for i in rt.winfo_children(): i.destroy()
                Label(rt, text = "Please EXIT/TERMINATE the program inorder to update Info onto the App.", 
                fg = 'red', font = ("segoe ui", 14)).place(x = 60, y = 150)
                Button(rt, text = "Close", font = ('cambria', 12), fg = 'red', 
                command = lambda: rt.destroy()).place(x = 800, y = 45)

        SN_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        SN_entry.insert(0, "Serial Number")
        SN_entry.bind("<FocusIn>", lambda a: SN_entry.delete(0, END))
        SN_entry.place(x = 250, y = 80)
        ID_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        ID_entry.insert(0, "ID Number")
        ID_entry.bind("<FocusIn>", lambda a: ID_entry.delete(0, END))
        ID_entry.place(x = 250, y = 120)
        NAME_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        NAME_entry.insert(0, "Enter Name")
        NAME_entry.bind("<FocusIn>", lambda a: NAME_entry.delete(0, END))
        NAME_entry.place(x = 250, y = 160)
        AGE_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        AGE_entry.insert(0, "Enter Age")
        AGE_entry.bind("<FocusIn>", lambda a: AGE_entry.delete(0, END))
        AGE_entry.place(x = 250, y = 200)
        GENDER_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        GENDER_entry.insert(0, "GENDER  F/M")
        GENDER_entry.bind("<FocusIn>", lambda a: GENDER_entry.delete(0, END))
        GENDER_entry.place(x = 250, y = 240)
        SECTOR_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        SECTOR_entry.insert(0, "Enter Sector/field")
        SECTOR_entry.bind("<FocusIn>", lambda a: SECTOR_entry.delete(0, END))
        SECTOR_entry.place(x = 250, y = 280)
        ROLE_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        ROLE_entry.insert(0, "Enter Role")
        ROLE_entry.bind("<FocusIn>", lambda a: ROLE_entry.delete(0, END))
        ROLE_entry.place(x = 250, y = 320)
        DOJ_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        DOJ_entry.insert(0, "Date of Joining dd/mm/yy")
        DOJ_entry.bind("<FocusIn>", lambda a: DOJ_entry.delete(0, END))
        DOJ_entry.place(x = 250, y = 360)
        SALARY_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        SALARY_entry.insert(0, "Salary in INR")
        SALARY_entry.bind("<FocusIn>", lambda a: SALARY_entry.delete(0, END))
        SALARY_entry.place(x = 250, y = 400)
        ACCESS_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        ACCESS_entry.insert(0, "Access LEVEL A/B/C")
        ACCESS_entry.bind("<FocusIn>", lambda a: ACCESS_entry.delete(0, END))
        ACCESS_entry.place(x = 250, y = 440)
        AWARDS_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        AWARDS_entry.insert(0, "Awards Received /NA")
        AWARDS_entry.bind("<FocusIn>", lambda a: AWARDS_entry.delete(0, END))
        AWARDS_entry.place(x = 250, y = 480)
        OTHERINFO_entry = Entry(rt, fg = 'purple', font = ('cambria', 14))
        OTHERINFO_entry.insert(0, "Other Info /NA")
        OTHERINFO_entry.bind("<FocusIn>", lambda a: OTHERINFO_entry.delete(0, END))
        OTHERINFO_entry.place(x = 250, y = 520)
        submit_b = Button(rt, text = "ADD DATA", fg = 'red', command = resure).place(x = 200, y = 575)

    def infofunc():
        from backend import info_msg
        for i in rt.winfo_children(): i.destroy()
        Label(rt, text = info_msg, font = ("callester", 13)).place(x = 60, y = 60)

    Label(rt, text = "Employee DataBase Manager", font = ("montserrat",18), fg = 'blue').place(x = 190, y = 0)
    load_B = Button(rt, text = "Load Employees Data", font = ('quicksand', 13), 
    fg = "red", command = loadfunc).place(x = 100, y = 40)
    add_B = Button(rt, text = "Add Employees Data", font = ('quicksand', 13), 
    fg = "red", command = addfunc).place(x = 300, y = 40)
    rem_B = Button(rt, text = "Remove Employees Data", font = ('quicksand', 13), 
    fg = "red").place(x = 490, y = 40)
    info_b = Button(rt, text = "Info/Help", font = ("quicksand", 12),
    command = infofunc, fg = "green").place(x = 320, y = 100)    
    Button(rt, text = "Close", font = ('cambria', 12), fg = 'cyan',
     command = lambda: rt.destroy()).place(x = 800, y = 45)
    rt.mainloop()

if __name__ == "__main__":
    from tkinter import Label, Place, Entry, Tk, END, Button, messagebox
    try: 
        import backend
        backend.FilePresenceCheck()
        main()
    except ImportError:
        rt = Tk()
        rt.title("ERROR BOX")
        Label(rt, text = "File 'backend.py' Not found! \n Make sure Installation of app was correct\n Importance of 'backend.py': HIGH, Handles DB management", fg = 'red', font = ('ubuntu mono', 15, "bold")).pack()
        Button(rt, text = "Close", fg = 'orange', font = ("cambria", 14), command = lambda: rt.destroy()).pack()
        rt.mainloop()

    
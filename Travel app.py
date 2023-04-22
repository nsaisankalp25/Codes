import  tkinter
import tkinter.ttk
from tkinter import Button, Entry, IntVar, Label, StringVar, ttk
from PIL import Image, ImageTk


rt_ticket = tkinter.Tk()   
rt_ticket.title('Travel booking.com')
rt_ticket.geometry('862x400')
style = ('segoe ui', 15)
style2 = ('calibri', 13)
fromcities = StringVar()
tocities = StringVar()
timevar = StringVar()
modevar = StringVar()
typevar = StringVar()
type2var = StringVar()
time_dep_var_d = IntVar()
time_dep_var_m = StringVar()
main = []

cars_available = ('Uber','Ola','Wajahati','RTA','Super car')
car_seats = ('Normal','Super','Delux','Ultra','Shared')
bus_types = ('Bus trans','Yahoo','Wajahati','RTA','sleeper Busses')
bus_seats = ('Normal','Super','Delux', 'Sleeper')
Air_types = ('Indigo','Emirates','AirIndia','Ethihad','United')
Air_seats = ('Economy','Business','First')
ship_types = ('Maersk','Mediterranean \nShipping.Co',
            'Evergreen Line','COSCO Shipping','Orient Overseas')
ship_seats = ('Economy','Business','First', 'Super')
#ORDER: Name, Dep city, Des city, Time, Vehicle, MM/YYYY, DD, vehicle name, class


def proceed(e):
    def next_def():
        main.append(fromcities.get())
        main.append(tocities.get())
        main.append(timevar.get())
        main.append(modevar.get())
        main.append(time_dep_var_m.get())
        main.append(time_dep_var_d.get())
        main.append(type2var.get())
        #('Car', 'Bus', 'Airplane', 'Ship')

        for widgets in rt_ticket.winfo_children():
            widgets.destroy()
            
        def submitdef():
            
            main.append(typevar.get())
            main.append(type2var.get())
            print(main)
            for widgets in rt_ticket.winfo_children():
                widgets.destroy()
            def old_ticket():
                Label(rt_ticket, text = f"Passenger Name: {main[0]}").grid(row = 0, column = 0)
                Label(rt_ticket, text = f"from-to: {main[1]}-{main[2]}").grid(row = 1, column = 0)
                Label(rt_ticket, text = f"Time: {main[3]}").grid(row = 0, column = 1)
                Label(rt_ticket, text = f"Transporation: {main[7]}").grid(row = 2, column = 0)
                Label(rt_ticket, text = f"Date: {main[6]}/{main[5]}").grid(row = 2, column = 1)
                Label(rt_ticket, text = f"Class: {main[8]}").grid(row = 3, column = 0)
                Label(rt_ticket, text = "Travel Booking.com").grid(row = 3, column = 1)
           

            image1 = Image.open("ticket.png")
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(image=test)
            label1.image = test
            label1.grid(row = 0, column = 0)
            style3 = ('calibri', 20)
            #['Sai', 'Ajman', 'Umm Al Quwain', '0:30 AM', 'Ship', '2/2021', 4, '', 'Orient Overseas', 'Business']
            # 0       1            2              3        4       5         6   7   8                    9
            l1 = Label(rt_ticket, text = main[0], bg = '#d3a35e', font = style3)
            l1.place(x = 350, y = 47)
            l2 = Label(rt_ticket, text = main[1], bg = '#d3a35e', font = style3)
            l2.place(x = 50, y = 150)
            l3 = Label(rt_ticket, text = main[2], bg = '#d3a35e', font = style3)
            l3.place(x = 600, y = 150)
            l4 = Label(rt_ticket, text = main[3], bg = '#d3a35e', font = style3)
            l4.place(x = 100, y = 210)
            l5 = Label(rt_ticket, text = f'{main[6]}/{main[5]}', bg = '#d3a35e', font = style3)
            l5.place(x = 100, y = 250)
            l6 = Label(rt_ticket, text = main[8], bg = '#d3a35e', font = style3)
            l6.place(x = 180, y = 340)
            l7 = Label(rt_ticket, text = main[9], bg = '#d3a35e', font = style3)
            l7.place(x = 630, y = 330)
            l8 = Label(rt_ticket, text = main[4], bg = '#d3a35e', font = style3)
            l8.place(x = 650, y = 220)
            #Name, Dep_city, Des_city, Time, MMYYYY, DD, vehicle_name, seat_class

            #['Sai', 'Ajman', 'Umm Al Quwain', '0:30 AM', 'Ship', '2/2021', 4, '', 'Orient Overseas', 'Business']
            # 0       1            2              3        4       5         6   7   8                    9
            
            

        if modevar.get().lower() == 'car':

            print('car is selected')
            type_l = Label(rt_ticket, text = "Select a car company ", font = style2)
            type_l.grid(row = 0, column = 0)
            type_c = ttk.Combobox(rt_ticket, width = 12, textvariable = typevar)
            type_c['values'] = cars_available
            type_c.grid(row = 0, column = 1)
            type_c.current()
            
            type_c2_l = Label(rt_ticket, text = "Select Comfort_ticket: ", font = style2)
            type_c2_l.grid(row = 1, column = 0)
            type_c2 = ttk.Combobox(rt_ticket, width = 12, textvariable = type2var)
            type_c2['values'] = car_seats
            type_c2.grid(row = 1, column = 1)
            type_c2.current()

            sub_b = Button(rt_ticket, text = "Submit", command =  submitdef)
            sub_b.grid(row = 2, column = 1)


        elif modevar.get().lower() == 'bus':
            print('bus has been selected')

            type_l = Label(rt_ticket, text = "Select a bus company ", font = style2)
            type_l.grid(row = 0, column = 0)
            type_c = ttk.Combobox(rt_ticket, width = 12, textvariable = typevar)
            type_c['values'] = bus_types 
            type_c.grid(row = 0, column = 1)
            type_c.current()
            
            type_c2_l = Label(rt_ticket, text = "Select Comfort_ticket: ", font = style2)
            type_c2_l.grid(row = 1, column = 0)
            type_c2 = ttk.Combobox(rt_ticket, width = 12, textvariable = type2var)
            type_c2['values'] = bus_seats
            type_c2.grid(row = 1, column = 1)
            type_c2.current()

            sub_b = Button(rt_ticket, text = "Submit", command =  submitdef)
            sub_b.grid(row = 2, column = 1) 
         
        elif modevar.get().lower() == 'airplane':

            print('airplane has been selected')
            type_l = Label(rt_ticket, text = "Select a Airline company ", font = style2)
            type_l.grid(row = 0, column = 0)
            type_c = ttk.Combobox(rt_ticket, width = 14, textvariable = typevar)
            type_c['values'] = Air_types
            type_c.grid(row = 0, column = 1)  
            type_c.current()
            
            type_c2_l = Label(rt_ticket, text = "Select Comfort_ticket: ", font = style2)
            type_c2_l.grid(row = 1, column = 0)
            type_c2 = ttk.Combobox(rt_ticket, width = 12, textvariable = type2var)
            type_c2['values'] = Air_seats 
            type_c2.grid(row = 1, column = 1)
            type_c2.current()

            sub_b = Button(rt_ticket, text = "Submit", command =  submitdef)
            sub_b.grid(row = 2, column = 1) 
         
        elif modevar.get().lower() == 'ship':
            print('Ship has been selected')
                
            type_l = Label(rt_ticket, text = "Select a Ship company ", font = style2)
            type_l.grid(row = 0, column = 0)
            type_c = ttk.Combobox(rt_ticket, width = 18, textvariable = typevar)
            type_c['values'] = ship_types 
            type_c.grid(row = 0, column = 1)
            type_c.current()
            
            type_c2_l = Label(rt_ticket, text = "Select Comfort_ticket: ", font = style2)
            type_c2_l.grid(row = 1, column = 0)
            type_c2 = ttk.Combobox(rt_ticket, width = 12, textvariable = type2var)
            type_c2['values'] = ship_seats 
            type_c2.grid(row = 1, column = 1)
            type_c.current()

            sub_b = Button(rt_ticket, text = "Submit", command =  submitdef)
            sub_b.grid(row = 2, column = 1) 

        else:
            print(f'{modevar}this has been selected')
       



    name = name_e.get()
    main.append(name)
    name_e.destroy()
    name_l.destroy()
    intro.config(text = f"Hello {name}, please fill this form.")
    from_l = Label(rt_ticket, text = "Select depart_ticketure city to \n to destination city", font = style2)
    from_l.grid(row = 1, column = 0)
    cities = (
    "Abu Dhabi", 
    "Dubai", 
    "Sharjah", 
    "Ajman", 
    "Fujairah", 
    "Umm Al Quwain",
    "Al Ain")
    
    fromcities.set("Depart_ticketure City")
    tocities.set('Destination City')
    timevar.set('Time')
    modevar.set('Transport_ticket type')
    city_select = ttk.Combobox(rt_ticket, width = 12, textvariable = fromcities)
    city_select['values'] = cities
    city_select.grid(row = 1, column = 1)
    city_select.current()

    to_l = Label(rt_ticket, text = "-To-")
    to_l.grid(row = 1, column = 2)
    city_select2 = ttk.Combobox(rt_ticket, width = 12, textvariable = tocities)
    city_select2['values'] = cities
    city_select2.grid(row = 1, column = 3) 
    city_select2.current()
    time = ttk.Combobox(rt_ticket, width = 12, textvariable = timevar)
    time_list = [] 

    for i in range(24):
        if i >= 12:
            time_list.append(f"{str(i)}:00 PM")
            time_list.append(f"{str(i)}:15 PM")
            time_list.append(f"{str(i)}:30 PM")
            time_list.append(f"{str(i)}:45 PM")
        else:
            time_list.append(f"{str(i)}:00 AM")
            time_list.append(f"{str(i)}:15 AM")
            time_list.append(f"{str(i)}:30 AM")
            time_list.append(f"{str(i)}:45 AM")


    time_tuple = tuple(time_list)

    time['values'] = time_tuple
    time.grid(row = 2, column = 1)
    time.current() 
    time_l = Label(rt_ticket, text = "Select Time of Depart_ticketure", font = style2)
    time_l.grid(row = 2, column = 0)

    month_list = []
    for i in range(1, 12):
        month_list.append(f'{i}/2021')
    month = tuple(month_list)
    day_list = []
    for i in range(1, 31):
        day_list.append(i)
    day = tuple(day_list)
    


    dep_l = Label(rt_ticket, text = "Select Date of \nDepart_ticketure: ", font = style2)
    dep_l.grid(row = 3, column = 0)
    time_dep_var_d.set('Day')
    time_dep_var_m.set('MM/YYYY')

    time_d = ttk.Combobox(rt_ticket, width = 12, textvariable = time_dep_var_d)
    time_d['values'] = day
    time_d.grid(row = 3, column = 1)    
    time_d.current()

    time_m = ttk.Combobox(rt_ticket, width = 10, textvariable = time_dep_var_m)
    time_m['values'] = month
    time_m.grid(row = 3, column = 2)
    time_m.current()

    
    mode_l = Label(rt_ticket, text = "Select Mode of Transport_ticketation", font = style2)
    mode_l.grid(row = 4, column = 0)

    time = ttk.Combobox(rt_ticket, width = 12, textvariable = modevar)
    time['values'] = ('Car', 'Bus', 'Airplane', 'Ship')
    time.grid(row = 4, column = 1)
    time.current()

    next_b = Button(rt_ticket, text = "Next -->", font = style2, command = next_def)
    next_b.grid(row = 5, column = 2)
    


intro = Label(rt_ticket, text = "Welcome to \nTravel Booking.com", font = style)
intro.grid(row = 0, column = 0)
name_l = Label(rt_ticket, text = "Enter Name: ", font = style)
name_l.grid(row = 1, column = 0)
name_e = Entry(rt_ticket, font = style)
name_e.grid(row = 1, column = 1)
name_e.bind("<Return>", proceed)


rt_ticket.mainloop()

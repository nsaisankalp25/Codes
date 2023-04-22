import tkinter
from tkinter import Label, Button, Entry, Spinbox
from tkinter import Scale, OptionMenu, messagebox
from tkinter import DoubleVar, HORIZONTAL, StringVar

rt = tkinter.Tk()
rt.geometry("600x700")
rt.title("Application forms")


avar = DoubleVar()
dvar = DoubleVar()
mvar = DoubleVar()
yvar = DoubleVar()
click = StringVar()
gendrop = StringVar()
mondrop = StringVar()

def destroy_rt():
    rt.destroy()

def into_file():
    showsmg = messagebox.askyesno("Confirm Submission", 'Are you sure?\nPlease recheck and confirm')

    if showsmg == 1:
        my_file = "{}_file_info.txt".format(name_e.get())
        f = open(my_file, "w")
        
        
        name_i = name_e.get()
        age_i = age_s.get()
        global date
        date = dobds.get()
        if date < '32':
            d = 31
            try:
                global dmy
                dmy = f"{date}/{m}/{y}"
            except:
                dmy = f"{d}/{m}/{y}"
        m = mondrop.get()
        y = dobys.get()
        
        country = C_E.get()
        state = S_E.get()
        city = Ci_E.get()
        Dis = D_E.get()
        building = B_E.get()
        flat = F_E.get()
        cont = click.get()
        gender = gendrop.get()
            
        f.write(f"Name: {name_i}\n")
        f.write(f'Age: {age_i}\n')
        f.write(f'Date of Birth: {dmy}\n')
        f.write(f'Gender: {gender}\n')
        f.write(f'Continent: {cont}\n')
        f.write(f'Country: {country}\n')
        f.write(f'State: {state}\n')
        f.write(f'City: {city}\n')
        f.write(f'Dictrict: {Dis}\n')
        f.write(f'Building: {building}\n')
        f.write(f'Flat: {flat}\n')


        Submitb.destroy()
        Closeb = Button(rt, text = 'Close', command = destroy_rt, font = ('sans serrif', 12))
        Closeb.grid(row = 14, column = 1)
        f.close()
    
    else: 
        print('The answer has been no')

intro = Label(rt, text = 'Application', font = ('montserrat', 20))
intro.grid(row = 0, column = 0)

name_l = Label(rt, text = 'Enter your name: ', font = ('quicksand', 14))
name_l.grid(row = 1, column = 0)
name_e = Entry(rt, font = ('calibri', 14))
name_e.grid(row = 1, column = 1)

age_l = Label(rt, text = 'Enter your age', font = ('quicksand', 14))
age_l.grid(row = 2, column = 0)
age_s = Scale(rt, from_ = 0, to = 100, orient = HORIZONTAL, variable = avar,
sliderlength = 45, length = 250, width = 15, activebackground = 'yellow', fg = 'red',
troughcolor = 'grey')
age_s.grid(row = 2, column = 1)

dobdl = Label(rt, text = 'Enter your Date of birth [D]', font = ('quicksand', 14))
dobml = Label(rt, text = "Enter your Date of birth [M]", font = ('quicksand',14))
dobyl = Label(rt, text = 'Enter your Date of birth [Y]', font = ('quicksand', 14))
dobdl.grid(row = 3, column = 0)
dobml.grid(row = 4, column = 0)
dobyl.grid(row = 5, column = 0)

dobds = Spinbox(rt, from_ = 0, to = 31, font = ('calibri', 12))
dobds.grid(row = 3, column = 1)

genselect = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
mondrop.set("Select Month")
monthslider = OptionMenu(rt, mondrop, *genselect)
monthslider.grid(row = 4, column = 1)

dobys = Spinbox(rt, from_ = 100, to = 2100, font = ('calibri', 12))
dobys.grid(row = 5, column = 1)

continents = [
    "Asia",
    "Antarctica",
    "North America",
    'South America',
    "Europe",
    'Africa',
    'Asia',
    'Australia'
]


gendersel = [
    "Male",
    "Female"
]


gen_l = Label(rt, text = 'Select gender: ', font = ('quicksand',14))
gen_l.grid(row = 6, column = 0)
gendrop.set("Select Gender")
click.set("Select Continent")
gen_op = OptionMenu(rt, gendrop, *gendersel)
gen_op.grid(row = 6, column = 1)

dropl = Label(rt, text = 'Select CONTINENT :', font = ('quicksand', 14))
dropl.grid(row = 7, column = 0)

droped = OptionMenu(rt, click, *continents)
droped.grid(row = 7, column = 1)

C_l = Label(rt, text = 'Name of COUNTRY [living in]: ', font = ('quicksand', 14))
C_l.grid(row = 8, column = 0)
C_E = Entry(rt, font = ('calibri', 14))
C_E.grid(row = 8, column = 1)
S_l = Label(rt, text = 'Name of STATE [living in]: ', font = ('quicksand', 14))
S_l.grid(row = 9, column = 0)
S_E = Entry(rt, font = ('calibri', 14))
S_E.grid(row = 9, column = 1)
Ci_l = Label(rt, text = 'Name of CITY [living in]: ', font = ('quicksand', 14))
Ci_l.grid(row = 10, column = 0)
Ci_E = Entry(rt, font = ('calibri', 14))
Ci_E.grid(row = 10, column = 1)
D_l = Label(rt, text = 'Name of DISTRICT [living in]: ', font = ('quicksand', 14))
D_l.grid(row = 11, column = 0)
D_E = Entry(rt, font = ('calibri', 14))
D_E.grid(row = 11, column = 1)
B_l = Label(rt, text = 'Name of BUILDING [living in]: ', font = ('quicksand', 14))
B_l.grid(row = 12, column = 0)
B_E = Entry(rt, font = ('calibri', 14))
B_E.grid(row = 12, column = 1)
F_l = Label(rt, text = 'FLAT NUMBER [living in]: ', font = ('quicksand', 14))
F_l.grid(row = 13, column = 0)
F_E = Entry(rt, font = ('calibri', 14))
F_E.grid(row = 13, column = 1)

Submitb = Button(rt, text = 'Submit', command = into_file, font = ('sans serrif', 12))
Submitb.grid(row = 14, column = 0)

rt.mainloop()

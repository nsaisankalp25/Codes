#Temperature converter
import tkinter
from tkinter import Label, Entry, Button, Grid

rt = tkinter.Tk()

intro = Label(rt, text = 'Temperature converter')
intro.grid(row = 0, column = 0)

convert = Label(rt, text = 'Enter Value', fg = 'black',
bg = 'yellow', font = ('montserrat', 15))
convert.grid(row = 1, column = 0)

def ktfdef():
    try:
        a = float(majore.get())
        b = round(((1*a - 273.15) * 9/5 + 32 ), 3)
        print(b)
        totalans = Label(rt, text = f'Fahrenheit: {b}', fg = 'blue', bg = 'white', font = ('calibri', 14))
        totalans.grid(row = 2, column = 1)
        #totalans.config(text = f'Answer: {b}')
    except ValueError:
        print('Hmmm')

def ftkdef():
    try:
        a = float(majore.get())
        b = round(((1*a - 32) * 5/9 + 273.15), 3) 
        print(b)
        totalans = Label(rt, text = f'Kelvin: {b}', fg = 'blue', bg = 'white', font = ('calibri', 14))
        totalans.grid(row = 3, column = 1)
        #totalans.config(text = f'Answer: {b}')
    except ValueError:
        print('Hmmm')


def ftcdef():
    try:
        a = float(majore.get())
        b = round((1*a - 32) * 5/9, 3) 
        print(b)
        totalans = Label(rt, text = f'Celcius: {b}', fg = 'blue', bg = 'white', font = ('calibri', 14))
        totalans.grid(row = 4, column = 1)
    except ValueError:
        print('Hmmm')
    
def ctfdef():
    pass
    

majore = Entry(rt, font = ('montserrat', 15))
majore.grid(row = 1, column = 1)


ktf = Button(rt, text = 'Kelvin --> Fahrenheit', fg = 'black', 
bg = 'lightgreen', font = ('quicksand',15), command = ktfdef,
 activeforeground = 'black', activebackground = 'lightgreen')
ktf.grid(row = 2, column = 0)


ftk = Button(rt, text = 'Fahrenheit --> Kelvin', fg = 'black', 
bg = 'lightgreen', font = ('quicksand',15), command = ftkdef,
 activeforeground = 'black', activebackground = 'lightgreen')
ftk.grid(row = 3, column = 0)

ftc = Button(rt, text = 'Fahrenheit --> Celcius', fg = 'black', 
bg = 'lightgreen', font = ('quicksand',15), command = ftcdef,
 activeforeground = 'black', activebackground = 'lightgreen')
ftc.grid(row = 4, column = 0)



ctf = Button(rt, text = 'Celcius --> Fahrenheit', fg = 'black', 
bg = 'lightgreen', font = ('quicksand',15), command = ctfdef,
 activeforeground = 'black', activebackground = 'lightgreen')
ctf.grid(row = 5, column = 0)


ktc = Button(rt, text = 'Kelvin --> Celcius', fg = 'black', 
bg = 'lightgreen', font = ('quicksand',15), #command = #ktcdef,
 activeforeground = 'black', activebackground = 'lightgreen')
ktc.grid(row = 6, column = 0)

ctk = Button(rt, text = 'Celcius --> Kelvin', fg = 'black', 
bg = 'lightgreen', font = ('quicksand',15), #command = #ctkdef,
 activeforeground = 'black', activebackground = 'lightgreen')
ctk.grid(row = 7,  column = 0)





rt.mainloop()





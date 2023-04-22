import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Place
rt  = tkinter.Tk()
rt.configure(bg = '#B0C4DE')
rt.geometry("500x500")

rt.title('Sai simple CALCULATOR')
ent1 = Label(rt, text = '1st number: ', bg = '#B0C4DE', font = ('Arial',12)) # One of my first python codes :-)
ent1.grid(row = 0, column = 0)
ent2 = Label(rt, text = '2nd number: ', bg = '#B0C4DE', font = ('Arial',12))
ent2.grid(row = 1, column = 0)
num1 = Entry(text = 'Enter first NUMBER', bg = '#bacade', fg = 'brown',
font = ('helvetica',18, 'bold'))
num2 = Entry(text = 'Enter second NUMBER', bg = '#bacade', fg = 'brown',
font = ('helvetica',18, 'bold'))

def addcom():
    try:
        fnum1 = float(num1.get())
        fnum2 = float(num2.get())
        add = fnum1 + fnum2
        addddd =  round(add,3)
        adddd = 'Sum:',  addddd
        mylabel = Label(font = ('arial',12), text=  adddd)
        mylabel.place(x = 110, y = 103)
    except ValueError:
        idk = Label(text = 'Only one number entered', font = ('quicksand', 11, 'bold'))
        idk2 = Label(text = 'or', font = ('quicksand', 11, 'bold'))
        idk2.place(x = 20, y = 385)
        idk3 = Label(text = 'non-numbers(letters or signs) has been entered', font = ('quicksand', 11, 'bold'))
        idk3.place(x = 20, y = 425)
        idk.place(x = 20, y = 350)

def subcom():
    try:
        fnum1 = float(num1.get())
        fnum2 = float(num2.get())
        sssub = (fnum1 - fnum2)
        ssuub = round(sssub,3)
        ssub = 'Subtracted:', ssuub
        mylabel = Label(text= ssub, font = ('arial', 12))
        mylabel.place(x = 110, y = 138)
    except ValueError:
        idk = Label(text = 'Only one number entered', font = ('quicksand', 11, 'bold'))
        idk2 = Label(text = 'or', font = ('quicksand', 11, 'bold'))
        idk2.place(x = 20, y = 385)
        idk3 = Label(text = 'non-numbers(letters or signs) has been entered', font = ('quicksand', 11, 'bold'))
        idk3.place(x = 20, y = 425)
        idk.place(x = 20, y = 350)

def divcom():
    try:
        fnum1 = float(num1.get())
        fnum2 = float(num2.get())
        div = fnum1/fnum2
        divv = round(div,3)
        divv = 'Quotient:', divv

        mylabel = Label(font = ('arial',12),text= divv )

        mylabel.place(x = 110, y = 178)
    except ValueError:
        idk = Label(text = 'Only one number entered', font = ('quicksand', 11, 'bold'))
        idk2 = Label(text = 'or', font = ('quicksand', 11, 'bold'))
        idk2.place(x = 20, y = 385)
        idk3 = Label(text = 'non-numbers(letters or signs) has been entered', font = ('quicksand', 11, 'bold'))
        idk3.place(x = 20, y = 425)
        idk.place(x = 20, y = 350)

def mulcom():
    try:
        fnum1 = float(num1.get())
        fnum2 = float(num2.get())
        mul = 'Product:', round((fnum1 * fnum2), 3)
        mylabel = Label(font = ('arial',12),text=  mul )
        mylabel.place(x = 110, y = 213)
    except ValueError:
        idk = Label(text = 'Only one number entered', font = ('quicksand', 11, 'bold'))
        idk2 = Label(text = 'or', font = ('quicksand', 11, 'bold'))
        idk2.place(x = 20, y = 385)
        idk3 = Label(text = 'non-numbers(letters or signs) has been entered', font = ('quicksand', 11, 'bold'))
        idk3.place(x = 20, y = 425)
        idk.place(x = 20, y = 350)

def powcom():
    try:
        fnum1 = float(num1.get())
        fnum2 = float(num2.get())
        powr = 'Power:', round((fnum1 **  fnum2) ,4)
        mylabel = Label(font = ('arial',12),text= powr )
        mylabel.place(x = 110, y = 248)
    except ValueError:
        idk = Label(text = 'Only one number entered', font = ('quicksand', 11, 'bold'))
        idk2 = Label(text = 'or', font = ('quicksand', 11, 'bold'))
        idk2.place(x = 20, y = 385)
        idk3 = Label(text = 'non-numbers(letters or signs) has been entered', font = ('quicksand', 11, 'bold'))
        idk3.place(x = 20, y = 425)
        idk.place(x = 20, y = 350)

def factcom():
    try:
        fnum1 = int(num1.get())
        if fnum1 >= 101:
            Label(text = 'Its a huge number, try a number less that 100').grid(row = 13, column = 1)
        else:
            for i in range(1,fnum1*1):
                fnum1 = fnum1 * i

            ffnum1 = 'factorial:', round(fnum1, 4)
            mylabel = Label(font = ('arial',12),text = ffnum1)
            mylabel.place(x = 110, y = 283)
    except ValueError:
        idk = Label(text = 'Only one number entered', font = ('quicksand', 11, 'bold'))
        idk2 = Label(text = 'or', font = ('quicksand', 11, 'bold'))
        idk2.place(x = 20, y = 385)
        idk3 = Label(text = 'non-numbers(letters or signs) has been entered', font = ('quicksand', 11, 'bold'))
        idk3.place(x = 20, y = 425)
        idk.place(x = 20, y = 350)

def rootcom():
    try:
        fnum1 = float(num1.get())
        fnum2 = float(num2.get())
        fnum1 = fnum1**(1/fnum2)
        ffnum1 = 'Root:', round(fnum1, 4)
        mylabel = Label(font = ('arial',12),text =ffnum1 )
        mylabel.place(x = 110, y = 318)
    except ValueError:
        idk = Label(text = 'Only one number entered', font = ('quicksand', 11, 'bold'))
        idk2 = Label(text = 'or', font = ('quicksand', 11, 'bold'))
        idk2.place(x = 20, y = 385)
        idk3 = Label(text = 'non-numbers(letters or signs) has been entered', font = ('quicksand', 11, 'bold'))
        idk3.place(x = 20, y = 425)
        idk.place(x = 20, y = 350)

def des():
    rt.destroy()
    print('The window is closed.')
    



addsubbut = Button(text = 'ADD', command = addcom, fg = 'red', bg = 'pink', 
padx = 14, pady = 3, activebackground = 'pink', activeforeground = 'red')

subsubbut = Button(text = 'Subtract', command = subcom,  fg = 'red', bg = 'pink',
padx = 4, pady = 3, activebackground = 'pink', activeforeground = 'red')

divsubbut = Button(text = 'Divide', command = divcom, fg = 'red', bg = 'pink',
padx = 9.45, pady = 3, activebackground = 'pink', activeforeground = 'red')

mulsubbut = Button(text = 'Multiply', command = mulcom,  fg = 'red', bg = 'pink',
padx = 4.25, pady = 3, activebackground = 'pink', activeforeground = 'red')

powsubbut = Button(text = 'Power', command = powcom, fg = 'red', bg = 'pink', 
padx = 10, pady = 3, activebackground = 'pink', activeforeground = 'red')

factbut = Button(text = 'Factorial', command = factcom, fg = 'red', bg = 'pink', 
padx = 4, pady = 3, activebackground = 'pink', activeforeground = 'red')

rootbut = Button(text = 'ROOT', command = rootcom, fg = 'red', bg = 'pink', 
padx = 11, pady = 3, activebackground = 'pink', activeforeground = 'red')

close = Button(text = 'Close', command = des, fg = 'red', bg = 'pink',
padx = 11, pady = 4, activeforeground = 'red', activebackground = 'pink')

addsubbut.place(x = 20, y = 100)
subsubbut.place(x = 20, y = 135)
divsubbut.place(x = 20, y = 170)
mulsubbut.place(x = 20, y = 205)
powsubbut.place(x = 20, y = 240)
factbut.place(x = 20, y = 275)
rootbut.place(x = 20, y = 310)
close.place(x = 100, y = 350)


num1.grid(row = 0, column = 1)
num2.grid(row = 1, column = 1)


rt.mainloop()
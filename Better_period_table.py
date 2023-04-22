import tkinter
from tkinter import *

rt_table = tkinter.Tk()
rt_table.title('Periodic Table')
rt_table.geometry('1000x600')

file = open('elements.txt', 'r')
elements_list = []

def search(key):
    get_user = search_e.get()
    search_e.delete(0, END)
    for i in elements_list:
        i = i.split()
        if get_user in i:
            err.config(text = "\t\t\n\t\t\n\t\t\n")
            put2 = Label(rt_table, text = "\t\t\n\t\t\n\t\t\n", font = ('calibri', 18))
            put2.place(x = 200, y = 60)
            put = Label(rt_table, text = f"Number: {i[0]}\nSymbol: {i[1]}\nName: {i[2]}",
             font = ('montserrat', 14), fg = 'blue')
            put.place(x = 200, y = 60)
            break
        else:
            err.config(text = 'Incorrect Input(s)')
            continue

for i in file:
    i = i.rstrip()
    i = i.lstrip()
    i = i.replace('\n', ' ')
    i = i.replace('\t', ' ')
    elements_list.append(i)
print(elements_list)
style = ('calibri', 20)
style2 = ('calibri', 17)
for a in range(1, 16):
    Label(rt_table, text = "     ", font = style).grid(row = 0, column = a)

def btnclick(num):
    num = str(num)
    for i in elements_list:
        i = i.split()
        if num in i:
            err.config(text = "\t\t\n\t\t\n\t\t\n")
            put2 = Label(rt_table, text = "\t\t\n\t\t\n\t\t", font = ('calibri', 22), bg = '#f0f0f0')
            put2.place(x = 200, y = 60)
            put = Label(rt_table, text = f"Number: {i[0]}\nSymbol: {i[1]}\nName: {i[2]}",
             font = ('montserrat', 14), fg = 'blue')
            put.place(x = 200, y = 60)
            break
        else:
            err.config(text = 'Incorrect Input(s)')
            continue

Button(rt_table, text = "1", font = style,
command=lambda:btnclick(1)).grid(row = 0, column = 0)
Button(rt_table, text = '2', font = style,
command=lambda:btnclick(2)).grid(row = 0, column = 17)
Button(rt_table, text = '3', font = style,
command=lambda:btnclick(3)).grid(row = 1, column = 0)
Button(rt_table, text = "4", font = style,
command=lambda:btnclick(4)).grid(row = 1, column = 1)
Button(rt_table, text = '11', font = style,
command=lambda:btnclick(11)).grid(row = 2, column = 0)
Button(rt_table, text = "12", font = style,
command =lambda:btnclick(12)).grid(row = 2, column = 1)
Button(rt_table, text = "55", font = style,
command =lambda:btnclick(55)).grid(row = 5, column = 0)
Button(rt_table, text = "56", font = style,
command =lambda:btnclick(56)).grid(row = 5, column = 1)
Button(rt_table, text = "87", font = style,
command =lambda:btnclick(87)).grid(row = 6, column = 0)
Button(rt_table, text = "88", font = style,
command =lambda:btnclick(88)).grid(row = 6, column = 1)
Label(rt_table, text = "**", font = style).grid(row = 5, column = 2)
Label(rt_table, text = "**", font = style).grid(row = 6, column = 2)

first = [5,6,7,8,9,10]
second = [13,14,15,16,17,18]
third = []
fort_tableh = []
fifth = []
sixth = []
seventh = []
eighth = []
for ab in range(19,37):
    third.append(ab)

for ae in range(37,55):
    fort_tableh.append(ae)

for aa2 in range(72, 87):
    fifth.append(aa2)

for aa3 in range(104, 119):
    sixth.append(aa3)

for a4 in range(57, 72):
    seventh.append(a4)

for a5 in range(89, 104):
    eighth.append(a5)
button_dict = {}
for i in first:   
    def action(x=i): 
        btnclick(str(x))

    button_dict[i] = Button(rt_table, text = i, font = style,
                               command = action).grid(row = 1, column = i+7)

for ii in second:
	def action(x = ii): 
		btnclick(str(x))
	
	button_dict[ii] = Button(rt_table, text = ii, font = style,
                               command = action).grid(row = 2, column = ii-1)

for i2 in third:
	def action(x = i2): 
		btnclick(str(x))
	
	button_dict[i2] = Button(rt_table, text = i2, font = style,
                               command = action).grid(row = 3, column = i2-19)

for i3 in fort_tableh:
    def action(x = i3):
        btnclick(str(x))

    button_dict[i3] = Button(rt_table, text = i3, font = style,
                               command = action).grid(row = 4, column = i3-37)

for i4 in fifth:
    def action(x = i4):
        btnclick(str(x))

    button_dict[i3] = Button(rt_table, text = i4, font = style,
                               command = action).grid(row = 5, column = i4-69)

for i5 in sixth:
    def action(x = i5):
        btnclick(str(x))

    button_dict[i3] = Button(rt_table, text = i5, font = style2 ,
                               command = action).grid(row = 6, column = i5-101)

for i6 in seventh:
    def action(x = i6):
        btnclick(str(x))

    button_dict[i3] = Button(rt_table, text = i6, font = style,
                               command = action).grid(row = 8, column = i6-56)

for i7 in eighth:
    def action(x = i7):
        btnclick(str(x))

    button_dict[i3] = Button(rt_table, text = i7, font = style2,
                               command = action).grid(row = 9, column = i7-88)

emp = Label(rt_table, text = "", font = style)
emp.grid(row = 7, column = 0)
err = Label(rt_table,text = '', fg = 'red')
err.place(x = 200, y = 60)

search_l = Label(rt_table, text = "Search any Periodic element: ", font = style)
search_l.place(x = 100, y = 20)

search_e = Entry(rt_table, font = style)
search_e.place(x = 450, y = 20)
search_e.bind('<Return>', search)

rt_table.mainloop()

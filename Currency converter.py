    
from google_currency import convert
import tkinter
from tkinter import *

rt = tkinter.Tk()

display_l = Label( text = '', 
font = ('montserrat', 15), fg = '#2BCA20')
display_l.grid(row = 6, column = 0) 


def convert_def():
    try:
        money_from  = currency_get_e.get()
        money_to = currency_to_e.get()
        amount = float(amount_e.get())
        send = convert(money_from.lower(), money_to.lower(), amount)
        a = send.split()
        a = a[5]
        a = a.replace(',', '')
        a = a.replace("\"", '')      
        display_l.config(text = f'Amount:  {a}') 
                
               
        
    except ValueError:
        Label(rt, text = "Invalid Value(s) entered").grid(row = 5, column = 1)


style = ('consolas', 18)

currency_get_l = Label(rt, text = "Enter Currency to be converted:",
fg = '#0004FF', font = style)
currency_get_l.grid(row = 1, column = 0)
currency_get_e = Entry(rt, font = style)
currency_get_e.grid(row = 1 ,column = 1)

empty_l = Label(rt, text = "_________").grid(row = 2, column = 0)

currency_to_l = Label(rt, text = "Enter Name of Currency:", 
fg = '#AA00FF', font = style).grid(row = 3, column = 0)
currency_to_e = Entry(rt, font = style, fg = '#AA00FF')
currency_to_e.grid(row = 3, column = 1)

amount_l = Label(rt, text = "Enter Amount: ", font  = style)
amount_l.grid(row = 4, column = 0)
amount_e = Entry(rt, fg = '#FF4900', font = style)
amount_e.grid(row = 4, column = 1)


submit_b = Button(rt, text = "Convert!", font = ('fira code', 15),
fg = '#FF4900', command = convert_def).grid(row = 2, column = 1)

rt.mainloop()
# print(convert("usd", "aed", 10))
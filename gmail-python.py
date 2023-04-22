import smtplib
import email
from email.message import EmailMessage
import os
import tkinter
from tkinter import Label, Grid, Text, Button, END, Entry
rt = tkinter.Tk()

def submitdef():
    tksub = sub_e.get()
    tkcontent = con_t.get(1.0, END)
    E_ad = os.environ.get("EMAIL_USER")
    E_Pass = os.environ.get("EMAIL_PASS")

    #Need to do TKSUB, TKCONTENT

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(E_ad, E_Pass)

        subject = f'Subject: {tksub}'
        body = f'Body: {tkcontent}'

        msg = f'{subject} \n\n{body}'

        smtp.sendmail(E_ad, 'saisankalp25@gmail.com', msg)




sub_l = Label(rt, text = 'Enter Subject: ')
sub_l.grid(row = 0, column = 0)

sub_e = Entry(rt)
sub_e.grid(row = 0, column = 1)

con_l = Label(rt, text = 'Enter Content: ')
con_l.grid(row = 1, column = 0)

con_t = Text(rt, height = 10, width = 14)
con_t.grid(row = 1, column = 1)

submit = Button(rt, text = 'Submit', command = submitdef)
submit.grid(row = 2, column = 0)




rt.mainloop()
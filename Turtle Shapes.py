import turtle as tr 
import tkinter
from tkinter import Button

win = tr.Screen()
win.bgcolor('#EDEDED')
win.title('Shapes Drawer')
rt = tkinter.Tk()
rt.geometry('200x200')
rt.title('Shapes Generator')
rt.configure(bg = 'white')



tt = tr.Turtle()
#tt.hideturtle()
tt.pencolor('red')
tt.color('red','yellow')
tt.speed(5)
tt.setheading(0)

def circledef():
    tt.pencolor('red')
    tt.color('red','yellow')
    tt.setheading(0)
    tt.clear()
    print("Currently in Circledef")
    tt.pensize(2)
    tt.begin_fill()
    tt.goto(0,0)
    tt.circle(100)
    tt.end_fill()
    tt.penup()

def rectangledef():
    tt.setheading(0)
    tt.clear()
    tt.penup()
    tt.begin_fill()
    tt.goto(-250,-125)
    tt.pendown()
    for i in range(2):
        tt.forward(500)
        tt.left(90)
        tt.forward(250)
        tt.left(90)                                         
        print(i)
    tt.end_fill()
    tt.penup()

def squaredef():
    tt.clear()
    tt.setheading(0)
    tt.penup()
    tt.goto(-125,-125)
    tt.pendown()
    tt.begin_fill()
    for i in range(4):
        tt.forward(250)
        tt.left(90)
        print(i)
    tt.end_fill()
    tt.penup()
        
def triangledef():
    tt.clear()
    tt.setheading(0)
    tt.penup()
    tt.goto(-100,-120)
    tt.pendown()
    tt.begin_fill()
    tt.forward(200)
    tt.left(120)
    tt.forward(200)
    tt.left(120)
    tt.forward(200)
    tt.end_fill()
    tt.penup()


def alldesdef():
    rt.destroy()
    win._destroy()


CB = Button(rt, text = 'Circle', command = circledef, padx = 12,
fg = 'red', bg = 'lightskyblue', activeforeground = 'red', activebackground = 'lightskyblue')
CB.grid(row = 0, column = 0)

RectB = Button(rt, text = 'Rectangle', command = rectangledef,
fg = 'red', bg = 'lightskyblue', activeforeground = 'red', activebackground = 'lightskyblue')
RectB.grid(row = 0, column = 1)

SqB = Button(rt, text = 'square', command = squaredef, padx = 9,
fg = 'red', bg = 'lightskyblue', activeforeground = 'red', activebackground = 'lightskyblue')
SqB.grid(row = 1, column = 0)

TriB = Button(rt, text = 'Triangle', command = triangledef, padx = 7,
fg = 'red', bg = 'lightskyblue', activeforeground = 'red', activebackground = 'lightskyblue')
TriB.grid(row = 1, column = 1)

win.mainloop()


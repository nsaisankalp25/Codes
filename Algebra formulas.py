import tkinter 
from tkinter import Entry, Label, Button
from tkinter import Grid, Place


rt = tkinter.Tk()
rt.configure(bg = '#FEEAD8')
rt.title('Algebra Identities')
rt.geometry("900x450")

intro = Label(rt, text = 'Welcome to Algebraic formulaes calculator!'
, fg = 'red', font = ('calibri', 20))
intro.grid(row = 0, column = 1)

emp = Label(rt, text = '', font = ('arial',30), bg = '#FEEAD8')
emp.grid(row = 1, column = 0)

def errdef():
        print('Non-Numbers has been entered')
        err = Label(rt, text = 'Pls enter a number', fg = 'white', bg = 'black',
                    font = ('arial', 12))
        err.grid(row = 5, column = 1)

def Equation1():
    global eql1
    global aknow
    global bknow
    global Al
    global Bl
    global Answer
    global subB


    eq1l = Label(rt, text = '(a^2)×(x^2)+(2*abxy)×(b^2*y^2)', fg = 'black', 
    bg = 'LightSkyBlue', font = ('montserrat', 18))
    eq1l.grid(row = 1, column = 1)


    aknow = Label(rt, text = 'Enter the Value of A', fg = 'darkorange', bg = '#FEEAD8',
    font = ('montserrat',16))
    aknow.grid(row = 2, column = 0)

    bknow = Label(rt, text = 'Enter the Value of B', fg = 'darkorange', bg = '#FEEAD8',
    font = ('montserrat',16))
    bknow.grid(row = 3, column = 0)


    Al = Entry(rt, font = ('comic sans', 20), width = 8)
    Al.grid(row = 2, column = 1)

    Bl = Entry(rt, font = ('comic sans', 20), width = 8)
    Bl.grid(row = 3, column = 1)

    def Answer():
        try:
            global anum
            global bnum
            anum = float(Al.get())
            bnum = float(Bl.get())
            if anum % int(anum) == 0:
                if bnum % int(bnum) == 0:
                    anum = int(anum)
                    bnum = int(bnum)
                    print('First if statement')
                    ans = ('{} *x^2 + {}* x*y + {} *y^2').format(anum**2, 2*anum*bnum, bnum**2)
                    ansl = Label(rt,text = f'Answer: {ans}' ,font = ('calibri', 18))
                    ansl.grid(row = 4, column = 1)
                
            elif bnum % int(bnum) == 0:
                bnum = int(bnum)
                print('in elif')
                ans = ('{} *x^2 + {}* x*y + {} *y^2').format(anum**2, 2*anum*bnum, bnum**2)
                ansl = Label(rt,text = f'Answer: {ans}' ,font = ('calibri', 18))
                ansl.grid(row = 4, column = 1)
                
            
            else: 
                print('nothing happened')
                ans = ('{} *x^2 + {}* x*y + {} *y^2').format(anum**2, 2*anum*bnum, bnum**2)
                ansl = Label(rt,text = f'Answer: {ans}' ,font = ('calibri', 18))
                ansl.grid(row = 4, column = 1)

        except ValueError:
            print('Its an Error')
            errl = Label(rt, text = 'Only Enter a number', fg = 'white', font = ('arial', 16), bg = '#FEEAD8')
            errl.grid(row = 3, column = 2)

    subB = Button(rt, text = 'Submit', fg = 'LightSkyBlue', bg = 'black',
                font = ('montserrat', 15), command = Answer)
    empp = Label(rt, text = '                                                     ', bg ='#FEEAD8', font = ('quicksand', 80))
    empp.grid(row = 200, column = 100)
    subB.grid(row = 2, column = 2)

def Equation2():
    global eql2
    global aknow2
    global bknow2
    global Al2
    global Bl2
    global Answer2
    global subB2
    print('In equation 2')
    eq2l = Label(rt, text = '(a^2)×(x^2)-(2*abxy)×(b^2*y^2)', fg = 'black', 
    bg = 'LightSkyBlue', font = ('montserrat', 18))
    eq2l.grid(row = 1, column = 1)


    aknow2 = Label(rt, text = 'Enter the Value of A', fg = 'darkorange', bg = '#FEEAD8',
    font = ('montserrat',16))
    aknow2.grid(row = 2, column = 0)

    bknow2 = Label(rt, text = 'Enter the Value of B', fg = 'darkorange', bg = '#FEEAD8',
    font = ('montserrat',16))
    bknow2.grid(row = 3, column = 0)


    Al2 = Entry(rt, font = ('comic sans', 20), width = 8)
    Al2.grid(row = 2, column = 1)

    Bl2 = Entry(rt, font = ('comic sans', 20), width = 8)
    Bl2.grid(row = 3, column = 1)

    

    def Answer2():
        try:
            global anum2
            global bnum2
            anum2 = float(Al2.get())
            bnum2 = float(Bl2.get())
            if anum2 % int(anum2) == 0:
                if bnum2 % int(bnum2) == 0:
                    anum2 = int(anum2)
                    bnum2 = int(bnum2)
                    print('First if statement')
                    ans2 = ('{} *x^2 - {}* x*y + {} *y^2').format(anum2**2, 2*anum2*bnum2, bnum2**2)
                    ansl2 = Label(rt,text = f'Answer: {ans2}' ,font = ('calibri', 18))
                    ansl2.grid(row = 4, column = 1)
                
            elif bnum2 % int(bnum2) == 0:
                bnum2 = int(bnum2)
                print('in elif')
                ans2 = ('{} *x^2 - {}* x*y + {} *y^2').format(anum2**2, 2*anum2*bnum2, bnum2**2)
                ansl2 = Label(rt,text = f'Answer: {ans2}' ,font = ('calibri', 18))
                ansl2.grid(row = 4, column = 1)
                
            
            else: 
                print('nothing happened')
                ans2 = ('{} *x^2 - {}* x*y + {} *y^2').format(anum2**2, 2*anum2*bnum2, bnum2**2)
                ansl2 = Label(rt,text = f'Answer: {ans2}' ,font = ('calibri', 18))
                ansl2.grid(row = 4, column = 1)

        except ValueError:
            print('Its an Error')
            errl2 = Label(rt, text = 'Only Enter a number', fg = 'white', font = ('arial', 16), bg = '#FEEAD8')
            errl2.grid(row = 3, column = 2)

    subB2 = Button(rt, text = 'Submit', fg = 'LightSkyBlue', bg = 'black',
                font = ('montserrat', 15), command = Answer2)
    subB2.grid(row = 2, column = 2)
    empp = Label(rt, text = '                                                     ', bg ='#FEEAD8', font = ('quicksand', 80))
    empp.grid(row = 200, column = 100)

def Equation4():    
    global eql2
    global aknow2
    global bknow2
    global Al2
    global Bl2
    global Answer2
    global subB2
    print('In equation 3')
    eq = '(ax + by + cz)^2'
    eq2l = Label(rt, text = '(ax + by + cz)^2', fg = 'black', 
    bg = 'LightSkyBlue', font = ('montserrat', 18))
    eq2l.grid(row = 1, column = 1)


    aknow2 = Label(rt, text = 'Enter the Value of A', fg = 'darkorange', bg = '#FEEAD8',
    font = ('montserrat',16))
    aknow2.grid(row = 2, column = 0)

    bknow2 = Label(rt, text = 'Enter the Value of B', fg = 'darkorange', bg = '#FEEAD8',
    font = ('montserrat',16))
    bknow2.grid(row = 3, column = 0)

    cknow2 = Label(rt, text = 'Enter the Value of C', fg = 'darkorange', bg = '#FEEAD8',
    font = ('montserrat',16))
    cknow2.grid(row = 4, column = 0)

    


    Al2 = Entry(rt, font = ('comic sans', 20), width = 8)
    Al2.grid(row = 2, column = 1)

    Bl2 = Entry(rt, font = ('comic sans', 20), width = 8)
    Bl2.grid(row = 3, column = 1)

    Cl2 = Entry(rt, font = ('comic sans', 20), width = 8)
    Cl2.grid(row = 4, column = 1)

    

    def Answer2():
        try:
            global anum2
            global bnum2
            global cnum2

            anum2 = float(Al2.get())
            bnum2 = float(Bl2.get())
            cnum2 = float(Cl2.get())
            if anum2 % int(anum2) == 0:
                if bnum2 % int(bnum2) == 0:
                    anum2 = int(anum2)
                    bnum2 = int(bnum2)
                    if cnum2 % int(cnum2) == 0:
                        cnum2 = int(cnum2)
                    print('First if statement')
                    ans2 = (f'({anum2}*x + {bnum2}*y + {cnum2}*z)^2')
                    ansl2 = Label(rt,text = f'Answer: {ans2}' ,font = ('calibri', 18))
                    ansl2.grid(row = 5, column = 1)
                
            elif bnum2 % int(bnum2) == 0:
                bnum2 = int(bnum2)
                if cnum2 % int(cnum2) == 0:
                    cnum2 = int(cnum2)
                print('in elif')
                ans2 = (f'({anum2}*x + {bnum2}*y + {cnum2}*z)^2')
                ansl2 = Label(rt,text = f'Answer: {ans2}' ,font = ('calibri', 18))
                ansl2.grid(row = 5, column = 1)
            
            elif cnum2 % int(cnum2) == 0:
                cnum2 = int(cnum2)
                ans2 = (f'({anum2}*x + {bnum2}*y + {cnum2}*z)^2')
                ansl2 = Label(rt,text = f'Answer: {ans2}' ,font = ('calibri', 18))
                ansl2.grid(row = 5, column = 1)

            
            else: 
                print('nothing happened')
                ans2 = (f'({anum2}*x + {bnum2}*y + {cnum2}*z)^2')
                ansl2 = Label(rt,text = f'Answer: {ans2}' ,font = ('calibri', 18))
                ansl2.grid(row = 5, column = 1)

        except ValueError:
            print('Its an Error')
            errl2 = Label(rt, text = 'Only Enter a number', fg = 'white', font = ('arial', 16), bg = '#FEEAD8')
            errl2.grid(row = 3, column = 2)

    subB2 = Button(rt, text = 'Submit', fg = 'LightSkyBlue', bg = 'black',
                font = ('montserrat', 15), command = Answer2)
    subB2.grid(row = 2, column = 2)
    empp = Label(rt, text = '                                                     ', bg ='#FEEAD8', font = ('quicksand', 80))
    empp.grid(row = 200, column = 100)

def Equation3():
    global eql2
    global aknow2
    global bknow2
    global Al2
    global Bl2
    global Answer2
    global subB2
    print('In equation 3')
    eq = '(ax-by)×(ax-by) = (a^2 × x^2) - (b^2 × y^2)'
    eq2l = Label(rt, text = '(a^2 × x^2) - (b^2 × y^2)', fg = 'black', 
    bg = 'LightSkyBlue', font = ('montserrat', 18))
    eq2l.grid(row = 1, column = 1)


    aknow2 = Label(rt, text = 'Enter the Value of A', fg = 'darkorange', bg = '#FEEAD8',
    font = ('montserrat',16))
    aknow2.grid(row = 2, column = 0)

    bknow2 = Label(rt, text = 'Enter the Value of B', fg = 'darkorange', bg = '#FEEAD8',
    font = ('montserrat',16))
    bknow2.grid(row = 3, column = 0)


    Al2 = Entry(rt, font = ('comic sans', 20), width = 8)
    Al2.grid(row = 2, column = 1)

    Bl2 = Entry(rt, font = ('comic sans', 20), width = 8)
    Bl2.grid(row = 3, column = 1)

    

    def Answer2():
        try:
            global anum2
            global bnum2
            anum2 = float(Al2.get())
            bnum2 = float(Bl2.get())
            if anum2 % int(anum2) == 0:
                if bnum2 % int(bnum2) == 0:
                    anum2 = int(anum2)
                    bnum2 = int(bnum2)
                    print('First if statement')
                    ans2 = (f'({anum2**2} × x^2) - ({bnum2**2} × y^2)')
                    ansl2 = Label(rt,text = f'Answer: {ans2}' ,font = ('calibri', 18))
                    ansl2.grid(row = 4, column = 1)
                
            elif bnum2 % int(bnum2) == 0:
                print('in elif')
                ans2 = (f'({anum2**2} × x^2) - ({bnum2**2} × y^2)')
                ansl2 = Label(rt,text = f'Answer: {ans2}' ,font = ('calibri', 18))
                ansl2.grid(row = 4, column = 1)
                
            
            else: 
                print('nothing happened')
                ans2 = (f'({anum2**2} × x^2) - ({bnum2**2} × y^2)')
                ansl2 = Label(rt,text = f'Answer: {ans2}' ,font = ('calibri', 18))
                ansl2.grid(row = 4, column = 1)

        except ValueError:
            print('Its an Error')
            errl2 = Label(rt, text = 'Only Enter a number', fg = 'white', font = ('arial', 16), bg = '#FEEAD8')
            errl2.grid(row = 3, column = 2)

    subB2 = Button(rt, text = 'Submit', fg = 'LightSkyBlue', bg = 'black',
                font = ('montserrat', 15), command = Answer2)
    subB2.grid(row = 2, column = 2) 
    empp = Label(rt, text = '                                                     ', bg ='#FEEAD8', font = ('quicksand', 80))
    empp.grid(row = 200, column = 100)

def Calleq():  

    eq1b = Button(rt, text = 'Equation 1', fg = 'white', bg = 'black',
    activebackground = 'black', activeforeground = 'white', command = Equation1)
    eq1b.grid(row = 200, column = 200)


    eq3b = Button(rt, text = 'Equation 2', fg = 'black', bg = 'white',
    activebackground = 'white', activeforeground = 'black', command = Equation2)
    eq3b.grid(row = 200, column = 201)

    eq2b = Button(rt, text = 'Equation 3', fg = 'black', bg = 'white',
    activebackground = 'white', activeforeground = 'black', command = Equation3)
    eq2b.grid(row = 201, column = 200)

    eq4b = Button(rt, text = 'Equation 4', fg = 'white', bg = 'black',
    activebackground = 'black', activeforeground = 'white', command = Equation4)
    eq4b.grid(row = 201, column = 201)

Calleq()

def des():
    rt.destroy()

b = Button(rt, text = 'Close', command = des)
b.grid(row = 10, column = 2)


rt.mainloop()
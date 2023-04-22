import tkinter
from tkinter import Label, Pack
rt = tkinter.Tk()
rt.title('mail id from text automated')
rt.geometry("400x400")
try:
    global file
    file = open(r'C:\\Users\\Vinod-2018\\Desktop\\TOTAL SAI THINGS\\sai stuff\\Sai Programming\Gmails.txt', 'r')
    gmail_c = 0
    
    for f in file:
        f = f.split()
        g = f[1]   
        read = g.partition('@')
        
        Label(rt, text = f"mail Id: {g}", 
        font = ('open sans', 12), fg = 'blue').pack()
        Label(rt, text = f'Name: {read[0]}',
        font = ('ubuntu mono', 12), fg = 'red').pack()
        print(f'Total email: {g}')
        print(f'Name: {read[0]}')
        print(f'Suffix: {read[2]}')
        
    file.close()

except FileNotFoundError:
    print('file doesnt exist')
    Label(rt, text = "The file doesn't exist, try again").pack()
    

rt.mainloop()


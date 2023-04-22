import os
from tkinter import Tk, Label, Button
os.chdir(os.path.dirname(__file__))
print(os.listdir())
print(os.getcwd())
if 'UI.py' not in os.listdir():
    rt = Tk()
    Label(rt, text = "'UI.py' NOT FOUND!, PLEASE ENSURE INSTALLATION WAS CORRECT", 
    fg = 'red', font = ("consolas", 12)).pack()
    Button(rt, text = "CLOSE", fg = "purple", font = ("consolas",11), command = lambda: rt.destroy()).pack()
    rt.mainloop()
else:
    print(True)
    exec(open("UI.py").read())
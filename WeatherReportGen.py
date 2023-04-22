import pprint
import requests
from tkinter import Entry, Label, Button, Tk

with open(r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Dependencies\WeatherRepDep.txt', 'r') as file:
    apikey = file.readlines()[0]

rt = Tk()
rt.title("Python Weather Report Gen V-0.8")
rt.geometry("800x500")

asklabel = Label(rt, text = 'Enter the name of the city.   *Full Name', fg = "#0008FF", 
font = ("montserrat", 16)).place(x = 20, y = 10)

def showRep(a) -> None:
    city = cityname.get().strip().lower().capitalize()
    Label(rt, text = "    \t\t\t\t\t\t\n"*10).place(x = 0, y = 100)
    if city == "" or city == " ": Label(rt, text = "Enter a city's full name to view its weather", font = ("calibri", 14)).place(x = 100, y = 100)
    else:
        try:
            apiUrl = f'https://api.openweathermap.org/data/2.5/weather?q={city.strip().lower()}&appid={apikey}&units=metric'
            dataRaw = requests.get(apiUrl).json()
            data = {}
            data["Clouds"] = f"{dataRaw['clouds']['all']}%"
            data["Coords"] = f"Lat: {dataRaw['coord']['lat']} deg | Long: {dataRaw['coord']['lon']} deg"
            data["Percipitation"] = f"{dataRaw['main']['feels_like']}%"
            data["Humidity"] = f"{dataRaw['main']['humidity']}%"
            data["Pressure"] = f"{dataRaw['main']['pressure']} hPa"
            data['Temp'] = f"{dataRaw['main']['temp']} C"
            data["Temp-Figures"] = f"Max Temp: {dataRaw['main']['temp_max']}C | Min Temp: {dataRaw['main']['temp_min']}C"
            data["Region"] = f"{dataRaw['sys']['country']}/{dataRaw['name']}"
            data["Vision"] = f"Visibility: {float((dataRaw['visibility']/1000))} KM | Weather Type: {dataRaw['weather'][0]['main']}"
            data["Description"] = f"{dataRaw['weather'][0]['description']}"
            data["wind"] = f"{dataRaw['wind']['deg']} deg | Speed: {dataRaw['wind']['speed']} m/s"
            data = pprint.pformat(data)
            Label(rt, text = "    \t\t\t\t\t\t\n"*10).place(x = 0, y = 100)
            readStr = str(data).replace("{", "").replace("}", "").replace("'", '')
            Label(rt, text = readStr, font = ('open sans', 16), fg = '#D71000').place(x = 40, y = 100)

        except KeyError:
            Label(rt, text = "Enter a valid city's full name to view its weather", font = ("calibri", 14)).place(x = 100, y = 100)

def showinfo() -> None:
    Label(rt, text = "    \t\t\t\t\t\t\n"*10).place(x = 0, y = 100)
    Label(rt, text = """
    Version: 1.0
    Made and Developed: Sai 
    API Provider: openweathermap.org
    Code Output: Weather Details about a place
    Code Input: Take in a place to show weather details 
    Programming Lang - Enviornment: Python 3.9.6 - VSC
    
    """, fg = '#00BA19', font = ('roboto mono', 12)).place(x = 0, y = 100)
cityname = Entry(rt, fg = "#FF008F", font = ("open sans", 17), width = 30)
cityname.place(x = 28, y = 50)
cityname.bind("<Return>", showRep)
subB = Button(rt, text = "Get Weather Report", fg = '#1F8900' ,
font = ("cambria", 14), command = lambda: showRep("")).place(x = 400, y = 47)
infoB = Button(rt, text = 'info', font = ("calibri", 10), command = showinfo).place(x = 600,y = 47)
rt.mainloop()
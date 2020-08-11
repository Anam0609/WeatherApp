import tkinter as tk
import requests
from PIL import Image, ImageTk

# setting the window size
theheight = 500
thewidth = 800


# "https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=7f65701f025236c354d7754c5a4e0b71";
def get_weather(city):
    weatherkey = '7f65701f025236c354d7754c5a4e0b71'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    # api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={7f65701f025236c354d7754c5a4e0b71}
    params1 = {'appid': weatherkey, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params1)
    weather = response.json()
    print(weather)
    mylabel['text'] = displayingoutput(weather)

    icon_name = weather["weather"][0]["icon"]
    weather_image(icon_name)


def weather_image(icon):
    size = int(second_frame.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open("./img/" + icon + ".png").resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor="nw", image=img)
    weather_icon.image = img


def displayingoutput(weather):
    try:

        name = weather['name']
        count = weather['sys']['country']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humid = weather['main']['humidity']

        result = 'Name of Town: %s \nCountry: %s \nWeather Description: %s \nHumidity: %s \nTemperature (oC)): %s' % (
            name, count, desc, humid, temp)
    except:
        error = "Retrieving data failed"
    return result


def clearing():
    mylabel.config(text="")
    entry.getvar("")


window = tk.Tk()
window.title("Weather app")

canvas = tk.Canvas(window, height=theheight, width=thewidth)
# ===================================================================================
background_image = ImageTk.PhotoImage(file='weather.jpg')
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)
# ======================================================================================
canvas.pack()

# background_label.pack(relwidth=1, relheight=1)
frame = tk.Frame(window, bg='#3366ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
# textbox to enter the input city
entry = tk.Entry(frame, font=30)
entry.place(relwidth=0.65, relheight=1)
# button to invoke the weather API
myButton = tk.Button(frame, text="Get Weather", font=('arial', 20), bg="#3366ff", fg='#fff',
                     command=lambda: get_weather(entry.get()))
myButton.pack(side="right")

second_frame = tk.Frame(window, bg='#3366ff', bd=10)
second_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n', )
mylabel = tk.Label(second_frame, font=40, bd=10, anchor='nw', justify='left')
mylabel.place(relwidth=1, relheight=1)
myclearButton = tk.Button(window, text="Clear", font=('arial', 20), bg="#3366ff", fg='#fff', command=clearing)
myclearButton.pack(side='bottom')

weather_icon = tk.Canvas(mylabel, bg="white", bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

window.mainloop()

import requests
from translatepy.translators.google import GoogleTranslate
import tkinter

root = tkinter.Tk()

gtranslate = GoogleTranslate()
API_KEY = "90e361b1c10316e8244799ae41daee32"


def get_weather(city):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    r = requests.get(url)
    
    data = r.json()

    temp = data["main"]["temp"]
    tempVar.set(f"Температура: {temp}")
    
    weather = data["weather"][0]["main"]
    translate_weather = gtranslate.translate(weather, "ru")
    weatherVar.set(f"Погода: {translate_weather}")
    
    return temp, weather, tempVar, weatherVar
    
def main():
    city = city_entry.get()
    print(city)
    get_weather(city)

tempVar = tkinter.StringVar()
weatherVar = tkinter.StringVar()



label = tkinter.Label(root, text="Приветствуем в приложении Погода", bg="DodgerBlue", fg="white")
label.pack()

city_entry = tkinter.Entry(root)
city_entry.pack()

button = tkinter.Button(root, text="Найти", command=main, cursor="heart", padx=30, pady=15)
button.pack()

temp_label = tkinter.Label(root, textvariable=tempVar)
temp_label.pack()

weather_label = tkinter.Label(root, textvariable=weatherVar)
weather_label.pack()

root.mainloop()

import requests
from translatepy.translators.google import GoogleTranslate

gtranslate = GoogleTranslate()
API_KEY = "90e361b1c10316e8244799ae41daee32"

# r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Воронеж&appid={API_KEY}")
# print(r.text)

def get_weather(city):
    # print(f"Вы выбрали: {city}")
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    # print(url)
    
    r = requests.get(url)
    # print(r)
    
    data = r.json()
    # print(data)
    
    # print(type(data))
    
    temp = data["main"]["temp"]
    print(f"Температура {temp}℃")
    
    weather = data["weather"][0]["main"]
    translate_weather = gtranslate.translate(weather, "Japanese")
    print(f"Погода: {translate_weather}")
    
    return temp, weather
    
def main():
    print("Приветствуем в приложении Погода")
    city = input("Введите название города: ")
    get_weather(city)

main()


# Погода

import requests
from translatepy.translators.google import GoogleTranslate

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.gtranslate = GoogleTranslate()

    def get_weather(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["main"]
            print(f"Температура: {temp}℃")

            # Перевод описания погоды на японский
            translated_weather = self.gtranslate.translate(weather, "Japanese")
            print(f"Погода: {translated_weather}")
            
            return temp, weather
        else:
            print(f"Ошибка: {data.get('message', 'Не удалось получить данные о погоде')}")
            return None, None

    def run(self):
        print("Приветствуем в приложении Погода")
        city = input("Введите название города: ")
        self.get_weather(city)

if __name__ == "__main__":
    API_KEY = "90e361b1c10316e8244799ae41daee32"
    app = WeatherApp(API_KEY)
    app.run()

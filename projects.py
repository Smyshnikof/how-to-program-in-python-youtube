# Ресторан

import random

print("Добро пожаловать в ресторан У Егора")
print("Вот наше меню: ")
print("1. Картошку фри")
print("2. Кола")
print("3. Пицца")
print("4. Салат")

order = []

while True:
    action = input("Введите номер блюда, (0) - для завершения заказа: ")
    if action == "1":
        print("Картошка фри")
        order.append("Картошка фри")
        
    elif action == "2":
        print("Кола")
        order.append("Кола")
        
    elif action == "3":
        print("Пицца")
        order.append("Пицца")
        
    elif action == "4":
        print("Салат")
        order.append("Салат")
    
    elif action == "0":
        break
    
    else:
        print("Такого блюда нет.")
        
print(f"Ваш заказ: {order}")


# Телефонная книга

# from colorama import init
from colorama import Fore, Back, Style
init()

print(Style.BRIGHT + "Добро пожаловать в приложение Телефонная книга")
print("----------------------")
print(Style.RESET_ALL + "1. Показать контакты")
print(Fore.GREEN + "2. Добавить контакт")
print("3. Редактировать контакт")
print("4. Удалить контакт")
print(Fore.RED + "5. Очистить контакты")
print(Fore.RESET + "6. Показать только имена контактов")
print("7. Показать только номера контактов")
print("8. Выход")
print("----------------------")

phones = {
    "Егор": 89001110022,
    "Админ": 7899911123,
    
}

def show_contact():
    for name, phone in phones.items():
        print(f"{name} - {phone}") 

def add_contact():
    name = input("Имя контакта: ")
    phone = input("Телефон: ")
    phones[name] = phone
    print("Контакт добавлен")

def edit_contact():
    name = input("Имя контакта: ")
    if name in phones:
        new_phone = input("Новый телефон: ")
        phones[name] = new_phone
        print("Контакт обновлен")
    else:
        print("Такого контакта нет")
        
def delete_contact():
    name = input("Имя контакта: ")
    if name in phones:
        del phones[name]
        print("Контакт удален")
    else:
        print("Такого контакта нет")
        
def delete_all_contact():
    phones.clear()
    print("Все контакты удалены")

def show_only_name_contact():
    for name in phones:
        print(name)

def show_only_phone_contact():
    for phone in phones.values():
        print(phone)

while True:
    action = input("Выберите действие: ")
    
    if action == "1":
        show_contact()
        
    elif action == "2":
        add_contact()
        
    elif action == "3":
        edit_contact()
        
    elif action == "4":
        delete_contact()
        
    elif action == "5":
        delete_all_contact()
        
    elif action == "6":
        show_only_name_contact()
        
    elif action == "7":
        show_only_phone_contact()
        
    elif action == "8":
        break
    
    else:
        print("Такой команды нет.") 
        


# Погода

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


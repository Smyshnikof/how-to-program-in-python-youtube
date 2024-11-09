# print("Hello, world!")
# name = input(">")
# a = 1
# b = 2
# first_name = ""
# print(name)

# name = "EGOR"
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name)

# a = 10
# b = 15
# c = 50
# d = 5.5
# print(a, b, c)


# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a // b)
# print(a ** b)

# name = "Egor"
# text_int = "10"
# a = 10
# b = 10.90

# print(type(name))
# print(type(a))
# print(type(b))

# print(int(b))
# print(type(str(a)))
# print(float(text_int))


# a = 50
# b = 60
# c = a < b
# print(type(c))
# print(a > b)
# print(a < b)

# print(a <= b)
# print(a >= b)

# print(a == b)
# print(a != b)

# a = 100
# b = 50
# if a < b:
#     print("A < B")
# else:
#     print("A > B")


# username = "Smyshnikov"
# password = "12345"

# if username == "Smyshnikov" and password == "12345":
#     print("Добро пожаловать!")
# else:
#     print("До свидания!")

# username = input("Введите никнейм: ")
# password = input("Введите пароль: ")

# if username == "Smyshnikov" and password == "12345":
#     print("Добро пожаловать!")
# elif username == "Moderator" and password == "1010":
#     print("Добро пожаловать, модератор!")
# elif username == "Moderator" and password == "1010":
#     print("Добро пожаловать, модератор!")
# elif username == "Moderator" and password == "1010":
#     print("Добро пожаловать, модератор!")
# else:
#     print("До свидания!")
    

# -------- ДЗ на условия
# Задачка 1:

# Напиши программу на Python, которая запрашивает у пользователя текущую температуру в градусах Цельсия и выводит сообщение о погоде в зависимости от температуры:

# Если температура меньше -10 градусов, программа должна вывести сообщение "Очень холодно, лучше оставайтесь дома!".

# Если температура от -10 до 0 градусов включительно, программа должна вывести сообщение "Холодно, наденьте теплую одежду!".

# Если температура от 0 до 10 градусов включительно, программа должна вывести сообщение "Прохладно, можете одеть легкую куртку.".

# Если температура больше 10 градусов, программа должна вывести сообщение "Тепло, на улицу можно без куртки!".

# temp = float(input("Введите температуру: "))
# print(type(temp))


# day = 1
# while day <= 31:
#     print(day)
#     day = day + 1


# print("Добро пожаловать в ресторан У Егора")
# print("Вот наше меню: ")
# print("1. Картошку фри")
# print("2. Кола")
# print("3. Пицца")
# print("4. Салат")

# while True:
#     action = input("Введите номер блюда: ")
#     if action == "1":
#         print("Картошка фри")
#     elif action == "2":
#         print("Кола")
#     elif action == "3":
#         print("Пицца")
#     elif action == "4":
#         print("Салат")
#     else:
#         print("Такого блюда нет.")


import random

# print("Добро пожаловать в ресторан У Егора")
# print("Вот наше меню: ")
# print("1. Картошку фри")
# print("2. Кола")
# print("3. Пицца")
# print("4. Салат")

# order = []

# while True:
#     action = input("Введите номер блюда, (0) - для завершения заказа: ")
#     if action == "1":
#         print("Картошка фри")
#         order.append("Картошка фри")
        
#     elif action == "2":
#         print("Кола")
#         order.append("Кола")
        
#     elif action == "3":
#         print("Пицца")
#         order.append("Пицца")
        
#     elif action == "4":
#         print("Салат")
#         order.append("Салат")
    
#     elif action == "0":
#         break
    
#     else:
#         print("Такого блюда нет.")
        
# print(f"Ваш заказ: {order}")

# order_number = random.randint(100, 300)
# print(order_number)
# rand_rock = random.choice(["Камень", "Ножницы", "Бумага"])
# print(rand_rock)

# -------------ДЗ циклы

# Задание повышенной сложности, но очень интересное.

# Задача: Напишите программу, которая будет симулировать банкомат. Пользователь может вводить команды для выполнения операций с банковским счетом. Программа должна предоставлять следующие опции:

# 1. Проверить баланс.
# 2. Внести деньги на счет.
# 3. Снять деньги со счета.
# 4. Выйти из программы.

# Программа должна запрашивать команду пользователя и выполнять соответствующую операцию. После каждой операции программа должна снова предлагать пользователю выбрать операцию или выйти из программы.

# Пример:
# balance = 0 # Изначальный баланс счета

# while True:
# 1. Проверить баланс.
# 2. Внести деньги на счет.
# 3. Снять деньги со счета.
# 4. Выйти из программы.

# "Введите номер операции: "

# if 1.
# print(f"Ваш баланс: {balance} рублей.")

# if 2.
# deposit = float(input("Введите сумму для внесения: "))
# balance = balance + deposit
# print(f"Сумма {deposit} рублей успешно внесена на счет.")

# if 3.
# "Введите сумму для снятия: "
# print("Недостаточно средств на счете.")
# print(f"Сумма {withdrawal} рублей успешно снята со счета.")

# if 4.
# print("Спасибо за использование банкомата. До свидания!")


# order = []
# print(type(order))

# fruits = ["Яблоко", "Банан"]
# # print(fruits[0])

# fruits.append("Груша")
# print(fruits)

# fruits.pop()
# print(fruits)

# fruits.insert(0, "Груша")
# print(fruits)

# # fruits.remove("Яблоко")
# # print(fruits)

# # fruits.pop(0)
# # print(fruits)

# fruits.sort()
# print(fruits)

# fruits.reverse()
# print(fruits)


# a = [70, 12, 10, 50, 50.5, 100,6]
# a.sort()
# print(a)

# b = ["Текст", 12, 50.1]

# ---------- ДЗ на массив
# Задание: Создание списка и применение методов

# 1. Создайте пустой список с именем my_list.

# 2. Добавьте в список пять целых чисел по вашему выбору.

# 3. Выведите содержимое списка на экран с помощью команды print().

# 4. Используя метод append(), добавьте в список ещё одно целое число.

# 5. Выведите обновленное содержимое списка на экран.

# 6. Используя метод insert(), вставьте целое число в середину списка.

# Как работает insert?
# my_list.insert(2, "яблоко")
# добавляется яблоко на позицию 2 в массиве

# 7. Снова выведите обновленное содержимое списка на экран.

# 8. Используя метод remove(), удалите один из элементов списка.

# 9. Выведите содержимое списка после удаления элемента.

# 10. Используя метод sort(), отсортируйте элементы списка в порядке возрастания.

# 11. Выведите отсортированный список на экран.

# 12. Используя метод reverse(), переверните порядок элементов списка.

# 13. Выведите список в обратном порядке.


# fruits = ("Яблоко", "Банан")
# print(type())


# player = {
#     "name": "Smyshnikov",
#     "level": 50,
#     "skills": ["Python", "JS", "HTML + CSS"],
# }

# print(player["name"])
# print(player["level"])
# print(player["skills"][0])


# order = ["Кола", "Пицца", "Салат"]
# # print(order)

# for item in order:
#     print(item)

# fruits = ["Яблоко", "Банан", "Груша"]
# for fruit in fruits:
#     print(fruit)

# print(order[0])
# print(order[1])
# print(order[2])

# player = {
#     "name": "Smyshnikov",
#     "level": 50,
#     "skills": ["Python", "JS", "HTML + CSS"],
# }
# print(player)

# for key in player:
#     print(key)

# for value in player.values():
#     print(value)
    
# for key, value in player.items():
#     print(f"{key} - {value}")


# from colorama import init
# from colorama import Fore, Back, Style
# init()

# print(Style.BRIGHT + "Добро пожаловать в приложение Телефонная книга")
# print("----------------------")
# print(Style.RESET_ALL + "1. Показать контакты")
# print(Fore.GREEN + "2. Добавить контакт")
# print("3. Редактировать контакт")
# print("4. Удалить контакт")
# print(Fore.RED + "5. Очистить контакты")
# print(Fore.RESET + "6. Показать только имена контактов")
# print("7. Показать только номера контактов")
# print("8. Выход")
# print("----------------------")

# phones = {
#     "Егор": 89001110022,
#     "Админ": 7899911123,
    
# }

# def show_contact():
#     for name, phone in phones.items():
#         print(f"{name} - {phone}") 

# def add_contact():
#     name = input("Имя контакта: ")
#     phone = input("Телефон: ")
#     phones[name] = phone
#     print("Контакт добавлен")

# def edit_contact():
#     name = input("Имя контакта: ")
#     if name in phones:
#         new_phone = input("Новый телефон: ")
#         phones[name] = new_phone
#         print("Контакт обновлен")
#     else:
#         print("Такого контакта нет")
        
# def delete_contact():
#     name = input("Имя контакта: ")
#     if name in phones:
#         del phones[name]
#         print("Контакт удален")
#     else:
#         print("Такого контакта нет")
        
# def delete_all_contact():
#     phones.clear()
#     print("Все контакты удалены")

# def show_only_name_contact():
#     for name in phones:
#         print(name)

# def show_only_phone_contact():
#     for phone in phones.values():
#         print(phone)

# while True:
#     action = input("Выберите действие: ")
    
#     if action == "1":
#         show_contact()
        
#     elif action == "2":
#         add_contact()
        
#     elif action == "3":
#         edit_contact()
        
#     elif action == "4":
#         delete_contact()
        
#     elif action == "5":
#         delete_all_contact()
        
#     elif action == "6":
#         show_only_name_contact()
        
#     elif action == "7":
#         show_only_phone_contact()
        
#     elif action == "8":
#         break
    
#     else:
#         print("Такой команды нет.") 
        
        


# a = 10
# b = 20
# c = a + b
# print(c)

# def plus():
#     a = 10
#     b = 20
#     c = a + b
#     print(c)

# plus()

# def plus(a, b):
#     c = a + b
#     print(c)

# plus(10, 50)

# def plus(a, b):
#     c = a + b
#     return c

# a = (plus(10, 50))
# print(a)


# fruits = ["Яблоко", 2]
# a = fruits.append("Груша")
# print(a)

# print(print("Result"))

# def plus(a:int, b:int):
#     c = a + b
#     return c

# print(plus(10, 50))
# print(plus())


# a = 50
# object

# def minus(a, b):
    

# def calc():
#     action = input()
#     a = input()
#     b 
#         minux(a , b)


import requests

r = requests.get("https://ya.ru/")
print(r.text)



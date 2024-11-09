# Ресторан

class Menu:
    def __init__(self):
        self.items = {
            "1": "Картошка фри",
            "2": "Кола",
            "3": "Пицца",
            "4": "Салат"
        }

    def show_menu(self):
        print("Добро пожаловать в ресторан У Егора")
        print("Вот наше меню: ")
        for number, dish in self.items.items():
            print(f"{number}. {dish}")

    def get_item(self, item_number):
        return self.items.get(item_number, None)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_order(self):
        print(f"Ваш заказ: {self.items}")


class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def take_order(self):
        while True:
            action = input("Введите номер блюда, (0) - для завершения заказа: ")
            if action == "0":
                break

            item = self.menu.get_item(action)
            if item:
                print(f"{item}")
                self.order.add_item(item)
            else:
                print("Такого блюда нет.")

        self.order.show_order()


if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.menu.show_menu()
    restaurant.take_order()


# Телефонная книга
from colorama import init, Fore, Style
init()

class PhoneBook:
    def __init__(self):
        self.phones = {
            "Егор": 89001110022,
            "Админ": 7899911123,
        }

    def show_contacts(self):
        print(Style.BRIGHT + "Список контактов:")
        for name, phone in self.phones.items():
            print(f"{name} - {phone}")
        print(Style.RESET_ALL)

    def add_contact(self):
        name = input("Имя контакта: ")
        phone = input("Телефон: ")
        self.phones[name] = phone
        print(Fore.GREEN + "Контакт добавлен" + Fore.RESET)

    def edit_contact(self):
        name = input("Имя контакта: ")
        if name in self.phones:
            new_phone = input("Новый телефон: ")
            self.phones[name] = new_phone
            print(Fore.GREEN + "Контакт обновлен" + Fore.RESET)
        else:
            print(Fore.RED + "Такого контакта нет" + Fore.RESET)

    def delete_contact(self):
        name = input("Имя контакта: ")
        if name in self.phones:
            del self.phones[name]
            print(Fore.GREEN + "Контакт удален" + Fore.RESET)
        else:
            print(Fore.RED + "Такого контакта нет" + Fore.RESET)

    def delete_all_contacts(self):
        self.phones.clear()
        print(Fore.RED + "Все контакты удалены" + Fore.RESET)

    def show_only_names(self):
        print(Style.BRIGHT + "Имена контактов:")
        for name in self.phones:
            print(name)
        print(Style.RESET_ALL)

    def show_only_phones(self):
        print(Style.BRIGHT + "Номера контактов:")
        for phone in self.phones.values():
            print(phone)
        print(Style.RESET_ALL)

class PhoneBookApp:
    def __init__(self):
        self.phonebook = PhoneBook()

    def show_menu(self):
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

    def run(self):
        while True:
            self.show_menu()
            action = input("Выберите действие: ")
            
            if action == "1":
                self.phonebook.show_contacts()
            elif action == "2":
                self.phonebook.add_contact()
            elif action == "3":
                self.phonebook.edit_contact()
            elif action == "4":
                self.phonebook.delete_contact()
            elif action == "5":
                self.phonebook.delete_all_contacts()
            elif action == "6":
                self.phonebook.show_only_names()
            elif action == "7":
                self.phonebook.show_only_phones()
            elif action == "8":
                break
            else:
                print(Fore.RED + "Такой команды нет." + Fore.RESET)

if __name__ == "__main__":
    app = PhoneBookApp()
    app.run()

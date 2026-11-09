# ===== T-1. Главное меню (общая задача) =====
TITLE = "Каталог Библиотеки колледжа" # впишите название своего продукта
MENU = [] # пункты меню: (название, функция)
def ask_int(text):
# спрашивает целое число, пока его не введут правильно
while True:
value = input(text).strip()
if value.lstrip("-").isdigit():
return int(value)
print("Ошибка: введите целое число")
def ask_float(text):
# спрашивает число (можно дробное), пока его не введут правильно
while True:
value = input(text).strip().replace(",", ".")
try:
return float(value)
except ValueError:
print("Ошибка: введите число")
def start():
while True:
print()
print("=====", TITLE, "=====")
for number, item in enumerate(MENU, start=1):
print(number, "-", item[0])
print("0 - Выход")
choice = input("Выберите пункт: ").strip()
if choice == "0":
print("До свидания!")
break
elif choice.isdigit() and 1 <= int(choice) <= len(MENU):
MENU[int(choice) - 1][1]()
else:
print("Нет такого пункта меню")
# ===== US-2. Добавить книгу =====
books = [] # список книг
def add_book():
title = input("Название: ").strip()
author = input("Автор (фамилия и инициалы): ").strip()
year = ask_int("Год издания: ")
books.append({"название": title, "автор": author, "год": year,
"выдана": False})
print("Книга добавлена в каталог")
MENU.append(("Добавить книгу", add_book))
# ===== ЗАПУСК: эта строка всегда должна быть последней =====
start()

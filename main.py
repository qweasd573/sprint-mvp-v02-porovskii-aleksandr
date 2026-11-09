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
# ===== US-3. Список всех книг =====
def show_books():
if len(books) == 0:
print("Каталог пуст")
return
for number, b in enumerate(books, start=1):
status = "выдана" if b["выдана"] else "в наличии"
print(f"{number}. {b['автор']} «{b['название']}», {b['год']}"
f" — {status}")
MENU.append(("Список всех книг", show_books))
# ===== US-4. Поиск по автору =====
def find_by_author():
text = input("Фамилия автора: ").strip().lower()
found = false
for b in books:
if text in b["автор"].lower():
print(f"{b['автор']} «{b['название']}», {b['год']}")
found = true
if not found:
print("Книги этого автора не найдены")
MENU.append(("Найти книги по автору", find_by_author))
# ===== US-5. Выдать / вернуть книгу =====
def issue_book():
show_books()
number = ask_int("Номер книги: ")
if 1 <= number <= len(books):
book = books[number - 1]
book["выдана"] = not book["выдана"]
if book["выдана"]:
print("Книга выдана читателю")
else:
print("Книга возвращена в библиотеку")
else:
print("Нет книги с таким номером")
MENU.append(("Выдать / вернуть книгу", issue_book))
# ===== ЗАПУСК: эта строка всегда должна быть последней =====
start()

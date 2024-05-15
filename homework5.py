"""
homework5.py
"""

# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
SITE = "www.my_site.com#about"
print(SITE.replace("#", "/"))

# Напишите программу, которая добавляет ‘ing’ к словам
WORD_LIST = ["run", "go", "lie"]
for word in WORD_LIST:
    "{word}ing"
WORD_LIST_ING = " ".join(f"{word}ing" for word in WORD_LIST)
print(WORD_LIST_ING)

# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
LOGIN = "Ivanou Ivan"
SPACEINDEX = LOGIN.find(" ")
SURNAME = LOGIN[:SPACEINDEX + 1]
FIRST_NAME = LOGIN[SPACEINDEX + 1:]
print(FIRST_NAME + " " + SURNAME)

# Напишите программу которая удаляет пробел в начале, в конце строки
HELLO = " Hello World! "
HELLO_1 = HELLO.strip()
print(HELLO_1)

# Исправьте "pARiS" >> "Paris"
CITY = "pARiS"
print(CITY.capitalize())

""" Заменить символ “#” на символ “/” в строке 'www.my_site.com#about' """
SITE = "www.my_site.com#about"
print(SITE.replace("#", "/"))

# Напишите программу, которая добавляет ‘ing’ к словам
WORDS = ["run", "go", "lie"]
for word in WORDS:
    "{word}ing"
word_ing = " ".join(f"{word}ing" for word in WORDS)
print(word_ing)

# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
LOGIN = "Ivanou Ivan"
spaceIndex = LOGIN.find(" ")
surname = LOGIN[:spaceIndex + 1]
first_name = LOGIN[spaceIndex + 1:]
print(first_name + " " + surname)

# Напишите программу которая удаляет пробел в начале, в конце строки
HELLO = " Hello World! "
s = HELLO.strip()
print(s)

# Исправьте "pARiS" >> "Paris"
CITY = "pARiS"
print(CITY.capitalize())

# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
site = "www.my_site.com#about"
print(site.replace("#", "/"))

# Напишите программу, которая добавляет ‘ing’ к словам
words = ["run", "go", "lie"]
for word in words:
    "{word}ing"
word_ing = " ".join(f"{word}ing" for word in words)
print(word_ing)

# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
login: str = "Ivanou Ivan"
spaceIndex = login.find(" ")
surname = login[:spaceIndex + 1]
first_name = login[spaceIndex + 1:]
print(first_name + " " + surname)

# Напишите программу которая удаляет пробел в начале, в конце строки
txt = " Hello World! "
s = txt.strip()
print(s)

# Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"
txt = "pARiS"
print(txt.capitalize())

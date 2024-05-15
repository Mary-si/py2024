# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
# Напишите программу, которая добавляет ‘ing’ к словам
# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
# Напишите программу которая удаляет пробел в начале, в конце строки
# Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"


string = "www.my_site.com#about"
print(string.replace("#", "/"))

a = ["run", "go", "lie"]
for word in a:
    "{word}ing"
b = " ".join(f"{word}ing" for word in a)
print(b)

string = "Ivanou Ivan"
spaceIndex = string.find(" ")
word1 = string[:spaceIndex + 1]
word2 = string[spaceIndex + 1:]
print(word2 + " " + word1)

string = " Hello World! "
s = string.strip()
print(s)

txt = "pARiS"
print(txt.capitalize())

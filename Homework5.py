# """Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'"""

txt: str = "www.my_site.com#about"
print(txt.replace("#", "/"))

# """Напишите программу, которая добавляет ‘ing’ к словам"""

a = ["run", "go", "lie"]
for word in a:
    "{word}ing"
b = " ".join(f"{word}ing" for word in a)
print(b)

# """В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"""

b = "Ivanou Ivan"
spaceIndex = b.find(" ")
word1 = b[:spaceIndex + 1]
word2 = b[spaceIndex + 1:]
print(word2 + " " + word1)

# """Напишите программу которая удаляет пробел в начале, в конце строки"""

s = " Hello World! "
s = s.strip()
print(s)

# """Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris" """

a = "pARiS"
print(a.capitalize())

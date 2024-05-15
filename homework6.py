"""Homework6.py"""

# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
string = "Robin Singh"
a = string.split(" ")
print(a)

# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
string = "I love arrays they are my favorite"
a = string.split(" ")
print(a)

# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
name = ["Ivan", "Ivanou"]
city = "Minsk"
country = "Belarus"
print("Привет," + " " + " ".join(name) + "!" + " " "Добро пожаловать в" + " " + city + " " + country + ".")

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку
# => "I love arrays they are my favorite"
txt = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(txt))

# Создайте список из 10 элементов,
# вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
NameList = ["Mary", "Alex", "Jon", "Michail", "Maikl", "Ann", "Valeri", "Natali", "Svetlana", "Andrei"]
NameList.insert(2, "Gleb")
NameList.remove("Valeri")
print(NameList)

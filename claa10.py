# Напишите функцию декоратор, которая добавляет 1 к заданному числу
def add_number(func):
    def add_number2(a):
        a += 1
        func(a)
    return add_number2

@add_number
def number(a):
    print(a)

number(2)

# Напишите функцию декоратор, которая переводит полученный текст в верхний регистр
def text(func:str) -> str
    def text1(a):
        a = a.upper()
        func
    return text1

@text
def text(a):
    print(a)

text1("ura")

# Напишите функции декораторы, которые форматируют текст(добавляют html теги) в различные стили:


# Жирный <b> </b>
# Курсив <i> </i>
# Подчеркивание <u> </u>


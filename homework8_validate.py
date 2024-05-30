"""homework8"""

# Validate
# Ваша задача написать программу, принимающее число - номер кредитной карты
# (число может быть четным или не четным).
# И проверяющей может ли такая карта существовать.
# Предусмотреть защиту от ввода букв, пустой строки и т.д.
# Примечания Алгоритм Луна

# Примеры
# validate(4561261212345464) #=> False
# validate(4561261212345467) #=> True


def validate_number(card):
    # сумма чисел
    sum_numbers = 0
    # переводим номер карты из строки в массив
    card_numbers = list(map(int, card))
    # проходимся по каждому числу
    for index, num in enumerate(card_numbers):
        # если index четный, то число стоит на нечетной позиции,
        # тк считается с нуля,
        # цифры стоящие на нечетных местах умножаем на 2
        if index % 2 == 0:
            double_numb = num * 2
            # если есть удвоенное число и оно больше 9,
            # то вычитаем из него 9 и прибавляем к сумме чисел
            if double_numb > 9:
                double_numb -= 9
            # если меньше 9, то прибавляем к сумме чесел
            sum_numbers += double_numb
        # если число стоит на чётной позиции, то прибавляем его к сумме чисел
        else:
            sum_numbers += num
    # если сумма чисел делится на 10 без остатка, то номер карты правильный
    return sum_numbers % 10 == 0


print(validate_number("4561261212345464"))

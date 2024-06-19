"""homework 14"""

# Напишите программу - инженерный калькулятор.
# Передусмотрите возможные ошибки и обработайте их. ~ - это предложение ввода.
#
# Базовые требования:
# Программа считает простые математические выражения:
# ~ 5 + 4 9
#
# Программа ожидает от пользователя ввода математического выражения и правильно его трактует:
# ~ 10 - 3 + 1 8 ~ 2 ** 3 - 1 7

import re


def calculator(expression):
    try:
        result = eval(expression)
    except Exception as e:
        return f"Ошибка при вычислении: {e}"
    return result


expression_1 = "5 + 49"
expression_2 = "10 - 3 + 18"
expression_3 = "2 ** 3 - 17"

# проверка
result_1 = calculator(expression_1)
result_2 = calculator(expression_2)
result_3 = calculator(expression_3)

print(f"Результат ({expression_1}) = {result_1}")
print(f"Результат ({expression_2}) = {result_2}")
print(f"Результат ({expression_3}) = {result_3}")

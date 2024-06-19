"""homework 14"""

# Напишите программу - инженерный калькулятор.
# Передусмотрите возможные ошибки и обработайте их. ~ - это предложение ввода.
#
# Базовые требования:
# Программа считает простые математические выражения:
# ~ 5 + 4 9
#
# Программа ожидает от пользователя ввода математического выражения
# и правильно его трактует:
# ~ 10 - 3 + 1 8 ~ 2 ** 3 - 1 7


import ast


def calculator(expression):
    """калькулятор"""
    try:
        a = ast.parse(expression, mode="eval")
        result = eval(compile(a, filename="", mode="eval"))
    except Exception as b:
        return f"Ошибка при вычислении: {b}"
    return result


EXPRESSION_1 = "5 + 49"
EXPRESSION_2 = "10 - 3 + 18"
EXPRESSION_3 = "2 ** 3 - 17"

# проверка
result_1 = calculator(EXPRESSION_1)
result_2 = calculator(EXPRESSION_2)
result_3 = calculator(EXPRESSION_3)

print(f"Результат ({EXPRESSION_1}) = {result_1}")
print(f"Результат ({EXPRESSION_2}) = {result_2}")
print(f"Результат ({EXPRESSION_3}) = {result_3}")

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


# def calculator(expression):
#     """калькулятор"""
#     try:
#         result = eval(expression)
#     except Exception as e:
#         return f"Ошибка при вычислении: {e}"
#     return result

from simpleeval import SimpleEval

def calculator(expression):
    """калькулятор с помощью simpleeval"""
    simple_evaluator = SimpleEval()
    try:
        result = simple_evaluator.eval(expression)
    except Exception as e:
        return f"Ошибка при вычислении: {e}"
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

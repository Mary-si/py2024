"""homework10"""

# Положительные аргументы функции

# Напишите декоратор @validate_arguments, который проверяет,
# что все аргументы функции являются положительными числами.
# Если встречается аргумент, не соответствующий этому условию,
# функция должна вывести сообщение об ошибке.
#
# Вот некоторые подсказки:
# Внутри декоратора, используйте цикл for для перебора аргументов функции.
# Используйте оператор if для проверки,
# является ли аргумент положительным числом.
# Если аргумент не соответствует условию,
# используйте оператор raise для вызова исключения ValueError.


def validate_arguments(func):
    """проверяет что все аргументы функции являются положительными числами"""
    def wrapper(*args):
        for i in args:
            if i < 0:
                raise ValueError("Введите положительное число")
        return func(*args)
    return wrapper


@validate_arguments
def positive_func_args(*args):
    """вывод"""
    print(*args)


# Проверка функции с положительными числами
positive_func_args(1, 2, 3)

# Проверка функции с числом =< 0
positive_func_args(-1, 2, 3)

"""homework10"""

# Функция кэширования *
# Напишите декоратор @cache, который кэширует результаты вызова функции
# и возвращает закэшированное значение
# при повторных вызовах с теми же аргументами.
# Это поможет избежать повторных вычислений для одинаковых входных данных
# и ускорит работу программы.
#
# Подсказки:
# Используйте словарь для хранения закэшированных значений.
# Ключом словаря будет набор аргументов функции,
# а значением - результат вызова функции с этими аргументами.
#
# Внутри декоратора, передайте аргументы функции
# в качестве ключа для доступа к закэшированным значениям.
#
# Если ключ уже есть в словаре, верните соответствующее значение.
# Если ключа нет, вызовите функцию,
# сохраните результат в словаре и верните его.

# Пример использования:
# @cache
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(5))  # Вывод: 5
# print(fibonacci(10))  # Вывод: 55
# print(fibonacci(5))  # Вывод: 5 (значение взято из кэша)


def cache(func):
    """кэширует результаты вызова функции,
    возвращает закэшированное значение """
    cache_number = {}

    def wrapper(*args):
        if args in cache_number:
            return cache_number[args]
        result = func(*args)
        cache_number[args] = result
        return result
    return wrapper


@cache
def fibonacci(n):
    """выполнение """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Проверка
print(fibonacci(5))  # Вывод: 5
print(fibonacci(10))  # Вывод: 55
print(fibonacci(5))  # Вывод: 5 (значение взято из кэша)

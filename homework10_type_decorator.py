"""homework10"""


# Напишите декоратор, который проверял бы тип параметров функции,
# конвертировал их если надо и складывал:
# @typed(type=str)
# def add(a, b):
#     return a + b
#
# Проверка
# add("3", 5) -> "8"
# add(5, 5) -> "55"
# add('a', 'b') -> 'ab’
#
# @typed(type=int)
# def add(a, b, с):
#     return a + b + с
#
# add(5, 6, 7) -> 18
#
# @typed(type=float)
# def add(a, b, с):
#     return a + b + с
#
# add(0.1, 0.2, 0.4) -> 0.7000000000000001

def typed(expected_type):
    """проверяет типы параметров функции"""
    def decorator(func):
        def wrapper(*args):
            if all(isinstance(arg, expected_type) for arg in args):
                return func(*args)
            else:
                print(f"Не верный тип аргумета, он должен быть "
                      f"типа {expected_type}")
        return wrapper
    return decorator


@typed(int)
def add(*args):
    """суммируем"""
    print(sum(args))


# Проверка
add("3", 5)
add(5, 5)
add('a', 'b')
add(5, 6, 7)


def typed2(expected_type):
    """проверяет тип параметров функции"""
    def decorator(func):
        def numbers(a, b, c):
            if (isinstance(a, expected_type) and isinstance(b, expected_type)
                    and isinstance(c, expected_type)):
                func(a, b, c)
            else:
                print(f"Не верный тип аргумета, он должен быть"
                      f"типа {expected_type}")
        return numbers
    return decorator


@typed2(float)
def add2(a, b, c):
    """суммируем"""
    print(a + b + c)


# Проверка
add2(0.1, 0.2, 0.4)

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
    def decorator(func):
        def numbers(a, b):
            if isinstance(a, expected_type) and isinstance(b, expected_type):
                func(a, b)
            else:
                print(f"Не верный тип аргумета, он должен быть типа {expected_type}")
        return numbers
    return decorator


@typed(str)
def add(a, b):
    print(a + b)


# Проверка
add("3", 5)
add(5, 5)
add('a', 'b')


def typed1(expected_type):
    def decorator(func):
        def numbers(a, b, c):
            if (isinstance(a, expected_type) and isinstance(b, expected_type)
                    and isinstance(c, expected_type)):
                func(a, b, c)
            else:
                print(f"Не верный тип аргумета, он должен быть типа {expected_type}")
        return numbers
    return decorator


@typed1(int)
def add1(a, b, c):
    print(a + b + c)


# Проверка
add1(5, 6, 7)


def typed2(expected_type):
    def decorator(func):
        def numbers(a, b, c):
            if (isinstance(a, expected_type) and isinstance(b, expected_type)
                    and isinstance(c, expected_type)):
                func(a, b, c)
            else:
                print(f"Не верный тип аргумета, он должен быть типа {expected_type}")
        return numbers
    return decorator


@typed2(float)
def add2(a, b, c):
    print(a + b + c)


# Проверка
add2(0.1, 0.2, 0.4)

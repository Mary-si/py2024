"""homework10"""

# Вернуть число
# Создайте декоратор, который проверяет, является ли результат функции числом
# и выводит сообщение об ошибке, если это не так. Вот некоторые подсказки:
#
# Внутри декоратора, после вызова функции,
# проверьте тип результата с помощью функции isinstance().
# Если тип не является числом,
# выведите сообщение об ошибке с помощью функции print().


def typed(expected_type):
    """проверяет, является ли результат функции числом"""
    def decorator(func):
        def numbers(a, b):
            if isinstance(a, expected_type) and isinstance(b, expected_type):
                func(a, b)
            else:
                print(f"Не верный тип аргумета, должно быть число,"
                      f"тип {expected_type}")
        return numbers
    return decorator


@typed(int)
def add(a, b):
    """суммируем все"""
    print(a + b)


# Проверка
add(3, 5)
add("5", 5)
add('a', 'b')

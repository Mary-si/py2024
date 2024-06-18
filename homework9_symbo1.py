"""homework9"""


# Напишите программу, которая бы работала следующим образом -
# находила символ "#" и если этот символ найден -
# удаляла предыдущий символ из строки.
# Ваша задача обработать строки с "#" символом.
#
# Примеры:
# "a#bc#d" ==>  "bd"
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""


def symbols(s):
    """находит символ "#" и если этот символ найден,
    удаляет символ "#" и предыдущий символ из строки"""
    i = 0
    result = []
    while i < len(s):
        if s[i] == "#":
            if result:
                result.pop()
        else:
            result.append(s[i])
        i += 1
    return "".join(result)


# Проверка
assert symbols("a#bc#d") == "bd"
assert symbols("abc#d##c") == "ab"
assert symbols("abc##d######") == ""
assert symbols("#######") == ""
assert symbols("") == ""

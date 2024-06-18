"""homework9"""


# Подсчет количества букв
# На вход подается строка, например, "cccbba"
# результат работы программы - строка “c3b2a"
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"


def count_s(a):
    """Преобразование из "cccbba" в c3b2a"""
    symbol = a[0]
    count = 0
    sum_sym = ""
    for i in a:
        if symbol == i:
            count += 1
        else:
            sum_sym += symbol + str(count)
            symbol = i
            count = 1
    sum_sym += symbol + str(count)
    return sum_sym.replace("1", "")


# Проверка
assert count_s("cccbba") == "c3b2a"
assert count_s("abeehhhhhccced") == "abe2h5c3ed"
assert count_s("aaabbceedd") == "a3b2ce2d2"
assert count_s("abcde") == "abcde"
assert count_s("aaabbdefffff") == "a3b2def5"

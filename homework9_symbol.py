"""homework9"""

# Подсчет количества букв
# На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"


def count_s(a):
    symbol = a[0]
    count = 0
    sum_sym = ""
    for i in range(len(a)):
        if symbol == a[i]:
            count += 1
        if symbol != a[i]:
            sum_sym += symbol
            sum_sym += str(count)
            symbol = a[i]
            count = 1
    sum_sym += str(symbol)
    sum_sym += str(count)
    return sum_sym.replace("1", "")


# Проверка
print(count_s("cccbba"))

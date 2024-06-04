"""homework9"""

# Напишите программу, которая бы работала следующим образом -
# находила символ "#" и если этот символ найден - удаляла предыдущий символ из строки.
# Ваша задача обработать строки с "#" символом.
#
# Примеры:
# "a#bc#d" ==>  "bd"
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""


# def symbols(a):
#     i = 0
#     result = []
#     while i < len(a):
#         if a[i] == "#":
#             if result:
#                 result.pop()
#         else:
#             result.append(a[i])
#             i += 1
#     return "".join(result)
#
#
# # Проверка
# print(symbols("a#bc#d"))
# print(symbols("abc#d##c"))
# print(symbols("abc##d######"))
# print(symbols("#######"))
# print(symbols(""))


def symbols(s):
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
print(symbols("a#bc#d"))
print(symbols("abc#d##c"))
print(symbols("abc##d######"))
print(symbols("#######"))
print(symbols(""))

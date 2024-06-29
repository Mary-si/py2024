"""homework8"""

# Последовательность
# Дана последовательность целых чисел в виде массива.
# Определите, можно ли получить строго возрастающую последовательность,
# удалив из массива не более одного элемента.
# Примечание: последовательность a0, a1, ..., an считается строго возрастающей,
# если a0 < a1 < ... < an. Последовательность, содержащая только один элемент,
# также считается строго возрастающей.

# Примеры
# Для последовательности = [1, 3, 2, 1], вывод должен быть решение = False.
# В этом массиве нет ни одного элемента, который можно было бы удалить,
# чтобы получить строго возрастающую последовательность.

# Для последовательности = [1, 3, 2] вывод должен быть = True.
# Вы можете удалить 3 из массива, чтобы получить строго возрастающую
# последовательность [1, 2]. Альтернативно можно убрать 2,
# чтобы получить строго возрастающую последовательность [1, 3].
# solution([1, 2, 3])
# solution([1, 2, 1, 2])
# solution([1, 3, 2, 1])
# solution([1, 2, 3, 4, 5, 3, 5, 6])
# solution([40, 50, 60, 10, 20, 30])

# 1
numbers = [1, 2, 3]

for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        print("False")
        break
else:
    print("True")

# 2
numbers = [1, 2, 1, 2]

for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        print("False")
        break
else:
    print("True")

# 3
numbers = [1, 2, 1, 2]

for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        print("False")
        break
else:
    print("True")

# 4
numbers = [1, 2, 3, 4, 5, 3, 5, 6]

for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        print("False")
        break
else:
    print("True")

# 5
numbers = [40, 50, 60, 10, 20, 30]

for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        print("False")
        break
else:
    print("True")

"""homework7"""

# Быки и коровы¶
# В классическом варианте игра рассчитана на двух игроков.
# Каждый из игроков задумываети
# и записывает тайное 4-значное число с неповторяющимися цифрами.
# Игрок, который начинает игру по жребию,
# делает первую попытку отгадать число.
# Попытка — это 4-значное число с неповторяющимися цифрами,
# сообщаемое противнику.
# Противник сообщает в ответ, сколько цифр угадано без совпадения
# с их позициями в тайном числе
# (то есть количество коров) и сколько угадано вплоть до позиции
# в тайном числе (то есть количество быков).
# При игре против компьютера игрок вводит комбинации одну за другой,
# пока не отгадает всю последовательность.
# Ваша задача реализовать программу,
# против которой можно сыграть в "Быки и коровы"
# Пример
# Загадано
# 2310
# Две коровы, один бык
# 3219
# Вы выиграли!

import random


def get_all_answers():
    """создавать список всех вариантов комбинаций"""
    ans = []
    for i in range(10000):
        tmp = str(i).zfill(4)
        # zfill - добавляет 0-ли к строке (если исходная строка короче)
        if len(set(map(int, tmp))) == 4:
            # len - длинна строки
            # set = берет 4 цифры и преобразует их в множество
            # (набор неповторяющихся эллементов)
            # map = функция ктр выделяет каждую циру из числа,
            # int = преобразование в целое число, tmp = строка из 4х цифр
            ans.append(list(map(int, tmp)))
    return ans


def get_one_answer(ans):
    """выбрать один ответ из списка возможны"""
    # выбрать число случайным образом
    num = random.choice(ans)
    return num


def input_number():
    """запросить ввести 4 неповторяющиеся цифры"""
    while True:
        nums = input("Введите 4 неповторяющиеся цифры: ")
        # проверяем на длинну 4 символа и isdigit - проверяет что это не цифры
        if len(nums) != 4 or not nums.isdigit():
            continue
        # 4 цифры преобразуем в список
        nums = list(map(int, nums))
        # проверяем на уникальность 4 цифры
        if len(set(nums)) == 4:
            break
    return nums


def check(nums, true_nums):
    """сравнить два числа и сообщить кол-во быков и коров"""
    bulls1, cows1 = 0, 0
    for i, num in enumerate(nums):
        if num in true_nums:
            # проверяем позицию цифры под цифрой на бык или корова
            if nums[i] == true_nums[i]:
                bulls1 += 1
            else:
                cows1 += 1
    return bulls1, cows1


def del_bad_answers(ans, enem, bull, cow):
    """проверить и удалить неверные числа для ввода"""
    for num in ans[:]:
        temp_bull, temp_cow = check(num, enem)
        if temp_bull != bull or temp_cow != cow:
            ans.remove(num)
    return ans


print("Игра быки и коровы")
answers = get_all_answers()
player = input_number()
enemy = get_one_answer(answers)

while True:
    print("Ход игрока")
    print("Угадайте число компьютера")
    number = input_number()
    bulls, cows = check(number, enemy)
    print("Быки: ", bulls, "Коровы: ", cows)
    if bulls == 4:
        print("Вы выиграли!")
        print("Компьютер загадал число: ", enemy)
        break

    print("Ход компьютера")
    enemy_try = get_one_answer(answers)
    print("Компьютер считает, что вы загадали число: ", enemy_try)
    bulls, cows = check(enemy_try, player)
    print("Быки: ", bulls, "Коровы: ", cows)
    if bulls == 4:
        print("Победил компьютер!")
        print("Компьютер загадал число: ", enemy)
        break
    elif:
        answers = del_bad_answers(answers, enemy_try, bulls, cows)

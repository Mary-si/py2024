"""homework7"""

# Статуи
# Вы получили в подарок на день рождения статуи разных размеров,
# каждая статуя имеет неотрицательный целочисленный размер.
# Поскольку Вам нравится доводить вещи до совершенства,
# то необходимо расположить их от меньшего к большему,
# чтобы каждая статуя была больше предыдущей ровно на 1.
# Для этого Вам могут понадобиться дополнительные статуи.
# Определите количество отсутствующих статуй.
# Пример Для статуй = [6, 2, 3, 8] результат должен быть = 3.
# Иными словами, у Вас отсутствуют статуи размеров 4, 5 и 7.

print("Статуи")

statues = [6, 2, 3, 8]
print(statues)

# проверить список на неотрицательные и целые числа
for i in statues:
    if i < 0 or i == 0:
        print("В списке ошибка. Список может содержать только"
              "положительные и целые числа", i)

# выбрать min и max значение из списка
y = min(statues)
z = max(statues)
print(y, z)

# узнать кол-во цифр в заданном списке
A = len(statues)
print(A)

# узнать кол-во цифр сколько цифр от 2 до 8
x = list(range(2, 9))
print(x)

# узнать кол-во цифр во всем списке включая недостающие цифры
p = len(x)
print(p)

# определить количество отсутствующих статуй
y = p - A
print("Количество отсутствующих статуй:", y)

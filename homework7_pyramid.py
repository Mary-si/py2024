"""homework7"""

# Пирамида
# Мы можем визуализировать художественную пирамиду ASCII с N уровнями,
# напечатав N рядов звездочек,
# где верхний ряд имеет одну звездочку в центре,
# а каждый последующий ряд имеет две дополнительные звездочки с каждой стороны.
# Вот как это выглядит, когда N равно 3.
#   *
#  ***
# *****

# Вот как это выглядит, когда N равно 5.
#     *
#    ***
#   *****
#  *******
# *********

# Необходимо написать программу, которая генерирует такую пирамиду
# со значением N, равным 10

print("Пирамида")

A = "*"
B = " "
N = 10

for i in range(N):  # i = 0, 1, 2, ...
    print(B*(N-1-i) + A*(i+1) + A*i)

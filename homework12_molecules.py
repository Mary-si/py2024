"""homework 12"""

# Напишите программу, которая обрабатывает строку - формулу молекулы,
# возвращает атомы из этой молекулы и их количество в виде словаря.
#
# Замечания:
# Скобки в формулах могут быть круглыми, квадратными и фигурными.
# Скобки могут быть вложены друг в друга.
# Индекс после скобки означает количество раз,
# которое повторяется каждый атом внутри скобок.
# Индекс после скобки не обязателен. Если его нет,
# значит содержимое скобок повторяется 1 раз.
#
# Примеры:
# H2O -> {H: 2, O: 1}
# Mg(OH)2 -> {Mg: 1, O: 2, H: 2}
# K4[ON(SO3)2]2 -> {K: 4, O: 14, N: 2, S: 4}


import re
from collections import Counter


def repl(m):
    """возвращает строко, ктр состоит из символов элемента"""
    return m[1] * int(m[2] if m[2] else 1)


def molecule(formula: str) -> dict:
    """принимает строку и возвращает словарь с кол-вом элементов"""
    while "(" in formula:
        formula = re.sub(r'\((\w*)\)(\d*)', repl, formula)
    while "[" in formula:
        formula = re.sub(r'\[(\w*)](\d*)', repl, formula)
    formula = re.sub(r'([A-Z][a-z]?)(\d*)', repl, formula)
    formula_dict = Counter(re.findall('[A-Z][a-z]*', formula))
    return formula_dict


if __name__ == '__main__':
    assert molecule("H2O") == {'H': 2, 'O': 1}
    assert molecule("Mg(OH)2") == {'Mg': 1, 'O': 2, 'H': 2}
    assert molecule("K4[ON(SO3)2]2") == {'K': 4, 'O': 14, 'N': 2, 'S': 4}

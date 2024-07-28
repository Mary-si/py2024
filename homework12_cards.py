"""homework 12"""

# Колода карт
#
# Напишите программу которая содержит список карт,
# умеет их перемешивать и позволяет пользователю достать карту
# из колоды по ее номеру.
# Всего в колоде 54 карт. Класс Card содержит спискок номеров
# карт и список мастей.

import random


class Card:
    """информация о картах"""
    number_list = [2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A", "Joker"]
    mast_list = ["clubs", "diamonds", "hearts", "spades"]

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __repr__(self):
        return f"{self.number} {self.mast}"


class CardsDeck:
    """выбор карты"""
    def __init__(self):
        self.cards = [Card(number, mast) for number in Card.number_list[:-1]
                      for mast in Card.mast_list]
        self.cards.extend([Card("Joker", "Red")])
        self.cards.extend([Card("Joker", "Black")])

    def shuffle(self):
        """выбор"""
        random.shuffle(self.cards)

    def get(self, card_n):
        """выбор"""
        if 1 <= card_n <= 54:
            return self.cards[card_n - 1]
        return ValueError("Номер карты должен быть в диапазоне от 1 до 54")


deck = CardsDeck()
deck.shuffle()
card_number = int(input("Выберите карту из колоды в 54 карт: "))
card = deck.get(card_number)
print(f"You card is: {card}")
# Hearts 10

card_number = int(input("Выберите карту из колоды в 54 карт:"))
card = deck.get(card_number)
print(f"You card is: {card}")
# Diamonds 6

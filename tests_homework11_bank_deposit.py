"""homework18"""

# Создайте класс вклад. Который содержит необходимые поля и методы,
# например сумма вклада и его срок.
#
# Пользователь делает вклад в размере N рублей сроком на R лет под 10% годовых
# (вклад с возможностью ежемесячной капитализации - это означает,
# что проценты прибавляются к сумме вклада ежемесячно).
#
# Написать класс Bank, метод deposit принимает аргументы N и R,
# и возвращает сумму, которая будет на счету пользователя.
#
# https://myfin.by/wiki/term/kapitalizaciya-procentov

# Создайте отдельный модуль для тестов.
# Импортируйте функции из модуля.
# Напишите тесты на проверку работоспособности приложения.
# Тесты должны проверять как положительный результат, так и отрицательный.
# Тесты запускаются с помощью unittest


import unittest
from datetime import datetime
from homework11_bank_deposit import Deposit, Bank


class TestDeposit(unittest.TestCase):
    """проверка депозитов"""
    def setUp(self):
        """проверка депозитов"""
        self.deposit = Deposit("01.01.2005", "01.01.2020")

    def tearDown(self):
        """очистка после тестов"""
        del self.deposit

    def test_deposit_start_date_is_datetime(self):
        """проверка что deposit_start_date это объект datetime"""
        self.assertIsInstance(self.deposit.deposit_start_date, datetime,
                              "deposit_start_date должен"
                              "быть объектом datetime")

    def test_deposit_end_date_is_datetime(self):
        """проверка что deposit_end_date это объект datetime"""
        self.assertIsInstance(self.deposit.deposit_start_date, datetime,
                              "deposit_end_date должен быть объектом datetime")


class TestBank(unittest.TestCase):
    """поверка инфорации о договорах пользователя"""
    def setUp(self):
        """поверка инфорации о договорах пользователя"""
        self.bank = Bank(1000, 1, 0.01)

    def tearDown(self):
        """очистка после тестов"""
        del self.bank

    def test_calculate_correctness(self):
        """проверка корректности работы калькулятора"""
        expected_amount = 1000 * (1 + 0.01 / 12) ** 12
        self.assertAlmostEqual(self.bank.calculate(),
                               expected_amount, places=2,
                               msg="Итоговая сумма"
                                   "депозита рассчитана неверно")

    def test_calculate_zero_amount(self):
        """проверка на нулевые значения суммы депозита"""
        self.bank.deposit_amount = 0
        self.assertEqual(self.bank.calculate(), 0,
                         "Итоговая сумма депозита должна быть"
                         "0 при нулевой сумме депозита")


if __name__ == "__main__":
    unittest.main()

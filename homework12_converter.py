"""homework 12"""

# Конвертер валют
#
# Расширьте функционал класса Bank из домашней работы #11.
# Добавьте новый класс Currency, который умеет конвертировать
# различные валюты(USD, EUR, ...) в заданную валюту.
#
# bank = Bank(..)
#
# vasya = Person('USD', 10)
# petya = Person('EUR', 5)
#
# # Если валюта не задана, то конвертация происходит в BYN:
# assert bank.exchange_currency(vasya.currency, vasya.amount) ==
# (32.69, "BYN"), <error message>
# assert bank.exchange_currency(petya.currency, petya.amount) ==
# (35.20, "BYN"), <error message>
#
# # Конвертация в заданную валюту BYN:
# assert bank.exchange_currency(vasya.currency, vasya.amount, 'EUR')==
# (9.29, "EUR"), <error message>
# assert bank.exchange_currency(petya.currency, petya.amount, 'USD') ==
# (10.76, "USD"), <error message>


from datetime import datetime


class Deposit:  # pylint: disable=too-few-public-methods
    """Инфорация депозитов"""
    # создаем методы класса
    def __init__(self, deposit_start_date, end_date_deposit):
        self.deposit_start_date = datetime.strptime(deposit_start_date,
                                                    "%d.%m.%Y")
        self.end_date_deposit = datetime.strptime(end_date_deposit,
                                                  "%d.%m.%Y")


# pylint: disable=duplicate-code
# Your duplicate lines of code here
# pylint: enable=duplicate-code


deposit_1 = Deposit("08.09.2021", "08.09.2025")
deposit_2 = Deposit("02.03.2022", "02.03.2025")
deposit_3 = Deposit("01.01.2025", "31.12.2025")


class Bank:  # pylint: disable=too-few-public-methods
    """Инфорация о договорах пользователя"""
    def __init__(self, deposit_amount, deposit_term_year, percent_deposit):
        self.deposit_amount = deposit_amount
        self.deposit_term_year = deposit_term_year
        self.percent_deposit = percent_deposit

    def calculate(self):
        """калькулятор """
        while range(self.deposit_term_year * 12):
            self.deposit_amount += (self.deposit_amount *
                                    (self.percent_deposit / 12))
        return self.deposit_amount


user_1 = Bank(20000, 4, 0.05)
user_2 = Bank(5000, 3, 0.03)
user_3 = Bank(2000, 1, 0.01)


class Currency:  # pylint: disable=too-few-public-methods
    """конвертер"""
    EUR = 3.520
    USD = 3.269

    # создаем методы класса
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def exchange_currency(self, to_currency=None):
        """конвертер"""
        converter = {"USD": Currency.USD, "EUR": Currency.EUR, "BYN": 1}
        if to_currency not in converter:
            raise ValueError("Неподдерживаемая валюта для конвертации")
        if self.currency not in converter:
            return ValueError("Неподдерживаемая исходная валюта")
        if to_currency == "BYN":
            return self.amount * converter[self.currency], "BYN"
        return ((self.amount / converter[self.currency]) *
                converter[to_currency], to_currency)


# Проверка
vasya = Currency("USD", 10)
petya = Currency("EUR", 5)

# Если валюта не задана, то конвертация происходит в BYN:
assert (Currency.exchange_currency(vasya.currency, vasya.amount) ==
        (32.69, "BYN")), "Ошибка конвертации в BYN"
assert (Currency.exchange_currency(petya.currency, petya.amount) ==
        (35.20, "BYN")), "Ошибка конвертации в BYN"

# Конвертация в заданную валюту:
assert (Currency.exchange_currency(vasya.currency, vasya.amount) ==
        (9.29, "EUR")), "Ошибка конвертации в EUR"
assert (Currency.exchange_currency(petya.currency, petya.amount) ==
        (10.76, "USD")), "Ошибка конвертации в USD"

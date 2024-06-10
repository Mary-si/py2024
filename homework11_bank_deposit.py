"""homework11"""

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


class Deposit:
    """Инфорация депозитов"""
    # атрибуты класса
    all_deposit = 0

    # создаем методы класса
    def __init__(self, deposit_start_date, end_date_deposit):
        self.deposit_start_date = deposit_start_date
        self.end_date_deposit = end_date_deposit
        Deposit.all_deposit += 1


deposit_1 = Deposit("08.09.2021", "08.09.2025")
deposit_2 = Deposit("02.03.2022", "02.03.2025")
deposit_3 = Deposit("01.01.2025", "31.12.2025")


class Bank:
    """Инфорация о договорах пользователя"""


    def __init__(self, deposit_amount, deposit_term_year, percent_deposit):
        self.deposit_amount = deposit_amount
        self.deposit_term_year = deposit_term_year
        self.percent_deposit = percent_deposit

    def calculate(self):
        """калькулятор"""
        for i in range(self.deposit_term_year * 12):
            self.deposit_amount += (self.deposit_amount *
                                    (self.percent_deposit / 12))
        return self.deposit_amount


user_1 = Bank(20000, 4, 0.05)
user_2 = Bank(5000, 3, 0.03)
user_3 = Bank(2000, 1, 0.01)

# Проверка
final_amount_user_1 = user_1.calculate()
print(f"Сумма на счету у пользователя {user_1.deposit_term_year} лет,"
      f"будет {final_amount_user_1:.2f} рублей")

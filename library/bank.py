"""homework22"""


class Bank:  # pylint: disable=too-few-public-methods
    """Инфорация о договорах пользователя"""
    def __init__(self, deposit_amount, deposit_term_year, percent_deposit):
        self.deposit_amount = deposit_amount
        self.deposit_term_year = deposit_term_year
        self.percent_deposit = percent_deposit

    def calculate(self):
        """калькулятор """
        for _ in range(self.deposit_term_year * 12):
            self.deposit_amount += (self.deposit_amount *
                                    (self.percent_deposit / 12))
        return self.deposit_amount

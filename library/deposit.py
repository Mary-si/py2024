"""homework22"""


from datetime import datetime


class Deposit:  # pylint: disable=too-few-public-methods
    """Инфорация депозитов"""
    # создаем методы класса
    def __init__(self, deposit_start_date, end_date_deposit):
        self.deposit_start_date = datetime.strptime(deposit_start_date,
                                                    "%d.%m.%Y")
        self.end_date_deposit = datetime.strptime(end_date_deposit,
                                                  "%d.%m.%Y")

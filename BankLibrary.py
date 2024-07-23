"""homework22"""

from homework11_bank_deposit import Deposit, Bank


class BankLibrary:
    @staticmethod
    def create_deposit(deposit_start_date, end_date_deposit):
        """Создает экземпляр депозита и возвращает его."""
        return Deposit(deposit_start_date, end_date_deposit)

    @staticmethod
    def create_bank_account(deposit_amount, deposit_term_year, percent_deposit):
        """Создает экземпляр банковского счета и возвращает его."""
        return Bank(float(deposit_amount), int(deposit_term_year), float(percent_deposit))

    @staticmethod
    def calculate_final_amount(bank_account):
        """Выполняет расчет итоговой суммы на банковском счете."""
        return bank_account.calculate()

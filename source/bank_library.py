"""homework22"""

import logging
from .homework11_bank_deposit import Deposit, Bank

"""Настройка логгирования"""
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class BankLibrary:
    """BankLibrary"""
    @staticmethod
    def create_deposit(deposit_start_date, end_date_deposit):
        """Создает экземпляр депозита и возвращает его"""
        deposit = Deposit(deposit_start_date, end_date_deposit)
        logger.info("Created deposit: %s", deposit)
        return deposit

    @staticmethod
    def create_bank_account(deposit_amount, deposit_term_year, percent_deposit):
        """Создает экземпляр банковского счета и возвращает его"""
        bank_account = Bank(float(deposit_amount),
                            int(deposit_term_year), float(percent_deposit))
        logger.info("Created bank account: %s", bank_account)
        return bank_account

    @staticmethod
    def calculate_final_amount(bank_account):
        """Выполняет расчет итоговой суммы на банковском счете"""
        final_amount = bank_account.calculate()
        logger.info("Calculated final amount: %s", final_amount)
        return final_amount

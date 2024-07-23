"""homework21"""


# Создайте класс book с именем книги, автором, кол-м страниц, ISBN,
# флагом, зарезервирована ли книги или нет.
#
# Создайте класс пользователь который может брать книгу,
# возвращать, бронировать.
#
# Если другой пользователь хочет взять зарезервированную книгу
# (или которую уже кто-то читает - надо ему про это сказать).


# Создайте отдельный модуль для тестов.
# Импортируйте функции из модуля.
# Напишите тесты на проверку работоспособности приложения.
# Тесты должны проверять как положительный результат, так и отрицательный.
# Тесты используют библиотеку logging\loguru для логирования
# Добавьте простой отчет к вашим тестам используя библиотеку pytest-html
# https://pytest-html.readthedocs.io/en/latest/
# https://pytest-with-eric.com/plugins/pytest-html/
# Тесты запускаются с помощью pytest
# Добавьте в файл .gitignore все файлы и папки которые генерирует
# в процессе своей работы pytest и pytest-html,
# те в репозитории с кодом не должно быть лишних файлов
#
# Есть возможность запустить тесты с разным уровнем логгирования без изменения кода
# (те передача уровня логгирования во время запуска тестов)

# Примерная структура проекта:
# homework21/
# .github/
# - ...
# - tests/
# -- test_<bank-app>.py    <-- Файл с тестами для тестирования банка
# -- test_<library-app>.py <-- Файл с тестами для тестирования библиотеки
# - source/
# -- <library>.py          <-- Модуль реализуюший функционал библиотеки
# -- <bank>.py             <-- Модуль реализуюший функционал банка
# .gitignore
# requirements.txt
# ...
# Note: Помимо кода, пулл реквест должен содержать в себе файл-репорт
# (прикрепленный к пулл реквесту) который генерируется по результатам запуска тестов.
#
# Note2: Названия файлов примерное


import pytest
import numpy as np
from datetime import datetime
import logging
import sys
import os
from unittest import TestCase
from homework11_bank_deposit import Deposit, Bank

# Добавление пути к модулям
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
                    filename="test_homework21_bank_deposit_pytest.log", filemode='w')
logger = logging.getLogger(__name__)


@pytest.fixture
def deposit():
    """информация о депозитах"""
    return Deposit("01.02.2020", "01.02.2022")


@pytest.fixture
def bank():
    """информация о договорах пользователя"""
    return Bank(10, 2, 0.05)


@pytest.fixture
def almostequal():
    """almostequal"""
    return np.testing.assert_almost_equal


@pytest.fixture
def equal():
    """equal"""
    return TestCase().assertEqual


def test_deposit_start_date_is_datetime(deposit):
    """проверка что deposit_start_date это объект datetime"""
    logger.info("Проверка что deposit_start_date это объект datetime")
    assert isinstance(deposit.deposit_start_date, datetime), \
        "deposit_start_date должен быть объектом datetime"


def test_deposit_end_date_is_datetime(deposit):
    """проверка что deposit_end_date это объект datetime"""
    logger.info("Проверка что deposit_end_date это объект datetime")
    assert isinstance(deposit.end_date_deposit, datetime), \
        "deposit_end_date должен быть объектом datetime"


def test_calculate_correctness(bank, almostequal):
    """проверка корректности работы калькулятора"""
    logger.info("Проверка корректности работы калькулятора")
    expected_amount = 10 * (1 + 0.05 / 12) ** (2 * 12)
    almostequal(bank.calculate(), expected_amount, decimal=2), \
        "Итоговая сумма депозита рассчитана неверно"


def test_calculate_zero_amount(bank, equal):
    """проверка на нулевые значения суммы депозита"""
    logger.info("Проверка на нулевые значения суммы депозита")
    bank.deposit_amount = 0
    equal(bank.calculate(), 0), \
        "Итоговая сумма депозита должна быть 0 при нулевой сумме депозита"
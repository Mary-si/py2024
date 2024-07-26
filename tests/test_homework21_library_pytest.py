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


import logging
import os
import sys
import re

import pytest

from homework11_library import Book, User


# Добавление пути к модулям
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../source")))


# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="test_homework21_library_pytest.log")


@pytest.fixture
def book():
    """проверка книг"""
    return Book("Название книги", "Автор книги", 3000, "111-1-11-111111-1")


@pytest.fixture
def user():
    """информация о пользователях"""
    return User("Имя", "Фамилия", "1111111")


def test_pages_is_integer(book):
    """проверка что pages это целое число"""
    logger.info("Проверка, что количество страниц это целое число")
    assert isinstance(book.pages, int), "Количество страниц должно быть целым числом"


def test_isbn_format(book):
    """проверка, что ISBN имеет верный формат"""
    logger.info("Проверка, что ISBN имеет верный формат")
    pattern = r"^\d{3}-\d-\d{2}-\d{6}-\d$"
    result = re.match(pattern, book.isbn)
    assert result is not None, "ISBN должен соответствовать формату"


def test_isbn_contains_only_digits(book):
    """проверка что ISBN содержит только цифры"""
    logger.info("Проверка, что ISBN содержит только цифры")
    digits_only = book.isbn.replace("-", "")
    assert digits_only.isdigit(), "ISBN должен содержать только цифры"


def test_take_success(book):
    """проверка взятие книги, когда она доступна и не зарезервирована"""
    logger.info("Проверка, что книга взята")
    book.is_available = True
    book.is_reserved = False
    result = book.take()
    assert result == True, "Книга должна быть взята"  # noqa: E712
    logger.info("Книга успешно взята")


def test_take_fail_reserved(book):
    """проверка взятие книги, когда она недоступна, т.е. уже зарезервирована"""
    logger.info("Проверка взятие книги, когда она недоступна, т.е. уже зарезервирована")
    book.is_available = False
    book.is_reserved = True
    result = book.take()
    assert result == False, "Книга не должна быть взята, тк она зарезервирована"  # noqa: E712
    logger.info("Не удалось взять зарезервированную книгу")


def test_take_fail_unavailable(book):
    """проверка взятие книги, когда она недоступна"""
    logger.info("Проверка взятие книги, когда она недоступна")
    book.is_available = False
    book.is_reserved = False
    result = book.take()
    assert result == False, "Книга не должна быть взята, тк она недоступна"  # noqa: E712
    logger.info("Не удалось взять недоступную книгу")


def test_returned(book):
    """книга возвращена"""
    logger.info("Проверка, что книга возвращена")
    book.is_available = False
    book.is_reserved = True
    result = book.returned()
    assert result == True, "Книга должна быть возвращена"  # noqa: E712
    assert book.is_available == True, "Книга должна быть доступна после возврата"  # noqa: E712
    assert book.is_reserved == False, "Книга не может быть зарезервирована после возврата"  # noqa: E712
    logger.info("Книга успешно возвращена")


def test_reservation_success(book):
    """книга успешно зарезервирована, когда она свободна и не зарезервирована"""
    logger.info("Проверка, что книга успешно зарезервирована")
    book.is_available = True
    book.is_reserved = False
    result = book.reservation()
    assert result == True, "Книга должна быть зарезервирована"  # noqa: E712
    logger.info("Не удалось зарезервировать книгу")


def test_reservation_fail_unavailable(book):
    """Книга не может быть зарезервирована, поскольку она недоступна"""
    logger.info("Проверка, что книга не может быть зарезервирована, поскольку она недоступна")
    book.is_available = False
    result = book.reservation()
    assert result == "Книга недоступна для резервирования"
    logger.info("Не удалось зарезервировать книгу")


def test_reservation_fail_reserved(book):
    """Книга не может быть зарезервирована, поскольку она зарезервирована"""
    logger.info("Проверка, что книга не может быть зарезервирована, поскольку она зарезервирована")
    book.is_available = True
    book.is_reserved = True
    result = book.reservation()
    assert result == "Книга уже зарезервирована"
    logger.info("Не удалось зарезервировать книгу")


def test_take_book(user, book):
    """Книга взята пользователем и статус книги изменен"""
    logger.info("Проверка, что книга взята пользователем и статус книги изменен")
    user.take_book(book)
    assert user.took_book == book, "Пользователь должен взять книгу"
    assert not book.is_available, "Книга должна быть недоступна"
    logger.info("Книга взята пользователем")


def test_return_book(user, book):
    """Книга возвращена пользователем и статус книги изменен"""
    logger.info("Проверка, что книга возвращена пользователем и статус книги изменен")
    user.take_book(book)
    user.return_book(book)
    assert user.took_book is None, "Пользователь вернул книгу"
    assert book.is_available, "Книга доступна после возврата"
    logger.info("Книга возвращена")


def test_book_status(book):
    """Проверка статуса книги"""
    logger.info("Проверка статуса книги")
    assert book.title == "Название книги", \
        "Название книги должно быть корректным"
    assert book.is_available is True, \
        "Книга должна быть доступна"
    assert book.is_reserved is False, \
        "Книга не должна быть зарезервирована"

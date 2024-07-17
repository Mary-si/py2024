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
# в процессе своей работы pytest и pytest-html, те в репозитории с кодом не должно быть лишних файлов
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
import re
from homework11_library import Book, User
from loguru import logger


@pytest.fixture
def book():
    """проверка книг"""
    return Book("Название книги", "Автор книги",
                3000, "111-1-11-111111-1")


@pytest.fixture
def user():
    """информация о пользователях"""
    return User("Имя", "Фамилия", "1111111")


def test_pages_is_integer(book):
    """проверка что pages это целое число"""
    logger.info("Проверка, что количество страниц это целое число")
    assert isinstance(book.pages, int), \
        "Количество страниц должно быть целым числом"


def test_isbn_format(book):
    """проверка, что ISBN имеет верный формат"""
    logger.info("Проверка, что ISBN имеет верный формат")
    pattern = r"^\d{3}-\d-\d{2}-\d{6}-\d$"
    assert re.match(pattern, book.isbn), \
        "ISBN не соответствует формату 111-1-11-111111-1"


def test_isbn_contains_only_digits(book):
    """проверка что ISBN содержит только цифры"""
    logger.info("Проверка, что ISBN содержит только цифры")
    digits_only = book.isbn.replace("-", "")
    assert digits_only.isdigit(), \
        "ISBN должен содержать только цифры"


def test_take_success(book):
    """проверка взятие книги, когда она доступна и не зарезервирована"""
    logger.info("Проверка взятие книги, когда она доступна и не зарезервирована")
    book.is_available = True
    book.is_reserved = False
    result = book.take()
    assert result == "Книга взята"


def test_take_fail_reserved(book):
    """проверка взятие книги, когда она недоступна,
    т.е. уже зарезервирована"""
    logger.info("Проверка взятие книги, когда она недоступна, "
                "т.е. уже зарезервирована")
    book.is_available = False
    book.is_reserved = True
    result = book.take()
    assert result == "Книга зарезервирована"


def test_take_fail_unavailable(book):
    """проверка взятие книги, когда она недоступна"""
    logger.info("Проверка взятие книги, когда она недоступна")
    book.is_available = False
    book.is_reserved = False
    result = book.take()
    assert result == "Книга недоступна"


def test_returned(book):
    """книга возвращена"""
    logger.info("Проверка, что книга возвращена")
    book.is_available = False
    book.is_reserved = True
    result = book.returned()
    assert result == "Книга возвращена"


def test_reservation_success(book):
    """книга успешно зарерервирована, когда она свободна
    и не зарезервирована"""
    logger.info("Проверка, что книга успешно зарерервирована,"
                "когда она свободна и не зарезервирована")
    book.is_available = True
    book.is_reserved = False
    result = book.reservation()
    assert result == "Книга зарезервирована"


def test_reservation_fail_unavailable(book):
    """книга не может быть зарерервирована, тк она недоступна"""
    logger.info("Проверка, что книга не может быть зарерервирована,"
                "тк она недоступна")
    book.is_available = False
    book.is_reserved = False
    result = book.reservation()
    assert result == "Книга недоступна для резервирования"


def test_reservation_fail_reserved(book):
    """книга не может быть зарерервирована, тк она зарерервирована"""
    logger.info("Проверка, что книга не может быть зарерервирована,"
                "тк она зарерервирована")
    book.is_available = False
    book.is_reserved = True
    result = book.reservation()
    assert result == "Книга зарезервирована"


# как тут делать если в задаче отбражается так:
#
# def __init__(self, name, surname, id_number):
#     self.name = name
#     self.surname = surname
#     self.__id_number = id_number
#     self.took_book = None
def test_protected_id_number(user):
    """проверка, что id_number является защищенным атрибутом"""
    logger.warning("Проверка, что __id_number является защищенным атрибутом")
    with pytest.raises(AttributeError):
        _ = user.__id_number


def test_id_number(user):
    """проверка, что id_number содержит только цифры"""
    logger.warning("Проверка, что id_number содержит только цифры")
    assert user.id_number.isdigit(), \
        "id_number должен содержать только цифры"


def test_id_number_format(user):
    """проверка что id_number состоит из 7 цифр"""
    logger.warning("Проверка, что id_number состоит из 7 цифр")
    assert len(user.id_number) == 7, "id_number должен состоять из 7 цифр"


def test_take_book(user, book):
    """книга взята пользователем и статус книги изменен"""
    logger.info("Проверка, что книга взята пользователем"
                "и статус книги изменен")
    user.take_book(book)
    assert user.took_book == book, "Пользователь должен взять книгу"
    assert not book.is_available, "Книга должна быть недоступна"


def test_return_book(user, book):
    """книга возвращена пользователем и статус книги изменен"""
    logger.info("Проверка, что книга возвращена пользователем"
                "и статус книги изменен")
    user.take_book(book)
    user.return_book(book)
    assert user.took_book is None, "Пользователь должен вернуть книгу"
    assert book.is_available, "Книга доолжна быть доступна"


def test_reservation_book(user, book):
    """книга зарезервирована и статус книги изменен"""
    logger.info("Проверка, что книга зарезервирована "
                "и статус книги изменен")
    user.reservation_book(book)
    assert book.is_reserved, "Книга долдна быть зарезервирована"

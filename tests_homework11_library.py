"""homework18"""


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
# Тесты запускаются с помощью unittest


import unittest
import re
from homework11_library import Book, User


class TestBook(unittest.TestCase):
    """проверка книг"""
    def setUp(self):
        """проверка книг"""
        self.book = Book("Название книги", "Автор книги",
                         3000, "111-1-11-111111-1")

    def tearDown(self):
        """очистка после тестов"""
        del self.book

    def test_pages_is_integer(self):
        """проверка что pages это целое число"""
        self.assertIsInstance(self.book.pages, int, "Количество страниц должно быть целым числом")

    def test_isbn_format(self):
        """проверка что ISBN имеет верный формат"""
        pattern = r"^\d{3}-\d-\d{2}-\d{6}-\d$"
        self.assertTrue(re.match(pattern, self.book.isbn),
                        "ISBN не соответствует формату 111-1-11-111111-1")

    def test_isbn_contains_only_digits(self):
        """проверка что ISBN содержит только цифры"""
        digits_only = self.book.isbn.replace("-", "")
        self.assertTrue(digits_only.isdigit(), "ISBN должен содержать только цифры")

    def test_take_success(self):
        """проверка взятие книги, когда она доступна и не зарезервирована"""
        self.book.is_available = True
        self.book.is_reserved = False
        result = self.book.take()
        self.assertTrue(result)
        self.assertFalse(self.book.is_available)

    def test_take_fail_reserved(self):
        """проверка взятие книги, когда она недоступна, т.е. уже зарезервирована"""
        self.book.is_available = False
        self.book.is_reserved = True
        result = self.book.take()
        self.assertFalse(result)
        self.assertTrue(self.book.is_available)

    def test_take_fail_unavailable(self):
        """проверка взятие книги, когда она недоступна"""
        self.book.is_available = False
        self.book.is_reserved = False
        result = self.book.take()
        self.assertFalse(result)
        self.assertFalse(self.book.is_available)

    def test_returned(self):
        """книга возвращена"""
        self.book.is_available = False
        self.book.is_reserved = True
        result = self.book.returned()
        self.assertTrue(result)
        self.assertTrue(self.book.is_available)
        self.assertFalse(self.book.is_reserved)

    def test_reservation_success(self):
        """книга успешно зарерервирована, когда она свободна
        и не зарезервирована"""
        self.book.is_available = True
        self.book.is_reserved = False
        result = self.book.reservation()
        self.assertTrue(result)
        self.assertTrue(self.book.is_reserved)

    def test_reservation_fail_unavailable(self):
        """книга не может быть зарерервирована, тк она недоступна"""
        self.book.is_available = False
        self.book.is_reserved = False
        result = self.book.reservation()
        self.assertFalse(result)
        self.assertFalse(self.book.is_reserved)

    def test_reservation_fail_reserved(self):
        """книга не может быть зарерервирована, тк она зарерервирована"""
        self.book.is_available = False
        self.book.is_reserved = True
        result = self.book.reservation()
        self.assertFalse(result)
        self.assertTrue(self.book.is_reserved)


class TestUser(unittest.TestCase):
    """информация о пользователях"""
    def setUp(self):
        """информация о пользователях"""
        self.user = User("Имя", "Фамилия", "1111111")
        self.book = Book("Название книги", "Автор книги",
                         3000, "111-1-11-111111-1")

    def tearDown(self):
        """очистка после тестов"""
        del self.user
        del self.book

# как тут делать если в задаче отбражается так:
#
# def __init__(self, name, surname, id_number):
#     self.name = name
#     self.surname = surname
#     self.__id_number = id_number
#     self.took_book = None

    # def test_id_number(self):
    #     """проверка что id_number содержит только цифры"""
    #     self.assertTrue(self.user.id_number.isdigit(),
    #                     "id_number должен содержать только цифры")
    #
    # def test_id_number_format(self):
    #     """проверка что id_number состоит из 7 цифр"""
    #     self.assertEqual(len(self.user.id_number), 7,
    #                      "id_number должен состоять из 7 цифр")

    def test_take_book(self):
        """книга взята пользователем и статус книги изменен"""
        self.user.take_book(self.book)
        self.assertEqual(self.user.took_book, self.book)
        self.assertFalse(self.book.is_available)

    def test_return_book(self):
        """книга возвращена пользователем и статус книги изменен"""
        self.user.take_book(self.book)
        self.user.return_book(self.book)
        self.assertIsNone(self.user.took_book)
        self.assertTrue(self.book.is_available)

    def test_reservation_book(self):
        """книга зарезервирована и статус книги изменен"""
        self.user.reservation_book(self.book)
        self.assertTrue(self.book.is_reserved)


if __name__ == "__main__":
    unittest.main()

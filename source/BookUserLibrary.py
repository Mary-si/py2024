"""homework22"""

import logging
from homework11_library import Book, User

# Настройка логгирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class BookUserLibrary:
    @staticmethod
    def create_book(title, author, pages, isbn):
        """Создает экземпляр книги и возвращает его."""
        book = Book(title, author, pages, isbn)
        logger.info(f"Created book: {book}")
        return book

    @staticmethod
    def create_user(name, surname, id_number):
        """Создает экземпляр пользователя и возвращает его."""
        user = User(name, surname, id_number)
        logger.info(f"Created user: {user}")
        return user

    @staticmethod
    def take_book(user, book):
        """Вызывает метод взятия книги у пользователя."""
        user.took_book = book
        logger.info(f"{user} took book: {book}")

    @staticmethod
    def return_book(user, book):
        """Вызывает метод возврата книги у пользователя."""
        if user.took_book == book:
            user.took_book = None
            logger.info(f"{user} returned book: {book}")
        else:
            logger.warning(f"{user} did not take book: {book}")

    @staticmethod
    def reserve_book(user, book):
        """Резервирует книгу для пользователя, используя атрибут took_book."""
        user.took_book = book
        logger.info(f"{user} reserved book: {book}")

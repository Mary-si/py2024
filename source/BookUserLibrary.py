"""homework22"""

from homework11_library import Book, User


class BookUserLibrary:
    @staticmethod
    def create_book(title, author, pages, isbn):
        """Создает экземпляр книги и возвращает его."""
        return Book(title, author, pages, isbn)

    @staticmethod
    def create_user(name, surname, id_number):
        """Создает экземпляр пользователя и возвращает его."""
        return User(name, surname, id_number)

    @staticmethod
    def take_book(user, book):
        """Вызывает метод взятия книги у пользователя."""
        user.take_book(book)

    @staticmethod
    def return_book(user, book):
        """Вызывает метод возврата книги у пользователя."""
        user.return_book(book)

    @staticmethod
    def reserve_book(user, book):
        """Вызывает метод резервирования книги у пользователя."""
        user.reservation_book(book)

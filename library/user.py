"""homework22"""


from book import Book


class User:
    """Информация о пользователях"""

    # создаем методы класса
    def __init__(self, name, surname, id_number):
        self.name = name
        self.surname = surname
        self.__id_number = id_number
        self.took_book = None

    def take_book(self, book):
        """когда взяли книгу"""
        if book.take():
            self.took_book = book
            print(f"Пользователь: {self.name} "
                  f"{self.surname}, {self.__id_number}."
                  f"Взял книгу: {book.title}")
        else:
            print(f"Книга ({book.title}) взята или"
                  f"зарезервирована пользователем: "
                  f"{self.name} {self.surname}, {self.__id_number}")

    def return_book(self, book):
        """когда вернули книгу"""
        if self.took_book == book:
            book.returned()
            self.took_book = None
            print(f"Пользователь: {self.name}"
                  f"{self.surname}, {self.__id_number}."
                  f"Вернул книгу: {book.title}")
        else:
            print(f"У пользователя {self.name} {self.surname},"
                  f"{self.__id_number} нет взятых книг")

    def reservation_book(self, book):
        """когда зарезервировали книгу"""
        if book.reservation():
            print(f"Пользователь: {self.name} "
                  f"{self.surname}, {self.__id_number}."
                  f"Забронировал книгу: {book.title}")

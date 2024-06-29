"""homework11"""


# Создайте класс book с именем книги, автором, кол-м страниц, ISBN,
# флагом, зарезервирована ли книги или нет.
#
# Создайте класс пользователь который может брать книгу,
# возвращать, бронировать.
#
# Если другой пользователь хочет взять зарезервированную книгу
# (или которую уже кто-то читает - надо ему про это сказать).

class Book:
    """Инфорация о книгах"""

    # создаем методы класса
    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.status = True
        # True - доступна. False - взята. None - зарезервирована

    # def check_status_book(self):
    #     """статус """
    #     return self.flag

    def take(self):
        """статус"""
        if self.status is True:
            self.status = False
            return True
        return False

    def returned(self):
        """статус"""
        self.status = True

    def reservation(self):
        """статус"""
        if self.status is True:
            self.status = None
            return True
        return False


book_1 = Book("Tree", "Thomas Wyatt", 180,
              "978-5-06-002611-5")
book_2 = Book("Sea", "William Shakespeare", 230,
              "978-3-16-148410-0")
book_3 = Book("Cat", "Leo Rangell", 300,
              "978-6-08-128515-1")


class User:
    """Информация о пользователях"""

    # создаем методы класса
    def __init__(self, name, surname, id_number):
        self.name = name
        self.surname = surname
        self.__id_number = id_number
        self.took_book = None
        self.returned_book = None
        self.reservated_book = None

    def take_book(self, book):
        """когда взяли книгу"""
        if book.take():
            self.took_book = book
            print(f"Пользователь взял книгу: {self.name}"
                  f"{self.surname} {self.__id_number}")
        else:
            print(f"Книга взята или зарезервирована пользователем"
                  f"{self.name} {self.surname}, {self.__id_number}")

    def return_book(self, book):
        """когда вернули книгу"""
        if self.took_book == book:
            book.returned()
            self.took_book = None
            print(f"Пользователь вернул книгу: {self.name},"
                  f"{self.surname}, {self.__id_number}")
        else:
            print(f"У пользователя {self.name},{self.surname},"
                  f"{self.__id_number} нет взятых книг")

    def reservation_book(self, book):
        """когда зарезервировали книгу"""
        if book.reservation():
            self.reservated_book = book
            print(f"Пользователь забронировал книгу: {self.name},"
                  f"{self.surname}, {self.__id_number}")


user_1 = User("Mariya", "Simonenko", 1234589)
user_2 = User("Ivan", "Ivanov", 8944589)
user_3 = User("Olya", "Ignatenko", 2374549)

# Проверка
user_1.take_book(book_1)
user_3.take_book(book_1)
user_1.return_book(book_1)
user_2.reservation_book(book_2)
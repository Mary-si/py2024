"""homework22"""


class Book:
    """Информация о книгах"""

    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_available = True
        self.is_reserved = False

    def take(self):
        """Книга взята"""
        if self.is_available and not self.is_reserved:
            self.is_available = False
            return True
        return False

    def returned(self):
        """Книга возвращена"""
        self.is_available = True
        self.is_reserved = False
        return True

    def reservation(self):
        """Книга забронирована"""
        if self.is_available and not self.is_reserved:
            self.is_reserved = True
            return True
        return False

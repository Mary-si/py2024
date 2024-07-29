"""Импортирование необходимых классов и функций из модулей"""
from .homework11_bank_deposit import Deposit, Bank
from .homework11_library import Book, User

"""Указание, какие символы будут доступны для импорта"""
__all__ = ["Deposit", "Bank", "Book", "User"]

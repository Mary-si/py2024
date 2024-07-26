"""homework22"""

# main.py
from library.book import Book
from library.user import User
from library.deposit import Deposit
from library.bank import Bank


# Создание объектов книг
book_1 = Book("Tree", "Thomas Wyatt", 180, "978-5-06-002611-5")
book_2 = Book("Sea", "William Shakespeare", 230, "978-3-16-148410-0")
book_3 = Book("Cat", "Leo Rangell", 300, "978-6-08-128515-1")

# Создание объектов пользователей
user_1 = User("Mariya", "Simonenko", 1234589)
user_2 = User("Ivan", "Ivanov", 8944589)
user_3 = User("Olya", "Ignatenko", 2374549)

# Проверка функций пользователей с книгами
user_1.take_book(book_1)
user_3.take_book(book_1)
user_1.return_book(book_1)
user_2.reservation_book(book_2)

# Создание объектов депозитов
deposit_1 = Deposit("08.09.2021", "08.09.2025")
deposit_2 = Deposit("02.03.2022", "02.03.2025")
deposit_3 = Deposit("01.01.2025", "31.12.2025")

# Создание объектов банка
bank_user_1 = Bank(20000, 4, 0.05)
bank_user_2 = Bank(5000, 3, 0.03)
bank_user_3 = Bank(2000, 1, 0.01)

# Проверка функции расчета депозита
final_amount_user_1 = bank_user_1.calculate()
print(f"Сумма на счету у пользователя {bank_user_1.deposit_term_year} "
      f"лет, будет {final_amount_user_1:.2f} рублей")

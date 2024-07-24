"""
Этот модуль запускает тесты для bank_deposit и library, и генерирует HTML отчеты.
"""

from pytest import main

if __name__ == "__main__":
    # запуск тестов для bank_deposit и генерация HTML отчета
    main(["tests/test_homework21_bank_deposit_pytest.py",
          "--html=report_test_homework21_bank_deposit_pytest.html"])

    # запуск тестов для library и генерация HTML отчета
    main(["tests/test_homework21_library_pytest.py",
          "--html=report_test_homework21_library_pytest.html"])

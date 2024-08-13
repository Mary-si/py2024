"""homework23"""

# Вам необходимо создать пару контактов, обновить их и удалить через сайт
# https://thinking-tester-contact-list.herokuapp.com/.
# Для этого необходимо пройти все шаги вручную и подобрать все уникальные
# селекторы с которыми вы будите взаимодействовать в процессе работы:
#
# Экран логина:
#
# Ввод имени пользователя
# Ввод пароля
# Нажате кнопки 'Login'
# Добавить новый контакт:
#
# Нажать на кнопку "Add a New Contact": ..
# и тд.
#
# Результатом Вашей работы должны быть детальные шаги(инструкция) по добавлению,
# обновлению и удалению контактов. Оформите их в файле и сделайте PR.
#
# Прмерная структура:
#
# homework23/
# -- test_contactlist.py


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time

link = "https://thinking-tester-contact-list.herokuapp.com/"
browser = webdriver.Chrome()
browser.get(link)


def test_sign_up():
    """зарегистрироваться"""
    browser.find_element(By.ID, "signup").click()
    time.sleep(5)
    browser.find_element(By.ID, "firstName").send_keys("Mariya")
    browser.find_element(By.ID, "lastName").send_keys("Simonenko")
    browser.find_element(By.ID, "email").send_keys("by.zorina08@gmail.com")
    browser.find_element(By.ID, "password").send_keys("doNciqsubmit")
    browser.find_element(By.ID, "submit").click()

    browser.quit()


def test_log_in():
    """войти в аккаунт"""
    browser.find_element(By.ID, "email").send_keys("by.zorina08@gmail.com")
    browser.find_element(By.ID, "password").send_keys("doNciqsubmit")
    browser.find_element(By.ID, "submit").click()
    time.sleep(5)

    browser.quit()


def test_add_new_contact():
    """заполнить только формы со * - обязательные"""
    browser.find_element(By.ID, "add-contact").click()
    time.sleep(5)
    browser.find_element(By.ID, "firstName").send_keys("Gleb")
    browser.find_element(By.ID, "lastName").send_keys("Simonenko")
    browser.find_element(By.ID, "submit").click()

    browser.quit()


def test_edit_contact_1():
    """редактировать контакт без добавления новых данных, просто вернуться назад"""
    browser.save_screenshot("1.png")  # у кнопки с именем пользователя нет ID
    browser.find_element(By.ID, "Gleb Simonenko").click()
    time.sleep(5)
    browser.find_element(By.ID, "edit-contact").click()
    time.sleep(5)
    browser.find_element(By.ID, "cancel").click()
    time.sleep(5)
    browser.find_element(By.ID, "return").click()
    time.sleep(5)

    browser.quit()


def test_edit_contact_2():
    """редактировать контакт с добавлением новых данных, город"""
    browser.save_screenshot("1.png")  # у кнопки с именем пользователя нет ID
    browser.find_element(By.ID, "Gleb Simonenko").click()
    time.sleep(5)
    browser.find_element(By.ID, "edit-contact").click()
    time.sleep(5)
    browser.find_element(By.ID, "city").send_keys("Minsk")
    browser.find_element(By.ID, "submit").click()
    time.sleep(5)
    browser.find_element(By.ID, "return").click()
    time.sleep(5)

    browser.quit()


def test_delete_contact():
    """удалить контакт"""
    browser.find_element(By.ID, "Gleb Simonenko").click()
    time.sleep(5)
    browser.find_element(By.ID, "delete").click()
    time.sleep(5)

    # переключаемся на диалоговое окно подтверждения
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert_text = alert.text

    # Проверяем, что текст соответствует ожиданиям
    assert alert_text == "Are you sure you want to delete this contact?", \
        f"Unexpected alert text: {alert_text}"

    # подтверждаем удаление
    alert.accept()

    time.sleep(5)

    browser.quit()


test_sign_up()

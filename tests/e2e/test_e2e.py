import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Данные для логина
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_end_to_end(driver):
    # Создание объектов страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Открытие страницы логина и авторизация
    login_page.get_login_page()
    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login()

    # Проверка успешного входа
    login_page.verify_login_success()

    # Добавление товара в корзину
    inventory_page.add_to_backpack_cart()

    # Проверка, что товар добавлен в корзину
    assert inventory_page.cart_count() == "1"

    # Завершение оформления заказа
    inventory_page.complete_checkout("Vitaliy", "Popkov", "220085")

    # Проверка, что сообщение о завершении заказа отображается
    inventory_page.verify_thank_you_message()
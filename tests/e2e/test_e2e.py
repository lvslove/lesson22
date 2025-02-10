import pytest
from selenium.webdriver.common.by import By
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
    app_logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert "Swag Labs" in app_logo.text

    #Добавление товара в корзину
    inventory_page.add_to_backpack_cart()

    # Проверка, что товар добавлен в корзину
    assert inventory_page.cart_count() == "1"

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Начало оформления
    driver.find_element(By.CLASS_NAME, "checkout_button").click()

    # Заполнение данных для оформления
    driver.find_element(By.ID, "first-name").send_keys("Vitaliy")
    driver.find_element(By.ID, "last-name").send_keys("Popkov")
    driver.find_element(By.ID, "postal-code").send_keys("220085")
    driver.find_element(By.ID, "continue").click()

    # Завершение оформления
    driver.find_element(By.ID, "finish").click()


    # Проверка, что сообщение о завершении заказа  отображается
    thank_you_message = driver.find_element(By.ID, "checkout_complete_container")
    assert "Thank you for your order!" in thank_you_message.text
import pytest
from lesson22.pages.login_page import LoginPage
from lesson22.pages.inventory_page import InventoryPage


def test_valid_inventory(driver):
    login_page = LoginPage(driver)
    login_page.valid_login()
    inventory_page = InventoryPage(driver)

    assert "inventory" in driver.current_url, "Ошибка: логин не удался"

    inventory_page.move_to_cart()

    assert "cart" in driver.current_url, "Ошибка: не совершён переход в корзину"

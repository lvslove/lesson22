import pytest
from lesson22.pages.login_page import LoginPage
from lesson22.pages.inventory_page import InventoryPage


def test_valid_inventory(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login()

    assert "inventory" in driver.current_url, "Ошибка: логин не удался"
    inventory_page.click_on_backpack_btn()
    inventory_page.click_on_tshirt_btn()
    inventory_page.click_on_cart_icon()

    assert "cart" in driver.current_url, "Ошибка: не совершён переход в корзину"

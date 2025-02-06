import pytest

from lesson22.pages.login_page import LoginPage
from lesson22.pages.inventory_page import InventoryPage
from lesson22.pages.cart_page import CartPage

def test_cart_with_items(driver):
    login_page = LoginPage(driver)
    login_page.valid_login()
    inventory_page = InventoryPage(driver)

    assert "inventory" in driver.current_url, "Ошибка: логин не удался"

    inventory_page.move_to_cart()

    assert "cart" in driver.current_url, "Ошибка: не совершён переход в корзину"

    cart_with_items = CartPage(driver)
    assert cart_with_items.count_products_in_basket() == 1
    assert cart_with_items.return_product() == "Sauce Labs Backpack"

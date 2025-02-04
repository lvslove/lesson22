import pytest

from pages.login_page import LoginPage

from pages.inventory_page import InventoryPage

@pytest.mark.parametrize(
    ("username", "password"), [
        ('standard_user', 'secret_sauce'),
        # ('locked_out_user', 'secret_sauce'),
        # ('problem_user', 'secret_sauce'),
        # ('performance_glitch_user', 'secret_sauce'),
    ]
)

def test_add_to_cart(driver, username, password):
    login_page = LoginPage(driver)
    login_page.get_login_page()
    login_page.valid_login(username, password)
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_backpack_cart()
    assert inventory_page.cart_count() == "1", "Товар не добавлен в корзину"


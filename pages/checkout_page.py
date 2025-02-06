from selenium.webdriver.common.by import By
from lesson22.pages.base_page import BasePage
from lesson22.pages.inventory_page import InventoryPage

class CheckoutPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")

    def items_checkout(self):
        self.click_element(self.CHECKOUT_BTN)


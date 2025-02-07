from selenium.webdriver.common.by import By
from lesson22.pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")


    def items_checkout(self):
        self.click_element(self.CHECKOUT_BTN)


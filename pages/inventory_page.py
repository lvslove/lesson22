from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    THANK_YOU_MESSAGE = (By.ID, "checkout_complete_container")

    def add_to_backpack_cart(self):
        self.click_element(self.BACKPACK)

    def cart_count(self):
        return self.find_element(self.CART_BADGE).text

    def verify_thank_you_message(self):
        thank_you_message = self.find_element(self.THANK_YOU_MESSAGE)
        assert "Thank you for your order!" in thank_you_message.text, "Message not found!"

    def complete_checkout(self, first_name, last_name, postal_code):
        self.click_element((By.CLASS_NAME, "shopping_cart_link"))
        self.click_element((By.CLASS_NAME, "checkout_button"))
        self.enter_text((By.ID, "first-name"), first_name)
        self.enter_text((By.ID, "last-name"), last_name)
        self.enter_text((By.ID, "postal-code"), postal_code)
        self.click_element((By.ID, "continue"))
        self.click_element((By.ID, "finish"))
     
        
    
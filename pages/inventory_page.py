from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_to_backpack_cart(self):
        self.click_element(self.BACKPACK)

    def cart_count(self):
        return self.find_element(self.CART_BADGE).text
     
        
    
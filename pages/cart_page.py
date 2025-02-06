from selenium.webdriver.common.by import By
from lesson22.pages.base_page import BasePage


class CartPage(BasePage):
    BACKPACK_LINE = (By.ID, "remove-sauce-labs-backpack")
    TSHIRT_LINE = (By.ID, "remove-sauce-labs-bolt-t-shirt")

    def remove_backpack_line(self):
        self.click_element(self. BACKPACK_LINE)

    def remove_tshirt_line(self):
        self.click_element(self. TSHIRT_LINE)
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.wait import wait_clickable, wait_visible

class ProductPage(BasePage):
    ADD_TO_CART_ANY = (By.CSS_SELECTOR, "button[id^='add-to-cart-button-']")
    CART_HEADER_LINK = (By.CSS_SELECTOR, "a.ico-cart")

    def wait_loaded(self):
        wait_visible(self.driver, self.ADD_TO_CART_ANY, timeout=15)
        return self
    
    def add_to_cart(self):
        btn = wait_clickable(self.driver, self.ADD_TO_CART_ANY, timeout=15)
        btn.click()
        return self

    def go_to_cart_from_header(self):
        link = wait_clickable(self.driver, self.CART_HEADER_LINK, timeout=15)
        link.click()
        return self
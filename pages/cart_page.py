from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.wait import wait_clickable, wait_visible, wait_url_contains

class CartPage(BasePage):
    PATH = "/cart"

    CART_TABLE = (By.CSS_SELECTOR, "table.cart")
    CART_ROWS = (By.CSS_SELECTOR, "table.cart tbody tr")
    TERMS = (By.ID, "termsofservice")
    CHECKOUT = (By.ID, "checkout")

    def wait_loaded(self):
        wait_visible(self.driver, self.CART_TABLE, timeout=15)
        return self
    
    def item_count(self) -> int:
        rows = self.driver.find_elements(*self.CART_ROWS)
        return len(rows)
    
    def proceed_to_checkout(self):
        terms = self.driver.find_elements(*self.TERMS)
        if terms and not terms[0].is_selected():
            terms[0].click()
        
        wait_clickable(self.driver, self.CHECKOUT, timeout=15).click()
        wait_url_contains(self.driver, "/checkout", timeout=15)
        return self
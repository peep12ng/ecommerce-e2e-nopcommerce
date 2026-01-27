from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait import wait_visible, wait_clickable

class SauceDemoCartPage(BasePage):
    CART_LIST = (By.CSS_SELECTOR, "div.cart_list")
    CART_ITEMS = (By.CSS_SELECTOR, "div.cart_item")
    CHECKOUT = (By.CSS_SELECTOR, "#checkout")

    def wait_loaded(self):
        wait_visible(self.driver, self.CART_LIST, timeout=15)
        return self
    
    def item_count(self) -> int:
        return len(self.driver.find_elements(*self.CART_ITEMS))
    
    def proceed_to_checkout(self):
        wait_clickable(self.driver, self.CHECKOUT, timeout=15).click()
        return self
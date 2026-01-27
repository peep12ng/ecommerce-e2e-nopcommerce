from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait import wait_visible, wait_clickable

class SauceDemoInventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.CSS_SELECTOR, ".inventory_container")
    CART_LINK = (By.CSS_SELECTOR, "a.shopping_cart_link")
    ADD_BACKPACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")

    def wait_loaded(self):
        wait_visible(self.driver, self.INVENTORY_CONTAINER, timeout=15)
        return self
    
    def add_backpack_to_cart(self):
        wait_clickable(self.driver, self.ADD_BACKPACK, timeout=15).click()
        return self
    
    def go_to_cart(self):
        wait_clickable(self.driver, self.CART_LINK, timeout=15).click()
        return self
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait import wait_visible, wait_clickable

class OpenCartProductPage(BasePage):
    ADD_TO_CART = (By.ID, "button-cart")
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert.alert-success")
    CART_DROPDOWN = (By.ID, "header-cart")
    VIEW_CART = (By.XPATH, "//a[contains(@href, 'route=checkout/cart')]")

    def wait_loaded(self):
        wait_visible(self.driver, self.ADD_TO_CART, timeout=15)
        return self
    
    def add_to_cart(self):
        wait_clickable(self.driver, self.ADD_TO_CART, timeout=15).click()
        wait_visible(self.driver, self.SUCCESS_ALERT, timeout=15)
        return self
    
    def go_to_cart(self):
        wait_clickable(self.driver, self.CART_DROPDOWN, timeout=15).click()
        wait_clickable(self.driver, self.VIEW_CART, timeout=15).click()
        return self
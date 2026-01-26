from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait import wait_visible, wait_clickable, wait_url_contains

class OpenCartCartPage(BasePage):
    CART_TABLE = (By.CSS_SELECTOR, "div.table-responsive")
    CART_ROWS = (By.CSS_SELECTOR, "div.table-responsive table tbody tr")
    CHECKOUT = (By.XPATH, "//a[contains(@href, 'route=checkout/checkout')]")

    def wait_loaded(self):
        wait_visible(self.driver, self.CART_TABLE, timeout=15)
        return self
    
    def item_count(self) -> int:
        return len(self.driver.find_elements(*self.CART_ROWS))
    
    def proceed_to_checkout(self):
        wait_clickable(self.driver, self.CHECKOUT, timeout=15).click()
        wait_url_contains(self.driver, "route=checkout/checkout", timeout=15)
        return self
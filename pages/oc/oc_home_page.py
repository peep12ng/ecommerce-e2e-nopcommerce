from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait import wait_visible, wait_clickable

class OpenCartHomePage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")

    def open(self):
        super().open("/")
        wait_visible(self.driver, self.SEARCH_INPUT, timeout=15)
        return self
    
    def search(self, keyword: str):
        box = wait_visible(self.driver, self.SEARCH_INPUT, timeout=15)
        box.clear()
        box.send_keys(keyword)
        wait_clickable(self.driver, self.SEARCH_BUTTON, timeout=15).click()
        return self
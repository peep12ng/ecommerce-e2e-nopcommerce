from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait import wait_visible

class SauceDemoCheckoutStepOnePage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")

    def assert_loaded(self):
        wait_visible(self.driver, self.FIRST_NAME, timeout=15)
        wait_visible(self.driver, self.LAST_NAME, timeout=15)
        wait_visible(self.driver, self.POSTAL_CODE, timeout=15)
        return self
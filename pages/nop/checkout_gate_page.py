from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.wait import wait_visible

class CheckoutGatePage(BasePage):
    CHECKOUT_AS_GUEST_BTN = (By.XPATH, "//button[contains(normalize-space(.), 'Checkout as Guest')]")
    PAGE_TITLE = (By.CSS_SELECTOR, "div.page-title h1")

    def assert_loaded(self):
        wait_visible(self.driver, self.PAGE_TITLE, timeout=15)
        wait_visible(self.driver, self.CHECKOUT_AS_GUEST_BTN, timeout=15)
        return self
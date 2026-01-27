from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait import wait_visible, wait_clickable

class SauceDemoLoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")

    def open(self):
        super().open("/")
        wait_visible(self.driver, self.LOGIN_BTN, timeout=15)
        return self
    
    def login(self, username: str, password: str):
        wait_visible(self.driver, self.USERNAME, timeout=15).clear()
        wait_visible(self.driver, self.USERNAME, timeout=15).send_keys(username)    

        wait_visible(self.driver, self.PASSWORD, timeout=15).clear()
        wait_visible(self.driver, self.PASSWORD, timeout=15).send_keys(password)

        wait_clickable(self.driver, self.LOGIN_BTN, timeout=15).click()
        return self
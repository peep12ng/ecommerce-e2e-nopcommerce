from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.wait import wait_clickable, wait_visible

class DesktopsPage(BasePage):
    PATH = "/desktops"

    PRODUCT_TITLE_LINK = (By.CSS_SELECTOR, "h2.product-title a")

    def open(self):
        super().open(self.PATH)
        wait_visible(self.driver, self.PRODUCT_TITLE_LINK, timeout=15)
        return self
    
    def open_product_by_name(self, name: str):
        links = self.driver.find_elements(*self.PRODUCT_TITLE_LINK)
        for a  in links:
            if (a.text or "").strip() == name:
                a.click()
                return
        
        raise AssertionError(f"Product link not found on Desktops page: {name!r}")
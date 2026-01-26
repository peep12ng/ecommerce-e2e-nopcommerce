from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait import wait_visible, wait_clickable

class OpenCartSearchResultsPage(BasePage):
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product-thumb h4 a")

    def wait_loaded(self):
        wait_visible(self.driver, self.PRODUCT_TITLE, timeout=15)
        return self
    
    def open_product_by_name(self, name: str):
        links = self.driver.find_elements(*self.PRODUCT_TITLE)
        for a in links:
            if (a.text or "").strip() == name:
                a.click()
                return
            
        raise AssertionError(f"Product not found in search results: {name!r}")
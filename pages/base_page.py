from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip("/")

    def open(self, path: str = "/"):
        url = f"{self.base_url}{path}"
        self.driver.get(url)
        return self
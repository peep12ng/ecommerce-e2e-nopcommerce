from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver

        if hasattr(base_url, "base_url"):
            base_url = base_url.base_url
        
        if not isinstance(base_url, str):
            raise TypeError(f"base_url must be str, got {type(base_url).__name__}")

        self.base_url = base_url.rstrip("/")

    def open(self, path: str = "/"):
        self.driver.get(f"{self.base_url}{path}")
        return self
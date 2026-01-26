from __future__ import annotations

from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@dataclass(frozen=True)
class DriverOptions:
    headless: bool = False
    window_size: str = "1400, 900"

def create_chrome_driver(opts: DriverOptions) -> webdriver.Chrome:
    chrome_options = ChromeOptions()

    if opts.headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
    
    chrome_options.add_argument(f"--window-size={opts.window_size}")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
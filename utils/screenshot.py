from __future__ import annotations

import os
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver

def save_screenshot(driver: WebDriver, dir_path: str, name_prefix: str) -> str:
    os.makedirs(dir_path, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(dir_path, f"{name_prefix}_{ts}.png")
    driver.save_screenshot(path)
    return path
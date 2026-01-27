import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import SETTINGS

@pytest.mark.legacy
def test_smk_00_open_home(driver):
    driver.get(SETTINGS.base_url)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )

    assert "잠시" not in (driver.title or "")
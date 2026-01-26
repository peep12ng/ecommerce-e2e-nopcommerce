import pytest
from utils.config import SETTINGS
from utils.screenshot import save_screenshot

@pytest.mark.smoke
def test_smk_00_open_home(driver):
    driver.get(SETTINGS.base_url)
    assert "nopcommerce demo store" in driver.title.lower()

    save_screenshot(driver, SETTINGS.screenshots_dir, "smk_00_home")
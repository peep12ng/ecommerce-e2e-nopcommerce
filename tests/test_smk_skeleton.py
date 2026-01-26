import pytest
from utils.config import Settings
from utils.screenshot import save_screenshot

@pytest.mark.smoke
def test_smk_00_open_home(driver):
    driver.get(Settings().base_url)
    assert "nopcommerce demo store" in driver.title.lower()

    save_screenshot(driver, Settings.screenshots_dir, "smk_00_home")
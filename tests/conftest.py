import os
import sys
import pytest

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from utils.driver_factory import create_chrome_driver, DriverOptions
from utils.config import SETTINGS
from utils.screenshot import save_screenshot

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run Chrome in headless mode")

@pytest.fixture
def driver(request):
    headless = bool(request.config.getoption("--headless"))
    drv = create_chrome_driver(DriverOptions(headless=headless))
    drv.implicitly_wait(0)
    yield drv
    drv.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        drv = item.funcargs.get("driver")
        if drv:
            test_name = item.name.replace("/", "_").replace("\\", "_")
            path = save_screenshot(drv, SETTINGS.screenshots_dir, f"FAIL_{test_name}")
            rep.extra = getattr(rep, "extra", [])
            rep.extra.append(f"Screenshot saved to {os.path.abspath(path)}")
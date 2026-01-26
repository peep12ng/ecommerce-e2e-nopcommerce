import os
import sys
import pytest

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from utils.driver_factory import create_chrome_driver, DriverOptions

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run Chrome in headless mode")

@pytest.fixture
def driver(request):
    headless = bool(request.config.getoption("--headless"))
    drv = create_chrome_driver(DriverOptions(headless=headless))
    drv.implicitly_wait(0)
    yield drv
    drv.quit()

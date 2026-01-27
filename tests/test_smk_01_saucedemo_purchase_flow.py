import pytest
from utils.config import SETTINGS

from pages.sd.sd_login_page import SauceDemoLoginPage
from pages.sd.sd_inventory_page import SauceDemoInventoryPage
from pages.sd.sd_cart_page import SauceDemoCartPage
from pages.sd.sd_checkout_step_one_page import SauceDemoCheckoutStepOnePage

@pytest.mark.smoke
def test_smk_01_saucedemo_purchase_flow_to_checkout_step_one(driver):
    SauceDemoLoginPage(driver, SETTINGS.base_url).open().login(
        username="standard_user",
        password="secret_sauce",
    )

    SauceDemoInventoryPage(driver, SETTINGS.base_url).wait_loaded() \
    .add_backpack_to_cart() \
    .go_to_cart()

    cart = SauceDemoCartPage(driver, SETTINGS.base_url).wait_loaded()
    assert cart.item_count() >= 1, "Cart should have at least 1 item"
    cart.proceed_to_checkout()

    SauceDemoCheckoutStepOnePage(driver, SETTINGS.base_url).assert_loaded()
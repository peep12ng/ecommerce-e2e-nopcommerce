import pytest

from utils.config import SETTINGS
from pages.nop.desktops_page import DesktopsPage
from pages.nop.product_page import ProductPage
from pages.nop.cart_page import CartPage
from pages.nop.checkout_gate_page import CheckoutGatePage

@pytest.mark.legacy
def test_smk_01_purchase_flow_to_checkout_gate(driver):
    desktops = DesktopsPage(driver, SETTINGS.base_url).open()

    desktops.open_product_by_name("Lenovo IdeaCentre")

    ProductPage(driver, SETTINGS.base_url).wait_loaded().add_to_cart()
    ProductPage(driver, SETTINGS.base_url).go_to_cart_from_header()

    cart = CartPage(driver, SETTINGS.base_url).wait_loaded()
    assert cart.item_count() >= 1, "Cart should have at least 1 item"

    cart.proceed_to_checkout()

    CheckoutGatePage(driver, SETTINGS.base_url).assert_loaded()
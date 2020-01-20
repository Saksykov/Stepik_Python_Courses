import pytest
from .pages.product_page import ProductPage


promo_parts = ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5",
               "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"]


@pytest.mark.parametrize("link_parts", promo_parts)
def test_guest_can_add_product_to_basket(browser, link_parts):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link_parts}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()

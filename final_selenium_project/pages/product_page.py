import re
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_button_add_to_basket()
        self.add_product_to_basket()
        self.should_be_price()
        self.find_product_price_value()
        self.should_be_product_name()
        self.find_product_name()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "button add_to_basket not found"

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_VALUE), "price not found"

    def find_product_price_value(self):
        price_value = self.browser.find_element(*ProductPageLocators.PRICE_VALUE)
        price_str = re.findall(r"[0-9,]+", price_value.text)[0]
        price = float(re.sub(r",", r".", price_str))
        assert price > 0, "price is wrong"
        return price

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "product name not found"

    def find_product_name(self):
        name_value = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = name_value.text
        breadcrumb_value = self.browser.find_element(*ProductPageLocators.BREADCRUMB_PRODUCT_NAME)
        breadcrumb_name = breadcrumb_value.text
        assert product_name == breadcrumb_name, "product name is wrong"
        return product_name


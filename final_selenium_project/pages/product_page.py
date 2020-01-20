from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "button add_to_basket not found"

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()

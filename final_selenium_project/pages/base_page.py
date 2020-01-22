import math
import re

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators, BasketPageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "login link not present"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self):
        button_go_basket = self.browser.find_element(*BasePageLocators.BUTTON_VIEW_BASKET)
        button_go_basket.click()

    def should_be_basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_IS_EMPTY), "basket is not empty TEXT"

    def should_be_basket_is_empty_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "basket is not empty PRODUCT"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def find_flout_value_in_element(self, how, what):
        value_element = self.browser.find_element(how, what)
        value_str = re.findall(r"[0-9]+", value_element.text)
        value = float(".".join(value_str))
        return value

    def find_text_value(self, how, what):
        text_value = self.browser.find_element(how, what)
        text = text_value.text
        return text

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

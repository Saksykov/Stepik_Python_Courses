from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_VALUE = (By.CSS_SELECTOR, "div.row p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.row div.product_main h1")
    BREADCRUMB_PRODUCT_NAME = (By.CSS_SELECTOR, "ul.breadcrumb li.active")

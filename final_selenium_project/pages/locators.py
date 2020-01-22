from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")


class BasketPageLocators:
    TEXT_IS_EMPTY = (By.CSS_SELECTOR, "div#content_inner>p")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div.basket-items")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_VALUE = (By.CSS_SELECTOR, "div.row p.price_color")
    PRICE_BASKET_VALUE = (By.CSS_SELECTOR, "div.basket-mini")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.row div.product_main h1")
    BREADCRUMB_PRODUCT_NAME = (By.CSS_SELECTOR, "ul.breadcrumb li.active")
    ALERTINNER_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner")

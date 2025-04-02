from selenium.webdriver.common.by import By


class BasePageLocators():
    CATALOG = (By.CSS_SELECTOR, "#catalogDropdown button")
    SMARTFONY = (By.CSS_SELECTOR, '.btn-group-vertical a[href="/catalog/smartfony"]')


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_submit")

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")  # кнопка добавить товар в корзину
    PRODUCT_IN_CART = (By.CSS_SELECTOR, "#messages .in:nth-child(1) .alertinner strong")  # имя продукта в корзине
    VALUE_IN_CART = (By.CSS_SELECTOR, "#messages .in:nth-child(3) .alertinner strong")  # цена продукта в корзине
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")  # имя продукта на странице
    PRODUCT_VALUE = (By.CSS_SELECTOR, ".product_main .price_color")  # цена продукта на странице
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .in:nth-child(1) .alertinner")  # сообщение об успешном добавлении товара в корзину


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")

from selenium.webdriver.common.by import By


class BasePageLocators():
    CATALOG = (By.CSS_SELECTOR, "#catalogDropdown button")
    SMARTFONY = (By.CSS_SELECTOR, '.btn-group-vertical a[href="/catalog/smartfony"]')
    APPLE = (By.CSS_SELECTOR, '.sub.pe-0 a[href="/catalog/smartfony/smartfony-apple"]')


class MainPageLocators():
    pass


class ProductsPageLocators():
    SORT_BY_PRODUCT = (By.CSS_SELECTOR, ".sort-by-cover.link-alt .dropdown-toggle")
    SORT_BY_DEFAULT = (By.CSS_SELECTOR, ".sort-by-cover.link-alt .border-bottom:nth-child(1)")
    SORT_BY_INCREASE = (By.CSS_SELECTOR, ".sort-by-cover.link-alt .border-bottom:nth-child(2)")
    SORT_BY_DECREASE = (By.CSS_SELECTOR, ".sort-by-cover.link-alt .border-bottom:nth-child(3)")
    PRICE_PRODUCTS_IN_PAGE = (By.CSS_SELECTOR, ".px-md-1 .product-price.font-adaptive .current-price span:nth-child(1)")

from selenium.webdriver.common.by import By


class BasePageLocators:
    CATALOG = (By.CSS_SELECTOR, "#catalogDropdown button")
    SMARTFONY = (By.CSS_SELECTOR, '.btn-group-vertical a[href="/catalog/smartfony"]')
    APPLE = (By.CSS_SELECTOR, '.sub.pe-0 a[href="/catalog/smartfony/smartfony-apple"]')
    BUTTON_CART = (By.XPATH, "//div[@class='d-none d-lg-block']//a[@href='/cart' and contains(@class, 'btn-cart')]")


class MainPageLocators:
    pass


class ProductsPageLocators:
    SORT_BY_PRODUCT = (By.CSS_SELECTOR, ".sort-by-cover.link-alt .dropdown-toggle")
    SORT_BY_DEFAULT = (By.CSS_SELECTOR, ".sort-by-cover.link-alt .border-bottom:nth-child(1)")
    SORT_BY_INCREASE = (By.CSS_SELECTOR, ".sort-by-cover.link-alt .border-bottom:nth-child(2)")
    SORT_BY_DECREASE = (By.CSS_SELECTOR, ".sort-by-cover.link-alt .border-bottom:nth-child(3)")
    PRICE_PRODUCT_IN_PAGE = (By.CSS_SELECTOR, ".px-md-1 .product-price.font-adaptive .current-price span:nth-child(1)")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".px-md-1 .cart-button.w-100 button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".px-md-1 .product-name.font-adaptive a")


class CartPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "tr .product-name .product-name a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "tr .price span span")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, "tr .text-center .product-counter .qty-val")
    BUTTON_DOWN = (By.CSS_SELECTOR, "tr .text-center .product-counter .down")
    BUTTON_UP = (By.CSS_SELECTOR, "tr .text-center .product-counter .up")
    PRODUCT_TOTAL_PRICE = (By.CSS_SELECTOR, ".d-md-block tr .text-center span span:nth-child(1)")
    BUTTON_DELETE = (By.CSS_SELECTOR, "tr .action a.icon-link")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".w-100.d-inline-flex.justify-content-between.align-items-center .text-primary span")

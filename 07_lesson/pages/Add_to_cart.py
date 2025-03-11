from selenium.webdriver.common.by import By

class CartActions:
    def __init__(self, driver):
        self._driver = driver

    def add_products_to_cart(self, products):
        for product in products:
            product_element = self._driver.find_element(By.ID, f"add-to-cart-{product}")
            product_element.click()

from selenium.webdriver.common.by import By

class Cart:
    def __init__(self, driver):
        self._driver = driver

    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    def click_checkout(self):
        self._driver.find_element(By.ID, "checkout").click()

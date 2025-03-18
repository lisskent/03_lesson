from selenium.webdriver.common.by import By

class Checkout:
    def __init__(self, driver):
        self._driver = driver

    def fill_form(self, first_name, last_name, postal_code):
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self._driver.find_element(By.CSS_SELECTOR, ".btn_primary.cart_button").click()

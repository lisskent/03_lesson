import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestShoppingCart:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        yield
        self.driver.quit()

    def test_shopping_cart(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce" + Keys.RETURN)

        products = [
            "sauce-labs-backpack",
            "sauce-labs-bolt-t-shirt",
            "sauce-labs-onesie"
        ]
        for product in products:
            product_element = self.driver.find_element(By.ID, f"add-to-cart-{product}")
            product_element.click()

        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

        self.driver.find_element(By.ID, "checkout").click()

        self.driver.find_element(By.ID, "first-name").send_keys("Даниил")
        self.driver.find_element(By.ID, "last-name").send_keys("Савищенко")
        self.driver.find_element(By.ID, "postal-code").send_keys("101000")

        self.driver.find_element(By.CSS_SELECTOR, ".btn_primary.cart_button").click()

        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text

        assert total_text == "Total: $58.29"

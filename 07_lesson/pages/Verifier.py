from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Verifier:
    def __init__(self, driver):
        self._driver = driver

    def verify_total(self, expected_total):
        total_element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        assert total_text == expected_total

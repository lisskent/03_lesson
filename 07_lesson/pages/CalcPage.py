from selenium.webdriver.common.by import By

class CalcPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay_value):
        delay_input = self._driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay_value)
from selenium.webdriver.common.by import By

class CalcPage:
    """Класс для работы со страницей замедленного калькулятора."""

    def __init__(self, driver):
        """Инициализация страницы калькулятора.

        Args:
            driver: WebDriver объект для управления браузером.
        """
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay_value: str) -> None:
        """Устанавливает значение задержки на калькуляторе.

        Args:
            delay_value (str): Значение задержки в секундах (строка).

        Returns:
            None
        """
        delay_input = self._driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay_value)
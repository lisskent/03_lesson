from selenium.webdriver.common.by import By

class Checkout:
    """Класс для оформления заказа."""

    def __init__(self, driver):
        """Инициализация объекта оформления заказа.

        Args:
            driver: WebDriver объект для управления браузером.
        """
        self._driver = driver

    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Заполняет форму оформления заказа.

        Args:
            first_name (str): Имя покупателя.
            last_name (str): Фамилия покупателя.
            postal_code (str): Почтовый индекс.

        Returns:
            None
        """
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self._driver.find_element(By.CSS_SELECTOR, ".btn_primary.cart_button").click()
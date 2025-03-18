from selenium.webdriver.common.by import By

class Cart:
    """Класс для работы с корзиной."""

    def __init__(self, driver):
        """Инициализация объекта корзины.

        Args:
            driver: WebDriver объект для управления браузером.
        """
        self._driver = driver

    def go_to_cart(self) -> None:
        """Переходит в корзину.

        Returns:
            None
        """
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    def click_checkout(self) -> None:
        """Нажимает кнопку оформления заказа.

        Returns:
            None
        """
        self._driver.find_element(By.ID, "checkout").click()
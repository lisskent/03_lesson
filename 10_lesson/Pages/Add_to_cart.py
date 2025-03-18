from selenium.webdriver.common.by import By

class CartActions:
    """Класс для добавления товаров в корзину."""

    def __init__(self, driver):
        """Инициализация объекта действий с корзиной.

        Args:
            driver: WebDriver объект для управления браузером.
        """
        self._driver = driver

    def add_products_to_cart(self, products: list[str]) -> None:
        """Добавляет указанные товары в корзину.

        Args:
            products (list[str]): Список ID товаров для добавления (например, ["sauce-labs-backpack"]).

        Returns:
            None
        """
        for product in products:
            product_element = self._driver.find_element(By.ID, f"add-to-cart-{product}")
            product_element.click()
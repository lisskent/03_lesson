from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcActs:
    """Класс для выполнения действий с калькулятором."""

    def __init__(self, driver):
        """Инициализация объекта действий с калькулятором.

        Args:
            driver: WebDriver объект для управления браузером.
        """
        self._driver = driver

    def press_buttons(self, buttons: list[str]) -> None:
        """Нажимает последовательность кнопок на калькуляторе.

        Args:
            buttons (list[str]): Список кнопок для нажатия (например, ['7', '+', '8', '=']).

        Returns:
            None
        """
        for button in buttons:
            WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))
            ).click()

    def get_result(self) -> str:
        """Получает результат вычисления с экрана калькулятора.

        Returns:
            str: Текст результата с экрана калькулятора.
        """
        WebDriverWait(self._driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        return self._driver.find_element(By.CSS_SELECTOR, ".screen").text
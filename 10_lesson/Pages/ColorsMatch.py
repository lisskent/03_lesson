from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def rgb_to_hex(rgb: str) -> str:
    """Преобразует RGB цвет в HEX формат.

    Args:
        rgb (str): Строка с RGB/RGBA значением цвета (например, 'rgb(15, 81, 50)').

    Returns:
        str: HEX значение цвета (например, '#0f5132').
    """
    rgb = [int(x) for x in rgb.strip().replace('rgba', '').replace('rgb', '').replace('(', '').replace(')', '').split(',')]
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

class ColorsMatch:
    """Класс для проверки соответствия цветов полей формы ожидаемым значениям."""

    def __init__(self, driver):
        """Инициализация объекта проверки цветов.

        Args:
            driver: WebDriver объект для управления браузером.
        """
        self._driver = driver
        self.expected_colors = {
            "first-name": "#0f5132",
            "last-name": "#0f5132",
            "address": "#0f5132",
            "e-mail": "#0f5132",
            "phone": "#0f5132",
            "zip-code": "#842029",
            "city": "#0f5132",
            "country": "#0f5132",
            "job-position": "#0f5132",
            "company": "#0f5132"
        }

    def verify_colors(self) -> None:
        """Проверяет цвета всех полей формы на соответствие ожидаемым.

        Returns:
            None
        """
        for field_name in self.expected_colors.keys():
            field_alert = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.ID, field_name))
            )
            actual_color = field_alert.value_of_css_property('color')

            if actual_color.startswith('rgb'):
                actual_color = rgb_to_hex(actual_color)

            expected_color = self.expected_colors[field_name]
            assert actual_color == expected_color
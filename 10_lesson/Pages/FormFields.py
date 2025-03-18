from selenium.webdriver.common.by import By

class FormFields:
    """Класс для открытия формы и работы с её полями"""

    def __init__(self, driver):
        """Инициализация страницы формы.

        Args:
            driver: WebDriver объект для управления браузером.
        """
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()
        self.fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

    def fill_form(self) -> None:
        """Заполняет поля формы и отправляет её.

        Returns:
            None
        """
        for field_name, value in self.fields.items():
            self._driver.find_element(By.NAME, field_name).send_keys(value)
        self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
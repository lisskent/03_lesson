from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Auth:
    """Класс для авторизации на сайте магазина."""

    def __init__(self, driver):
        """Инициализация страницы авторизации.

        Args:
            driver: WebDriver объект для управления браузером.
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    def login(self, username: str, password: str) -> None:
        """Выполняет вход в систему с указанными логином и паролем.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль пользователя.

        Returns:
            None
        """
        self._driver.find_element(By.ID, "user-name").send_keys(username)
        self._driver.find_element(By.ID, "password").send_keys(password + Keys.RETURN)
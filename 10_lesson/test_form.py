import allure
from selenium import webdriver
from Pages.FormFields import FormFields
from Pages.ColorsMatch import ColorsMatch

@allure.title("Тест отправки формы и проверки цветов полей")
@allure.description("Проверка заполнения формы и соответствия цветов полей ожидаемым значениям")
@allure.feature("Форма данных")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission():
    driver = webdriver.Chrome()
    try:
        with allure.step("Инициализация страницы формы"):
            form_fields = FormFields(driver)
        
        with allure.step("Заполнение и отправка формы"):
            form_fields.fill_form()

        with allure.step("Инициализация проверки цветов"):
            colors_match = ColorsMatch(driver)
        
        with allure.step("Проверка соответствия цветов полей"):
            colors_match.verify_colors()
    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
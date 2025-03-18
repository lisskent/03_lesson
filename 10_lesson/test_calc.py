import allure
from selenium import webdriver
from Pages.CalcPage import CalcPage
from Pages.CalcActs import CalcActs

@allure.title("Тест медленного калькулятора: сложение чисел")
@allure.description("Проверка корректности сложения 7 + 8 = 15 с установленной задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator():
    driver = webdriver.Chrome()
    try:
        with allure.step("Инициализация страницы калькулятора"):
            calculator_page = CalcPage(driver)
        
        with allure.step("Установка задержки в 45 секунд"):
            calculator_page.set_delay("45")

        calculator_actions = CalcActs(driver)
        
        with allure.step("Ввод последовательности кнопок: 7 + 8 ="):
            buttons = ['7', '+', '8', '=']
            calculator_actions.press_buttons(buttons)

        with allure.step("Получение результата вычисления"):
            result = calculator_actions.get_result()

        with allure.step("Проверка результата: ожидаем 15"):
            assert result == "15"
    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
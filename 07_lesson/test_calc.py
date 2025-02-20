from selenium import webdriver
from pages.CalcPage import CalcPage
from pages.CalcActs import CalcActs

def test_calculator():
    driver = webdriver.Chrome()
    try:
        calculator_page = CalcPage(driver)
        calculator_page.set_delay("45")

        calculator_actions = CalcActs(driver)
        buttons = ['7', '+', '8', '=']
        calculator_actions.press_buttons(buttons)

        result = calculator_actions.get_result()
        assert result == "15"
    finally:
        driver.quit()

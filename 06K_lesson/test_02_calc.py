import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    buttons = ['7', '+', '8', '=']
    for button in buttons:
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))
        ).click()

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text

    assert result == "15", f"Expected result to be 15, but got {result}"

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def rgb_to_hex(rgb):
    rgb = [int(x) for x in rgb.strip().replace('rgba', '').replace('rgb', '').replace('(', '').replace(')', '').split(',')]
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


def test_form_submission(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    fields = {
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

    for field_name, value in fields.items():
        driver.find_element(By.NAME, field_name).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    expected_colors = {
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

    for field_name in fields.keys():
        field_alert = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, field_name))
        )
        actual_color = field_alert.value_of_css_property('color')

        if actual_color.startswith('rgb'):
            actual_color = rgb_to_hex(actual_color)

        expected_color = expected_colors[field_name]
        assert actual_color == expected_color

from selenium import webdriver
from pages.FormFields import FormFields
from pages.ColorsMatch import ColorsMatch

def test_form_submission():
    driver = webdriver.Chrome()

    form_fields = FormFields(driver)
    form_fields.fill_form()

    colors_match = ColorsMatch(driver)
    colors_match.verify_colors()

    driver.quit()
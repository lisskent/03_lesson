from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )

    images = driver.find_elements(By.TAG_NAME, "img")

    third_image_src = images[3].get_attribute("src")

    print("Значение атрибута src у 3-й картинки:", third_image_src)


finally:
    driver.quit()

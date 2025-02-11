from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")

time.sleep(20)

close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer p")
close_button.click()

time.sleep(5)

driver.quit()

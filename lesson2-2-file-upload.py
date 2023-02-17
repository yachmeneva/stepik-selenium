import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.NAME, "lastname").send_keys("Ya")
    browser.find_element(By.NAME, "firstname").send_keys("Olga")
    browser.find_element(By.NAME, "email").send_keys("test@test.ru")

    # путь к директории исполняемого(этого) файла
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curr_dir, "cv_file.txt")
    print(file_path)
    browser.find_element(By.ID, "file").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    time.sleep(15)
    browser.quit()
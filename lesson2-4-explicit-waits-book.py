import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    btn_book = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()

    x = int(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(str(calc(x)))
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(15)
    browser.quit()

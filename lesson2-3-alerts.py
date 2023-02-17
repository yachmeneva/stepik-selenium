import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.TAG_NAME, "button").click()

    # переключиться на алерт
    alert = browser.switch_to.alert
    alert.accept()

    x = int(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(str(calc(x)))

    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(15)
    browser.quit()

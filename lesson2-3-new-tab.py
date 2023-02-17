import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.TAG_NAME, "button").click()

    # переключиться на новую вкладку
    tab2_name = browser.window_handles[1]
    tab2 = browser.switch_to.window(tab2_name)

    x = int(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(str(calc(x)))

    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(15)
    browser.quit()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def math_function(x):
    return math.log(abs(12*math.sin(x)))


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = int(browser.find_element(By.ID, "input_value").text)
    res = math_function(x)

    browser.find_element(By.ID, "answer").send_keys(str(res))

    button = browser.find_element(By.TAG_NAME, "button")

    # в метод execute_script мы передали текст js-скрипта и найденный элемент button,
    # к которому нужно будет проскроллить страницу
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # скролл на 100рх вниз
    # browser.execute_script("window.scrollBy(0, 100);")

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    button.click()

finally:
    time.sleep(15)
    browser.quit()

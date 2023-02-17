from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    time.sleep(5)

    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    r = calc(x)

    robot_checked = browser.find_element(By.ID, "robotCheckbox").get_attribute("checked")
    print("value of I'm robot checkbox: ", robot_checked)
    assert robot_checked is None, "I'm robot checkbox is not selected by default"

    browser.find_element(By.ID, "answer").send_keys(r)
    browser.find_element(By.ID, "robotCheckbox").click()
    robot_checked = browser.find_element(By.ID, "robotCheckbox").get_attribute("checked")
    print("value of I'm robot checkbox: ", robot_checked)
    # true с маленькой буквы, т.к. это javascript
    assert robot_checked == "true", "I'm robot checkbox checked is true"

    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, ".btn-default").click()


finally:
    time.sleep(15)
    browser.quit()

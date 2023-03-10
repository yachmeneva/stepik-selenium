from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration():
    def test_registration1(self):
        #
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration1.html")

            # Ваш код, который заполняет обязательные поля
            browser.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Olga")
            browser.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Yachmeneva")
            browser.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("test@test.ru")

            # Отправляем заполненную форму
            browser.find_element(By.CSS_SELECTOR, "button.btn").click()
            time.sleep(1)

            welcome_text = browser.find_element(By.TAG_NAME, "h1").text
            msg_expected = "Congratulations! You have successfully registered!"
            assert welcome_text == msg_expected, "registration1.html: Registration unsuccessful."

        finally:
            browser.quit()

    def test_registration2(self):
        #
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration2.html")

            # Ваш код, который заполняет обязательные поля
            browser.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Olga")
            browser.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Yachmeneva")
            browser.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("test@test.ru")

            # Отправляем заполненную форму
            browser.find_element(By.CSS_SELECTOR, "button.btn").click()
            time.sleep(1)

            welcome_text = browser.find_element(By.TAG_NAME, "h1").text
            msg_expected = "Congratulations! You have successfully registered!"
            assert welcome_text == msg_expected, "registration2.html: Registration unsuccessful."

        finally:
            browser.quit()


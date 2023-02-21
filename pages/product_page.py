import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_btn.click()
        self.solve_quiz_and_get_code()

    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), "Add to cart button is not presented. "

    def should_be_success_add_msg(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print(f"Book name is: {product_name}")
        success_msg = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG).text
        print(f"Success message is: {success_msg}")
        assert product_name in success_msg, "Success added message is not presented. "

    def cart_price_check(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(f"\nProduct price is: {product_price}")
        cart_price = self.browser.find_element(By.CSS_SELECTOR, ".basket-mini").text
        print(f"Cart price is: {cart_price}")
        assert product_price in cart_price, "Basket price isn't correct"

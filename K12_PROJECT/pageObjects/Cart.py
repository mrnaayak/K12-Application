from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
class CartPage:

    price1_xpath="//span[@class='price']//span[@class='price']"
    def __init__(self, driver):
        self.driver = driver
    def get_price_1st_item(self):
        price=self.driver.find_element(By.XPATH, self.price1_xpath)
        return price.text


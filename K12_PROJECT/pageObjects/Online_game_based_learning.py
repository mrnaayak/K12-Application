from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.Cart import CartPage


class OnlineGamebasedLearning:
    radio_button_family_plan_12months_xpath = "//input[@id='bundle-option-2310-3935']"
    add_to_cart_button = "//button[@title='Add to Cart']"
    cart_link_xpath = "//a[@class='mybag-link']"
    popup_xpath = "//div[@class='msg-box']"

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def single_plan_month_month(self):
        pass

    def single_plan_year(self):
        pass

    def family_plan_month_month(self):
        pass

    def family_plan_year(self):
        self.driver.find_element(By.XPATH, self.radio_button_family_plan_12months_xpath).click()

    def add_to_cart_click(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_button).click()

    def popup_wait(self):
        wait = WebDriverWait(self.driver, 10)
        popup = wait.until(EC.visibility_of_element_located((By.XPATH, self.popup_xpath)))
        wait.until_not(EC.visibility_of_element_located((By.XPATH, self.popup_xpath)))
        # self.driver.find_element(By.XPATH, )

    def cart_button_click(self):
        self.driver.find_element(By.XPATH, self.cart_link_xpath).click()
        return CartPage(self.driver)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SubjectArt:
    kindergarden_xpath = "//dd[@class='even']//li[1]//a[1]"
    grade1= "//dd[@class='even']//li[2]//a[1]"
    grade2 = "//dd[@class='even']//li[3]//a[1]"
    grade3 = "//dd[@class='even']//li[4]//a[1]"
    grade4 = "//dd[@class='even']//li[5]//a[1]"
    grade5 = "//dd[@class='even']//li[6]//a[1]"
    grade6 = "//dd[@class='even']//li[7]//a[1]"
    grade7 = "//dd[@class='even']//li[8]//a[1]"
    grade8 = "//dd[@class='even']//li[9]//a[1]"
    books_xpath = "//ol//a[@class='product-image']"

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def kindergarden_click(self):
        self.driver.find_element(By.XPATH, self.kindergarden_xpath).click()
        time.sleep(3)
        products = self.driver.find_elements(By.XPATH, self.books_xpath)
        return products

    def grade1_click(self):
        self.driver.find_element(By.XPATH, self.grade1).click()
        products = self.driver.find_elements(By.XPATH, self.books_xpath)
        return products

    def grade2_click(self):
        self.driver.find_element(By.XPATH, self.grade2).click()
        products = self.driver.find_elements(By.XPATH, self.books_xpath)
        return products

    def grade3_click(self):
        self.driver.find_element(By.XPATH, self.grade3).click()
        products = self.driver.find_elements(By.XPATH, self.books_xpath)
        return products

    def grade4_click(self):
        self.driver.find_element(By.XPATH, self.grade4).click()
        products = self.driver.find_elements(By.XPATH, self.books_xpath)
        return products

    def grade5_click(self):
        self.driver.find_element(By.XPATH, self.grade5).click()
        products = self.driver.find_elements(By.XPATH, self.books_xpath)
        return products

    def grade6_click(self):
        self.driver.find_element(By.XPATH, self.grade6).click()
        products = self.driver.find_elements(By.XPATH, self.books_xpath)
        return products

    def grade7_click(self):
        self.driver.find_element(By.XPATH, self.grade7).click()
        products = self.driver.find_elements(By.XPATH, self.books_xpath)
        return products

    def grade8_click(self):
        self.driver.find_element(By.XPATH, self.grade8).click()
        time.sleep(3)

        products = self.driver.find_elements(By.XPATH, self.books_xpath)
        return products

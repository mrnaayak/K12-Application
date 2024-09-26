import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.home_page import LoginPage
from Utilities.ReadProperties import ReadConfing
from Utilities.customLogger import LogGen
from pageObjects.Cart import CartPage
import logging


class Test_GRADE:
    baseURL = ReadConfing.getApplicationURL()
    username = ReadConfing.getUsername()
    password = ReadConfing.getPassword()
    logger = LogGen.loggen()

    # def test_login(self,setup):
    #     self.driver=setup
    #     self.driver.get(self.baseURL)
    #     #create an object for the class LoginPage which declared in pom_class module
    #     self.lp=LoginPage(self.driver)
    #     self.lp.login_navbar_click()
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    def test_ascending_order_grade(self, setup):

        self.logger.info("#############Testing has started###########")
        self.driver = setup

        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.lp.login_navbar_click()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        grade_object = self.lp.click_grade()

        grade_object.select_price_low_to_high()

        prices_list = grade_object.get_all_prices()

        prices_list_text = []

        for each_product_price in prices_list:
            # price_text = each_product_price.text.strip()

            if each_product_price.text != '':
                prices_list_text.append(each_product_price.text)
        print('prices_list_text', prices_list_text)

        # print('Prices_list_text', prices_list_text)

        grade_object.go_to_2nd_page()

        prices_list2 = grade_object.get_all_prices()
        print('\n\n')

        prices_list_text_2 = []

        for each_product_price in prices_list2:
            if each_product_price.text != '':
                prices_list_text_2.append(each_product_price.text)
        print('prices_list_text', prices_list_text_2)
        # print('Prices_list_text', prices_list_text_2)

        all_prices_text = prices_list_text + prices_list_text_2

        print(all_prices_text)

        all_prices_text_without_dollar = []
        all_prices_text_without_dollar = [float(element.replace('$', '')) for element in all_prices_text]
        # print(all_prices_text_without_dollar)

        assert sorted(
            all_prices_text_without_dollar) == all_prices_text_without_dollar, 'Items not arranged in ascending order'

        time.sleep(10)
        self.logger.info("#############Testing has finished###########")


        self.driver.quit()

import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Subject_Art import SubjectArt
from Utilities.ReadProperties import ReadConfing
from pageObjects.home_page import LoginPage
from selenium.common.exceptions import StaleElementReferenceException
from Utilities.customLogger import LogGen



class Test_subject_art:
    baseURL = ReadConfing.getApplicationURL()
    username = ReadConfing.getUsername()
    password = ReadConfing.getPassword()
    logger = LogGen.loggen()


    def test_art_kindergarden_search(self, setup):
        self.logger.info("#############Testing has started###########")
        books = [' Summit Art Kindergarten',' Summit Art Kindergarten (Independent Study)']
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        subject_art_object = self.lp.click_art()
        products = subject_art_object.kindergarden_click()
        print('hi')
        # print(products)
        time.sleep(3)

        j = 0
        for i in products:
            title1 = i.get_attribute('title')
            print(title1)
            print(books[j])
            if title1 == books[j]:
                print('book verified')
            j = j + 1

        self.driver.quit()
        self.logger.info("#############Testing has started###########")




    def test_art_grade8(self, setup):
        books = ['Summit Intermediate World Art II, Semester 2 (ART08B)', 'Intermediate World Art II Summit (Independent Study)','Summit Intermediate World Art II, Semester 1 (ART08A)']
        self.logger.info("#############Testing has started###########")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        subject_art_object = self.lp.click_art()
        products = subject_art_object.grade8_click()
        j = 0
        for i in products:
            title1 = i.get_attribute('title')
            print(title1)
            print(books[j])
            if title1 == books[j]:
                print('book verified')
            j = j + 1

        self.driver.quit()
        self.logger.info("#############Testing has Finished###########")
    #
#
# def test_art_grade1(self, setup):
#     books = ['Summit Art Kindergarten (Independent Study)', 'Summit Art Kindergarten']
#     self.driver = setup
#     self.driver.get(self.baseURL)
#     self.lp = SubjectArt(self.driver)
#     products = self.lp.grade1_click()
#     j = 0
#     for i in products:
#         title = i.get_attribute('title')
#         if i == books[j]:
#             print('book verified')
#
#     self.driver.quit()
#
#
#
#
#
# def test_art_grade2(self, setup):
#     books = ['Summit Art Kindergarten (Independent Study)', 'Summit Art Kindergarten']
#     self.driver = setup
#     self.driver.get(self.baseURL)
#     self.lp = SubjectArt(self.driver)
#     products = self.lp.grade2_click()
#     j = 0
#     for i in products:
#         title = i.get_attribute('title')
#         if i == books[j]:
#             print('book verified')
#
#     self.driver.quit()
#
#
# def test_art_grade3(self, setup):
#     books = ['Summit Art Kindergarten (Independent Study)', 'Summit Art Kindergarten']
#     self.driver = setup
#     self.driver.get(self.baseURL)
#     self.lp = SubjectArt(self.driver)
#     products = self.lp.grade3_click()
#     j = 0
#     for i in products:
#         title = i.get_attribute('title')
#         if i == books[j]:
#             print('book verified')
#     self.driver.quit()
#
#
# def test_art_grade4(self, setup):
#     books = ['Summit Art Kindergarten (Independent Study)', 'Summit Art Kindergarten']
#     self.driver = setup
#     self.driver.get(self.baseURL)
#     self.lp = SubjectArt(self.driver)
#     products = self.lp.grade4_click()
#     j = 0
#     for i in products:
#         title = i.get_attribute('title')
#         if i == books[j]:
#             print('book verified')
#
#     self.driver.quit()
#
#
# def test_art_grade5(self, setup):
#     books = ['Summit Art Kindergarten (Independent Study)', 'Summit Art Kindergarten']
#     self.driver = setup
#     self.driver.get(self.baseURL)
#     self.lp = SubjectArt(self.driver)
#     products = self.lp.grade5_click()
#     j = 0
#     for i in products:
#         title = i.get_attribute('title')
#         if i == books[j]:
#             print('book verified')
#
#     self.driver.quit()
#
#
# def test_art_grade6(self, setup):
#     books = ['Summit Art Kindergarten (Independent Study)', 'Summit Art Kindergarten']
#     self.driver = setup
#     self.driver.get(self.baseURL)
#     self.lp = SubjectArt(self.driver)
#     products = self.lp.grade6_click()
#     j = 0
#     for i in products:
#         title = i.get_attribute('title')
#         if i == books[j]:
#             print('book verified')
#
#     self.driver.quit()
#
#
# def test_art_grade7(self, setup):
#     books = ['Summit Art Kindergarten (Independent Study)', 'Summit Art Kindergarten']
#     self.driver = setup
#     self.driver.get(self.baseURL)
#     self.lp = SubjectArt(self.driver)
#     products = self.lp.grade7_click()
#     j = 0
#     for i in products:
#         title = i.get_attribute('title')
#         if i == books[j]:
#             print('book verified')
#     self.driver.quit()

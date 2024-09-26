import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.home_page import LoginPage
from Utilities.ReadProperties import ReadConfing
from pageObjects.supplementary_GamebasedLearning import GamebasedLearning
from pageObjects.Online_game_based_learning import OnlineGamebasedLearning
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.customLogger import LogGen


class Test_login:
    baseURL = ReadConfing.getApplicationURL()
    username = ReadConfing.getUsername()
    password = ReadConfing.getPassword()
    logger = LogGen.loggen()

    # def test_login(self,setup):
    #     self.logger.info("#############Testing has started###########")

    #     self.driver=setup
    #     self.driver.get(self.baseURL)
    #     #create an object for the class LoginPage which declared in pom_class module
    #     self.lp=LoginPage(self.driver)
    #     self.lp.login_navbar_click()
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #
    #     time.sleep(5)
    #
    #     name = self.driver.find_element(By.XPATH,"//a[normalize-space()='Harish Naik']")
    #     print(name.text)
    #
    #
    #     assert "Harish Naik" in self.driver.page_source, "Expected 'Welcome' message not found on the page"
    # self.logger.info("#############Testing has started###########")

    #     self.driver.quit()

    # def test_art(self, setup):
    #     self.logger.info("#############Testing has started###########")
    #
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     # create an object for the class LoginPage which declared in pom_class module
    #     self.lp = LoginPage(self.driver)
    #     self.lp.click_art()
    #     assert self.driver.title == 'Online Art Classes, Courses & Curriculum | K12 Store', 'Navigation to Art Page Failed !!!'
    #
    #     self.logger.info("#############Testing has finished###########")

    def test_cart_supplementary_game(self, setup):
        self.logger.info("#############Testing has finished###########")
        self.driver = setup
        self.driver.get(self.baseURL)
        # create an object for the class LoginPage which declared in pom_class module
        self.lp = LoginPage(self.driver)
        self.lp.login_navbar_click()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        game_page = self.lp.click_supplementary_game()
        onlineGameLearningPageObject = game_page.start_now()
        onlineGameLearningPageObject.family_plan_year()
        onlineGameLearningPageObject.add_to_cart_click()
        time.sleep(3)
        onlineGameLearningPageObject.popup_wait()
        cart_page = onlineGameLearningPageObject.cart_button_click()
        price = cart_page.get_price_1st_item()

        print('the price is', price)

        assert price == '$149.95'

        self.driver.quit()

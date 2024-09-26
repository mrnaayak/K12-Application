#pom_class file is the module that consist
#all the posible class and methods related to login page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pageObjects.supplementary_GamebasedLearning import GamebasedLearning
from pageObjects.Grade_PAGE import GradePage
from pageObjects.Subject_Art import SubjectArt

import time
class LoginPage:
    txtbox_username_id="email"
    txtbox_password_id="pass"
    button_xpath="// div[ @class ='push-down-loginbtn'] // button[@ id='send2']"
    show_login_id_xpath="//a[@id='showLogin']"
    subject_xpath="//ul[@class='menu']//a[contains(text(),'Subject')]"
    art_xpath='//a[@href="https://www.k12courses.com/subject/art.html"]/span[text()="Art"]'
    #
    #
    supplementary_xpath="//ul[@class='menu']//a[contains(text(),'Supplementary')]"
    game_xpath="//div[@class='container']//a[@class='level1'][normalize-space()='Game-Based Learning (STRIDE)']"

    grade_xpath="//div[@class='menu-wrapper']//a[text()='Grade']"

    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def login_navbar_click(self):
        self.driver.find_element(By.XPATH,self.show_login_id_xpath).click()
    def setUserName(self,username):
        usernametxt=self.driver.find_element(By.ID,self.txtbox_username_id)
        usernametxt.clear()
        usernametxt.send_keys(username)
    def setPassword(self,pwd):
        passwordtxt=self.driver.find_element(By.ID,self.txtbox_password_id)
        passwordtxt.clear()
        passwordtxt.send_keys(pwd)
    def clickLogin(self):
        # self.driver.implicitly_wait(30)

        # self.driver.find_element(By.ID,self.button_id).click()
        self.driver.find_element(By.XPATH,self.button_xpath).click()

    def click_art(self):
        act=ActionChains(self.driver)
        act_sub=self.driver.find_element(By.XPATH,self.subject_xpath)
        act_art=self.driver.find_element(By.XPATH,self.art_xpath)
        act.move_to_element(act_sub).move_to_element(act_art).click().perform()
        return SubjectArt(self.driver)

    def click_supplementary_game(self):
        act = ActionChains(self.driver)
        act_sub = self.driver.find_element(By.XPATH, self.supplementary_xpath)
        act_game = self.driver.find_element(By.XPATH, self.game_xpath)
        act.move_to_element(act_sub).move_to_element(act_game).click().perform()
        return GamebasedLearning(self.driver)
    def click_grade(self):
        self.driver.find_element(By.XPATH,self.grade_xpath).click()
        return GradePage(self.driver)





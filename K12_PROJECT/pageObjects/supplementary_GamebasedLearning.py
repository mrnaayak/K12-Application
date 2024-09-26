from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Online_game_based_learning import OnlineGamebasedLearning

class GamebasedLearning:
    button_start_now_xpath="//div[@class='lb-cta']//a[@class='btn'][normalize-space()='START NOW']"

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def start_now(self):
        self.driver.find_element(By.XPATH, self.button_start_now_xpath).click()
        return OnlineGamebasedLearning(self.driver)



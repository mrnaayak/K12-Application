import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class GradePage:
    dropdown_xpath = '//*[@id="catalog-listing"]/div/div[1]/div/div[1]/div/select'

    price_label_xpath = "//div[@class='price-box']//span[@class='price']"
    page2_xpath = "//div[1]/div[1]/div[1]/div[2]/div[1]/ol[1]/li[2]/a[1]"

    page3_xpath = "//div[1]/div[1]/div[1]/div[2]/div[1]/ol[1]/li[4]/a[1]"


    def __init__(self, driver):
        self.driver = driver

    def select_price_low_to_high(self):
        wait = WebDriverWait(self.driver, 30)  # Adjust the timeout as needed
        dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, self.dropdown_xpath)))
        options = Select(dropdown)

        # options.select_by_value("https://www.k12courses.com/grades.html?dir=asc&order=price")
        options.select_by_visible_text("Starting Price (Low to High)")
        # options.select_by_index()

        time.sleep(10)

    def get_all_prices(self):
        prices_list = self.driver.find_elements(By.XPATH, self.price_label_xpath)
        time.sleep(2)
        # price = self.driver.find_element(By.XPATH, self.price1_xpath)
        return prices_list



    def go_to_2nd_page(self):
        self.driver.find_element(By.XPATH, self.page2_xpath).click()
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.price_label_xpath)))

        time.sleep(2)


    def go_to_3rd_page(self):
        self.driver.find_element(By.XPATH, self.page3_xpath).click()
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.price_label_xpath)))

        time.sleep(2)

# class SearchResultsPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.product_prices = (By.CLASS_NAME, "product-price")

# def get_product_prices(self):
#     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.product_prices))
#     prices_elements = self.driver.find_elements(*self.product_prices)
#     prices = [float(price.text.strip('$')) for price in prices_elements]
#     return prices
#
# def verify_prices_increasing_order(self, prices):
#     return prices == sorted(prices)


# Example usage
# driver = webdriver.Chrome()
# driver.get("https://www.example.com")
#
# search_page = SearchPage(driver)
# search_page.search_product("Laptops")
#
# results_page = SearchResultsPage(driver)
# product_prices = results_page.get_product_prices()
#
# if results_page.verify_prices_increasing_order(product_prices):
#     print("Prices are listed in increasing order.")
# else:
#     print("Prices are not listed in increasing order.")
#
# driver.quit()

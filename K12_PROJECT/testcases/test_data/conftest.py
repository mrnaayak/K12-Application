import pytest
from selenium import webdriver
@pytest.fixture()
def setup():
    driver=webdriver.Edge("C:\\drivers\\edgedriver_win64\\msedgedriver.exe")
    return driver
from selenium import webdriver
from selenium.webdriver.common.by import By

# ----- abtract class
class web_driver: 

    # numacc: int - numbers of account website
    # driver: webdriver.Edge - webdriver
    def __init__(self, numacc):
        self.numacc = numacc
        self.driver = webdriver.Edge()

    def search (self, link):
        # link: str - link to website
        self.driver.get(link)

# ----- first website: pubiza
class web_driverA (web_driver):

    pass



from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

# ----- abtract class
class web_driver: 

    # numacc: int - numbers of account website
    # driver: webdriver.Edge - webdriver
    # buttonid: List[string] - List of all button's ids
    def __init__(self, numacc, buttonid = []):
        self.numacc = numacc
        self.driver = webdriver.Edge()
        self.buttonid = buttonid

    def search (self, link):
        # link: str - link to website
        self.driver.get(link)

# ----- first website: pubiza.com
class web_driverA (web_driver):
    def surf (self):
        for i in range (1, self.numacc + 1):
            # Each account choose one link
            with open(f"E:\\Business\\src\\pubiza{i}.txt", "r") as file:
                lines = file.read().splitlines()
                link = random.choice(lines)
            self.search (link)
            time.sleep(100)



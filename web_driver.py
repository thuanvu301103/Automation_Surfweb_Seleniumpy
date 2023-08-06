from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# ----- abtract class
class web_driver: 

    # numacc: int - numbers of account website
    # driver: webdriver.Edge - webdriver
    # buttonid: List[string] - List of all button's ids
    def __init__(self, numacc):
        self.numacc = numacc
        self.driver = webdriver.Edge()
        # self.buttonid = buttonid

# ----- first website: pubiza.com
class web_driverA (web_driver):

    def surf (self):
        for i in range (1, self.numacc + 1):
            # need to use thread
            # Each account choose one link
            with open(f"E:\\Business\\src\\pubiza{i}.txt", "r") as file:
                lines = file.read().splitlines()
                link = random.choice(lines)
            self.driver.get(link)
            time.sleep(5) # bypass Google bot test

            # Click button 1: "1/2 Get Link"
            try:
                button1 = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "csubmit")))
                button1.click()
            except: continue
            time.sleep(5) # bypass Google bot test 

            # Click button 2-3: "SIRADAKi"
            try:
                button2 = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, "next-page-link page-link")))
                button2.click()
            except: continue
            time.sleep(5) # bypass Google bot test

            # Click button 2-3: "SIRADAKi": "next-page-link page-link" / "Linke Git": "bb-sticky-el"
            

            time.sleep(100)



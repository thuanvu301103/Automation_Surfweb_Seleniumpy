from function import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import random
import time
from msedge.selenium_tools import Edge, EdgeOptions


# ----- abtract class
class web_driver: 

    # numacc: int - numbers of account website
    # driver: webdriver.Edge - webdriver
    # buttonid: List[string] - List of all button's ids
    def __init__(self, numacc):
        self.numacc = numacc
        
        options = EdgeOptions()
        options.use_chromium = True
        options.add_extension("E:\\Business\\Automation_Surfweb_Seleniumpy\\buster_captcha_solver_for_humans-0.7.2-an+fx.xpi")
        self.driver = Edge(executable_path=r"E:\App setup\MicrosftWebDriver\MicrosoftWebDriver.exe", options = options)

    def setupoptions (self):

    

# ----- first website: pubiza.com
class web_driverA (web_driver):

    def surf (self):
        for i in range (1, self.numacc + 1):
            # need to use thread
            # Each account choose one link
            with open(f"E:\\Business\\src\\pubiza{i}.txt", "r") as file:
                lines = file.read().splitlines()
                link = random.choice(lines)
            try:
                self.driver.get(link)
            except: continue
            time.sleep(15)

            # Click button 1: "1/2 Get Link"
            try:
                button1 = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "csubmit"))).click()
            except: continue
            print ("button 1 click")
             
            # Click button 2-3: "SIRADAKi": "next-page-link page-link" / "Linke Git": "bb-sticky-el"
            button3 = None
            while button3 == None:
                try:
                    button2 = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "next-page-link page-link")))
                except: continue
                try:
                    button3 = self.driver.find_element(By.CLASS_NAME, "next-page-link page-link")
                except: 
                    button2.click()
                    print ("button 2 click")
            button3.click()
            print ("button 3 click")
            time.sleep(1000)

from importmodule import *
from function import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from msedge.selenium_tools import Edge, EdgeOptions


# ----- abtract class
class web_driver: 

    # numacc: int - numbers of account website
    # exepath: string -  webdriver dir
    def __init__(self, numacc, exepath):
        self.numacc = numacc
        self.exepath = exepath

# ----- first website: pubiza.com
class web_driverA (web_driver):

    def surf (self, numacc):

        # Each account choose randomly one link
        with open(f"E:\\Business\\src\\pubiza{numacc}.txt", "r") as file:
            lines = file.read().splitlines()
            link = random.choice(lines)

        # search link
        pyautogui.hotkey('alt', 'd') 
        pyautogui.typewrite(link, interval = 0.05)
        pyautogui.press('enter')
        time.sleep(10)

        # Click button 1: "1/2 GetLink"
        pyautogui.moveTo (970, 577, 2)
        pyautogui.leftClick()
        time.sleep(10)
           
        # Get next link
        pyautogui.hotkey('alt', 'd')
        pyautogui.hotkey('ctrl', 'c')
        link = pyperclip.paste()

        # Close browser 1
        pyautogui.hotkey('ctrl', 'shift', 'w')

        # Search link in webdriver (browser 2)
        driver = Edge(executable_path = self.exepath)
        driver.get (link)
        time.sleep(10)
             
        # Click button 2-3: "SIRADAKi": "next-page-link page-link" / "Linke Git": "bb-sticky-el"
        button3 = None
        while button3 == None:
            button2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "next-page-link page-link")))
            button3 = driver.find_element(By.CLASS_NAME, "next-page-link page-link")
            button2.click()
        else: button3.click()
        # print ("button 3 click")

        # Switch to new tab
        driver.switch_to.window(self.driver.window_handles[1])

        # Click button 4:
        button4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "get_link_btn")))
        button4.click()
        time.sleep(12)

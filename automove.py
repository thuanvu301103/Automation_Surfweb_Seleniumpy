from importmodule import pyautogui
from function import *
from web_driver import *

# ----- move 1: 
def move_1 (i: int):

    # i: int - variaty in each move 
    showwd ("UrbanVPN", 548, 155, 100, 100)

    # Move mouse to choose country
    pyautogui.moveTo (1213, 293 + i*33)
    pyautogui.leftClick()

    # Run VPN (click Run)
    pyautogui.moveTo (797, 533)
    pyautogui.leftClick()
    time.sleep(12)

# ----- no else move for move 1

# ----- Move 2:
def move_2 ():

    web_A = web_driverA(1, "E:\App setup\MicrosftWebDriver\MicrosoftWebDriver.exe")
    web_A.surf()

    # Then need to disable VPN
    showwd ("UrbanVPN", 548, 155, 100, 100)
    pyautogui.moveTo (797, 533)
    pyautogui.leftClick()

# ----- No else move for move 2
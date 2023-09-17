from importmodule import pyautogui, subprocess
from function import *
from web_driver import *

# ----- move 1: 
def move_1 (i: int):

    # i: int - variaty in each move 
    function.showwd ("UrbanVPN", 548, 155, 100, 100)

    # Move mouse to choose country
    pyautogui.moveTo (1213, 293 + (i+1)*33)
    pyautogui.leftClick()

    # Run VPN (click Run)
    pyautogui.moveTo (797, 533)
    pyautogui.leftClick()

    time.sleep(12)

# ----- no else move for move 1

# ----- move 2:
def move_2 ():
    
    # Open browser 1 to avoid recaptcha
    p1 = subprocess.Popen(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])
    p1.wait()
    time.sleep(2)
    showwd ('New tab - Personal - Microsoft\u200b Edge',0,0, 1914, 1011)
    
    # Surf web
    web_A = web_driverA(1, "E:\App setup\MicrosftWebDriver\MicrosoftWebDriver.exe")
    for i in range (1, web_A.numacc + 1):
        try:
            web_A.surf(i)
        except: 
            # Close browser 2
            pyautogui.hotkey('ctrl', 'shift', 'w')
            continue
    
    # Disable VPN
    showwd ("UrbanVPN", 548, 155, 100, 100)
    pyautogui.moveTo (797, 533)
    pyautogui.leftClick()
    
# ----- No else move for move 2
from importmodule import *
import win32gui, win32process, win32con
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options

# ----- for open exe file
def runexe (exedir):
    p = subprocess.Popen([exedir])
    p.wait()

# ----- for make sure window show up on the top
def showwd(name, x, y, cx, cy):
    # name: string - name of the windown
    # x,y: int - position of windown
    # cx, cy: int - size of windown 
    windowList = []
    win32gui.EnumWindows(lambda hwnd, windowList: windowList.append((win32gui.GetWindowText(hwnd),hwnd)), windowList)
    #print (windowList)
    cmdWindow = [i for i in windowList if name in i[0]]
    print (cmdWindow)
    win32gui.SetWindowPos(cmdWindow[0][1],win32con.HWND_TOPMOST,x,y,cx,cy,0)
    # time.sleep(200)

# ----- for bypass captcha : Still waorking
def pass_captcha (browser):
    pass
import win32gui, win32process, win32con

# ----- for make sure window show up on the top
def showwd(name, x, y, cx, cy):
    # name: string - name of the windown
    # x,y: int - position of windown
    # cx, cy: int - sizze of windown 
    windowList = []
    win32gui.EnumWindows(lambda hwnd, windowList: windowList.append((win32gui.GetWindowText(hwnd),hwnd)), windowList)
    # print (windowList)
    cmdWindow = [i for i in windowList if name in i[0]]
    win32gui.SetWindowPos(cmdWindow[0][1],win32con.HWND_TOPMOST,x,y,cx,cy,0)

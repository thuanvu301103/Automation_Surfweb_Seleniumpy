from importmodule import * 
from function import *
from automove import *

# ----- Open exefile: UrbanVPN
p = subprocess.Popen(["C:\\Program Files\\UrbanVPN\\bin\\urbanvpn-gui.exe"])
p.wait()

# ----- Start working with first 15 countries
for i in range(15):
    move_1(i)
    move_2()
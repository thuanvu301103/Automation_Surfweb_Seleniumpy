import subprocess
import time
from function import *
from automove import *


#button = driver.find_element(By.ID, "csubmit")
#button.click()
#time.sleep(100)

### ----- Start automation

# ----- Open Windown: UrbanVPN
p = subprocess.Popen(["C:\\Program Files\\UrbanVPN\\bin\\urbanvpn-gui.exe"])
# Must wait for urbanVPN to open
p.wait()

# ----- Start working with first 15 countries
for i in range(15):
    move_1(i)
    move_2()
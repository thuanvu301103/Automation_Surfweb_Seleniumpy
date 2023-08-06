import time
from web_driver import *


#driver.get("https://linkler.site/2Bnrf")
#button = driver.find_element(By.ID, "csubmit")
#button.click()
#time.sleep(100)

### ----- Start automation

# ----- Open Windown: UrbanVPN
p = subprocess.Popen(["C:\\Program Files\\UrbanVPN\\bin\\urbanvpn-gui.exe"])
# Must wait for urbanVPN to open
p.wait()

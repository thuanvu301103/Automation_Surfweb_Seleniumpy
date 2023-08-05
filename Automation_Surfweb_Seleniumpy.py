from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://linkler.site/2Bnrf")
button = driver.find_element(By.ID, "csubmit")
button.click()
time.sleep(100)
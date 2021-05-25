
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# gives us access to things like the enter key and escape key
from selenium.webdriver.common.keys import Keys

import time

PATH = 'C:\\Users\\samay\\chromedriver.exe'

driver  = webdriver.Chrome(PATH)

driver.get('https://leetcode.com/')
# Page title - duh!
print(driver.title)

driver.quit()

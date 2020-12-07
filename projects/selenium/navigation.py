
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# gives us access to things like the enter key and escape key
from selenium.webdriver.common.keys import Keys

import time

PATH = 'C:\\Users\\samay\\chromedriver.exe'

driver  = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')

link = driver.find_element_by_link_text('Python Programming')
link.click()

try:
    # wait 10 seconds before looking for element                                             Beginner Python Tutorials
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Beginner Python Tutorials')))
    element.clear() # this is to clear send keys so it doesn't append values
    element.click()

    # wait 10 seconds before looking for element
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sow-button-19310003')))
    element.clear()
    element.click()

    #you can also go back, and forward!
    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
except:
	# on error quit
    driver.quit()

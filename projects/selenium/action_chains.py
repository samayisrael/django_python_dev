
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# gives us access to things like the enter key and escape key
from selenium.webdriver.common.keys import Keys

import time

PATH = 'C:\\Users\\samay\\chromedriver.exe'

driver  = webdriver.Chrome(PATH)

driver.get('https://cookie-clicker2.com/cookie-clicker-1')
driver.implicitly_wait(5)

cookie = driver.find_elements_by_class_name('cookies-img')
cookie_count = driver.find_elements_by_class_name('text-point-box')
items = [driver.find_element_by_class_name('blah' + str(i)) for i in range(1, -1, -1)]


actions = ActionChains(driver)
actions.click(cookie) # clicks whereever the mouse happens to be

#note that this doesn't work because they have changed the code so that you can't loop through the options like in the tutorial
for i in range(200):
    actions.perform() # performs the action above.  I could also put a bunch of other code before this
    count = int(cookie_count.text.split(' ')[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element()
            upgrade_actions.click()
            upgrade_actions.perform()
        print(count)

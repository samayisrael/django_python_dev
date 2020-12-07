
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
# Page title - duh!
#print(driver.title)

# get the search box element from the page
search = driver.find_element_by_name('s')

# send some text to that box to search on
search.send_keys('test')

# and send return (enter) to submit the form
search.send_keys(Keys.RETURN)

# Explicit wait for the presence of main on the page
try:
    # wait 10 seconds before looking for element
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main")))

    articles = main.find_elements_by_tag_name('article')

    for article in articles:
        header = article.find_element_by_class_name('entry-summary')
        print(header.text)


except:
    print('nope')
	# else quit
    driver.quit()


# just like it sounds
#print(driver.page_source)

# delay the program so we can see the results before closing
#time.sleep(5)

# Closes current tab, not the entire browser
#driver.close()
# Closes the entire browser (all tabs)
#print('lameo')
driver.quit()

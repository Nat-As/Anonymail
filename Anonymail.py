import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://10minutemail.com/")
#assert "Anonymail" in driver.title
elem = driver.find_element_by_id("get_more_time")

while True:
    time.sleep(540)#Wait 9 minutes, then request more time
    elem.click()
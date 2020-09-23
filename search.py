from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://techwithtim.net")

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(30)

driver.quit()
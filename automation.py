from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://youtube.com')

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='search_query']"))).send_keys("EL47")
driver.find_element_by_xpath("//button[@id='search-icon-legacy']/yt-icon").click()

# searchbox = driver.find_element_by_xpath('//div[@id="search-input"]')
# searchbox.send_keys('EL47')

# searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# searchbutton.click()


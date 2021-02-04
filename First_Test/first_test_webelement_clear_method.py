

from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\gebruiker\\Desktop\\chromedriver")
base_url = "https://clarusway.com/"
driver.get(base_url)
element = driver.find_element_by_link_text("Events")
element.click()
time.sleep(5)

driver.quit()
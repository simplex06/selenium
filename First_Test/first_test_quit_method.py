from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\Users\\gebruiker\\Desktop\\chromedriver")

base_url = "https://clarusway.com"
expected_title = "Online Career IT Training School - Clarusway"
actual_title = ""

driver.get(base_url) 
actual_title = driver.title 
page_source = driver.page_source

print("page_source: \n", page_source)

#if actual_title == expected_title :
#    print("Test Passed")
#else:
#    print("Test Failed")

driver.quit()
# Import necessary library packages for chrome driver
from selenium import webdriver

# Set chrome options for working with headless mode (no screen)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

# create the instance of webdriver with chrome_options
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
        
base_url = "https://clarusway.com/"
expected_title = "Online Career IT Training School - Clarusway"
actual_title = ""

# Request from the chrome-driver to launch Chrome Browser
# And direct it to the base URL
driver.get(base_url)

# get the actual value of the title
actual_title = driver.title

# compare the actual title of the page with the expected one
# Then, print "Test Passed" if equal, print "Test Failed" if not.
if actual_title == expected_title:
    print("Test Passed")
else:
    print("Test Failed")

# Close the chrome-driver
driver.close()
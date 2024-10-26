########## Test Case
# -----------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://opensource-demo.orangehrmlive.com/
# 3) Enter username  (Admin).
# 4) Enter password  (admin123).   
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title) 
# 7) Verify title of the page: OrangeHRM    (Expected)
# 8) close browser
################# Invoking chrome browser - Approach 1 without Service class ##################
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
import time

################# Invoking chrome browser - Approach 2 - with Service class ##################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj=Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"oxd-button").click()
time.sleep(6)
actual_title = driver.title
exp_title = "OrangeHRM"
if actual_title == exp_title:
    print("Login Test Passed")
else:
    print("Login test failed")
driver.close()

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

############ find_element() -- Returns single web element

# 1. Locator matching with single web element

# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Apple MacBook")
#
# # 2. Locator matching with multiple  webelements
# element1=driver.find_element(By.XPATH, "//div[@class='footer']//a") # First element will be returned from multiple matchings
# print(element1.text) # Sitemap
#
# # 3. Element not available exception --> NoSuchElementException
# # element_login = driver.find_element(By.LINK_TEXT, "Log in") ## Correct Locator
# element_login = driver.find_element(By.LINK_TEXT, "Login") ## Incorrect locator
# element_login.click()
# time.sleep(3)

############ find_elements() -- Returns multiple WebElements
# 1. Locator matching with single web element

# 3. Element not available exception will not occur --> List returns 0 elements when web elements are not matching
footer_elements=driver.find_elements(By.XPATH, "//div[@class='foot']//ar")
print("Returned elements : ",len(footer_elements)) #23

driver.quit()
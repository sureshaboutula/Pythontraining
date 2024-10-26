import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
driver.get("https://www.facebook.com/")
driver.maximize_window()

### Tag & Id  ---> tagname#ValueofId : input#email ####

# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("samplemail@gmail.com")
#### tag name is always part of css selector hence it is not mandatory
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("samplemail@gmail.com")

### Tag & Class name  ---> tagname.valueofclass : input.inputtext _55r1 _6luy ####

#driver.find_element(By.CSS_SELECTOR, "input.inputtext _55r1 _6luy").send_keys("samplemail@gmail.com") --> Space inside class name
#driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("samplemail@gmail.com")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("samplemail@gmail.com")
# time.sleep(2)
# driver.close()

### Tag & Attribute ---> tagname[attribute=value] : input[data-testid=royal_email] #####
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("samplemail@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("samplemail@gmail.com")
# time.sleep(2)
# driver.close()

##### Tag & Class & Attribute ----> tagname.valueofclass[attribute=value] : input.inputtext[data-testid=royal_email]
#### For facebook application, we have same tag and class for both username and password. In this case, we need to use an attribute along with tag and class

driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("samplemail@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input.inputtext[placeholder=Password]").send_keys("password")
driver.find_element(By.CSS_SELECTOR, "button[data-testid=royal_login_button]").click()
time.sleep(10)
driver.close()

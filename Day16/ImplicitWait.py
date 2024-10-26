
#########Time.Sleep() approach
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
#
# service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj,options=chrome_options)
#
# driver.get("https://www.google.com/")
# driver.maximize_window()
#
# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys("Selenium")
# search_box.submit()
#
# # driver.find_element(By.XPATH, "//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()
#
# ## Due to Synch issue, sometimes script throws No Such Element Exception as the browser will be closed before finding the element
# ### Assume Synch Issue happens before line 19
#
# ### Using time.sleep()
# # Disadvanges --> This will reduce script performance
# #             --> If the element is not available within the time mentinoed, still there is change getting exception
# time.sleep(5)
# driver.find_element(By.XPATH, "//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()

######## Selenium Webdriver approach -- implicit and Explicit waits

### Implicit Wait:
# Advantages: 1. One statement will take care of synch issue for the complete script
#   2. It will not wait till the time we have passed in the implicit method. The moment element is found, it will go to the next statement. Performance will not be reduced
# Disadvantages: 1. It will still throws exception when the element is not found within the time passed in the implicit wait method

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
driver.implicitly_wait(10) ##### This will be applicable for all the statements after implicit wait statement

driver.get("https://www.google.com/")
driver.maximize_window()

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("Selenium")
search_box.submit()

driver.find_element(By.XPATH, "//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()
driver.quit()
################# Invoking chrome browser - Approach 1 without Service class ##################
import time

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")

################# Invoking chrome browser - Approach 2 - with Service class ##################
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# service_obj=Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/")

################# Invoking Firefox browser ##################
# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get("https://opensource-demo.orangehrmlive.com/")

###################  Invoking Firefox browser - with Service Class  ##################
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
service_obj=Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\geckodriver-v0.34.0-win-aarch64\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")

################# Invoking Edge browser ##################
# from selenium import webdriver
#
# driver = webdriver.Edge()
# driver.get("https://opensource-demo.orangehrmlive.com/")

################# Invoking Edge browser with Service class ##################
# from selenium.webdriver.edge.service import Service
# from selenium import webdriver
# service_obj=Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\edgedriver_win64\msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/")

#######################################################################

driver.maximize_window()
print("Title is : ",driver.title)
print("Current browser is: ",driver.current_url)
time.sleep(5)

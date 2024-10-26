import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"a[href='http://www.orangehrm.com']").click()
time.sleep(5)

#driver.close() # This command closes only the first tab with the url passed by get() method
driver.quit() # This command closes all the browser tabs
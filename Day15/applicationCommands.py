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
print(driver.title)  # OrangeHRM
print(driver.current_url)  # https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

print(driver.page_source)

driver.quit()
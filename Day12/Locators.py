import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
driver.get("https://demo.nopcommerce.com/")  ### http://automationpractice.com/index.php
driver.maximize_window()
sliders = driver.find_elements(By.CLASS_NAME,"nivo-imageLink")
print(len(sliders))

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

time.sleep(5)
driver.close()

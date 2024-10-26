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

### Absolute Xpath
# driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Laptop")
# driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

### Relative Xpath
# driver.find_element(By.XPATH, "//*[@id='small-searchterms']").send_keys("Laptop")
# driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button").click()

### or : //input[@name='q' or @id='small-searchterms']
# driver.find_element(By.XPATH, "//input[@name='q' or @id='small-searchterms']").send_keys("Laptop")
# driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button").click()

### and : //button[@class='button-1 search-box-button' and @type='submit']
# driver.find_element(By.XPATH, "//input[@name='q' or @id='small-searchterms']").send_keys("Laptop")
# driver.find_element(By.XPATH, "//button[@class='button-1 search-box-button' and @type='submit']").click()

### contains() and starts-with() and text()
# driver.find_element(By.XPATH, "//input[contains(@id,'small')]").send_keys("Laptop")
# driver.find_element(By.XPATH, "//button[starts-with(text(),'Sea')]").click()
# # driver.find_element(By.XPATH, "//button[text()='Search']").click()


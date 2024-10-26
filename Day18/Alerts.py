import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)

alertwindow = driver.switch_to.alert
print(alertwindow.text)

alertwindow.send_keys("Welcome")
alertwindow.accept() # Close alert by clicking Ok button

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)

alertwindow = driver.switch_to.alert
# print(alertwindow.text)

alertwindow.send_keys("Welcome")
alertwindow.dismiss() # Close alert by clicking Cancel button


driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#### is_displayed() and is_enabled()

search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Displayed Status : ", search_box.is_displayed())  # True
print("Displayed Status : ", search_box.is_enabled())   # True

#### is_selected()
male_radiobutton = driver.find_element(By.XPATH, "//input[@id='gender-male']")
female_radiobutton = driver.find_element(By.XPATH, "//input[@id='gender-female']")
print("Default Gender radio buttons Status...")
print(male_radiobutton.is_selected()) # False
print(female_radiobutton.is_selected()) # False

print("After selecting male radio button...")
male_radiobutton.click()
print(male_radiobutton.is_selected()) # True
print(female_radiobutton.is_selected()) # False

print("After selecting female radio button...")
female_radiobutton.click()
print(male_radiobutton.is_selected()) # False
print(female_radiobutton.is_selected()) # True

driver.quit()
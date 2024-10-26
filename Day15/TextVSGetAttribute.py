import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

email_id = driver.find_element(By.XPATH,"//input[@id='Email']")
# print("The result of get_attribute() is : ",email_id.get_attribute('value'))  ## admin@yourstore.com
email_id.clear()
email_id.send_keys("sampleemail@gmail.com")
print("The result of text is : ",email_id.text) # No output, as there is no inner text for input box
print("The result of get_attribute() is : ",email_id.get_attribute('value'))
print("The result of get_attribute() is : ",email_id.get_attribute('class'))
print("The result of get_attribute() is : ",email_id.get_attribute('name'))

login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print("The result of text for login button is :",login_button.text) ### LOG IN
print("The result of get_attribute() for login button is :", login_button.get_attribute('type')) ### submit
print("The result of get_attribute() for login button is :", login_button.get_attribute('value')) ### No output

time.sleep(3)
driver.quit()
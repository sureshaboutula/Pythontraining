import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Select single checkbox
# driver.find_element(By.XPATH, "//input[@id='wednesday']").click()

# #Select All checkboxes Approach 1:
# day_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
# print(len(day_checkboxes))
#
# for i in range(len(day_checkboxes)):
#     day_checkboxes[i].click()

#Select All checkboxes Approach 2:
# day_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
# for day_checkbox in day_checkboxes:
#     day_checkbox.click()

### Select multiple checkboxes by choice : Monday and Thursday
# day_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
# for day_checkbox in day_checkboxes:
#     weekname = day_checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='thursday':
#         day_checkbox.click()
# time.sleep(5)

### Select last 2 checkboxes:
### Formula --> Last n checkboxes then use len(total check boxes) - 2
# day_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
# for i in range(len(day_checkboxes)-2, len(day_checkboxes)): ### range(5,7) = index 6 and index 7
#     day_checkboxes[i].click()
# time.sleep(5)

### Select first 2 checkboxes
# day_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
# for i in range(len(day_checkboxes)):
#     if i<2:
#         day_checkboxes[i].click()
# time.sleep(2)

### Clearing all the checkboxes

day_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
for day_checkbox in day_checkboxes:
    day_checkbox.click()
time.sleep(3)

for day_checkbox in day_checkboxes:
    if day_checkbox.is_selected():
        day_checkbox.click()

time.sleep(3)
driver.quit()
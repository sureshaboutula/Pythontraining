import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# # Click on Link
# # driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

# Find number of links on a page
# links = driver.find_elements(By.TAG_NAME, "a")
links = driver.find_elements(By.XPATH, "//a")
print("Total number of Links : ", len(links))

# #Print all the link names
# for link in links:
#     print(link.text)

# # Print all link urls and count external and internal links
# ext_links = 0
# int_links = 0
# for link in links:
#     print(link.get_attribute("href"))
#     if link.get_attribute("href").startswith("https://demo.nopcommerce.com"):
#         int_links = int_links + 1
#     else:
#         ext_links = ext_links + 1
# print("Total External links : ", ext_links)
# print("Total Internal Links : ", int_links)

time.sleep(2)
driver.quit()
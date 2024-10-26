### Install requests moduel through File -> settings -> ProjectInterpreter -> search for requests package and install

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, "a")
count = 0
for link in all_links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url," is broken link")
        count+=1
    else:
        print(url," is valid link")
print("Total number of broken links: ",count)

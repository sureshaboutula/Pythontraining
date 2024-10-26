# 1) Open Web Browser(Chrome/firefox/IE).
# 2) Open URL  https://admin-demo.nopcommerce.com/login
# 3) Provide Email  (admin@yourstore.com).
# 4) Provide password  (admin).
# 5) Click on Login.
# 	driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
# 6) Capture title of the dashboad page.(Actual title)
# 7) Verify title of the page: "Dashboard / nopCommerce administration" (Expected)
# 8) close browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://admin-demo.nopcommerce.com/login")

driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.CLASS_NAME, "password").clear()
driver.find_element(By.CLASS_NAME, "password").send_keys("admin")
# driver.find_element(By.CLASS_NAME, "login-button").click()
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
act_title = driver.title
print(act_title)
exp_titile = "Dashboard / nopCommerce administration"
if act_title == exp_titile:
    print("Test Case is Passed")
else:
    print("Test Case is Failed")
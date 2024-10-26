import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
time.sleep(2)

print("One",driver.find_element(By.XPATH,"//a[contains(text(),'Indian Overseas')]/self::a").text)
print("\n Two",driver.find_element(By.XPATH, "//a[contains(text(),'Indian Overseas')]/parent::td").text)
print("\n Three",driver.find_element(By.XPATH,"//a[contains(text(),'Indian Overseas')]/ancestor::tr").text)
following_ele = driver.find_elements(By.XPATH,"//a[contains(text(),'Indian Overseas')]/following::td")
# for i in following_ele:
#     print(i.text)
print(len(following_ele))
child_ancest = driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/child::td")
# print("Starts child_ancest")
# for i in child_ancest:
#     print(i.text)
# print("end child_ancest")
print(len(child_ancest))

ancest_descen = driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/child::td")
# print("Starts ancest_descent")
# for i in ancest_descen:
#     print(i.text)
# print("end ancest_descent")
print(len(ancest_descen))
ancest_descen2 = driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/descendant::a")
# print("Starts ancest_descent2")
# for i in ancest_descen2:
#     print(i.text)
# print("end ancest_descent2")
print(len(ancest_descen2))

ancest_descen3 = driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/descendant::*")
# print("Starts ancest_descent3")
# for i in ancest_descen3:
#     print(i.text)
# print("end ancest_descent3")
print(len(ancest_descen3))
print(len(driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/preceding::*")))
print(len(driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/following::*")))

print(len(driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/preceding-sibling::*")))
print(len(driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/preceding-sibling::tr")))
print(len(driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/following-sibling::*")))
print(len(driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/following-sibling::tr")))

time.sleep(2)
driver.close()
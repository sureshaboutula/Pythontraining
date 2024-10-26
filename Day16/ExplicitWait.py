#### ExplicitWait

### Advantages :
# 1. More Effective
# 2. It will not wait till the time we have passed in the implicit method. The moment element is found, it will go to the next statement. Performance will not be reduced
# 3. If the element is not found within the time passed in ExplicitWait declaration, then it will throw exception by default. But this can be handled by passing ignore_exceptions attribute in WebdriverWait class

### Disadvantages:
# 1. Complex. Need to be called at multiple places
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\0G3425649\Documents\Pythontraining\Browser Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

### ExplicitWait declaration
waitdec = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                ElementNotVisibleException,
                                                                ElementNotSelectableException, Exception]
                        )

driver.get("https://www.google.com/")
driver.maximize_window()

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("Selenium")
search_box.submit()

search_link = waitdec.until(EC.presence_of_element_located((By.XPATH, "//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']")))
search_link.click()
driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
class ElementState():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def isEnabled(self):
        baseURL = "https://google.com"
        chrome_options = Options()
        # incognito window
        chrome_options.add_argument("--incognito")
        driver = self.get_driver()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        e1 = driver.find_element(By.ID, 'gs_htif0')
        e1State = e1.is_enabled()  # True for enabled and False for disabled
        print("E1 is Enabled? -> " + str(e1State))

        e2 = driver.find_element(By.ID, 'gs_taif0')
        e2State = e2.is_enabled()  # True for enabled and False for disabled
        print("E2 is Enabled? -> " + str(e2State))

        e3 = driver.find_element(By.ID, 'lst-ib')
        e3State = e3.is_enabled()  # True for enabled and False for disabled
        print("E3 is Enabled? -> " + str(e3State))

        e3.send_keys("letskodeit")

e = ElementState()
e.isEnabled()

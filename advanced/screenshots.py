from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from webdriver_manager.core import driver


class Screenshots():

        def get_driver(self):
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        def test(self):
            baseURL = "https://eobuwie.com.pl/"
            # chrome_options = Options()
            # # incognito window
            # chrome_options.add_argument("--incognito")
            driver = self.get_driver()
            driver.get(baseURL)
            driver.maximize_window()
            driver.implicitly_wait(5)

            driver.find_element(By.XPATH, "//span[contains(text(),'Zaloguj się')]").click()
            driver.find_element(By.ID, "email").send_keys("abc@email.com")
            driver.find_element(By.ID, "password").send_keys("abc")
            driver.find_element(By.CSS_SELECTOR, ".button-large.submit.primary").click()
            # destinationFileName = "C:/Users/48730/Desktop/example.png"

        # try:
        #     driver.save_screenshot(destinationFileName)
        #     print("Screenshot saved to directory --> :: " + destinationFileName)
        # except NotADirectoryError:
        #     print("Not a directory issue")

ff = Screenshots()
ff.test()
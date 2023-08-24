from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WindowSize():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = self.get_driver()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height : " + str(height))
        print("Width : " + str(width))


ff = WindowSize()
ff.test()
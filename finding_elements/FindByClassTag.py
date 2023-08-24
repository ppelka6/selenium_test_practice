import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from pages.CommonPage import CommonPage

class FindByClassTag():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = self.get_driver()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByClassName = driver.find_element(By.CLASS_NAME, "inputs")
        if elementByClassName is not None:
            print("Element Found -> By ClassName")
            elementByClassName.send_keys('Testing')

        elementByTagName = driver.find_element(By.TAG_NAME, "a")
        if elementByTagName is not None:
            print("Element Found -> By TagName:" + elementByTagName.text)

        time.sleep(5)

run_tests = FindByClassTag()
run_tests.test()
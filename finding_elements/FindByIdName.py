from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from pages.CommonPage import CommonPage

class FindByIdName():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = self.get_driver()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementById = driver.find_element(By.ID, "confirmbtn")
        if elementById is not None:
            print("Element Found -> By Id")

        elementByName = driver.find_element(By.NAME, "enter-name")
        if elementByName is not None:
            print("Element Found -> By Name")

run_tests = FindByIdName()
run_tests.test()
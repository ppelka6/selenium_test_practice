from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from pages.CommonPage import CommonPage

class FindByLinkText():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = self.get_driver()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByLinkText = driver.find_element(By.LINK_TEXT, "HOME")
        if elementByLinkText is not None:
            print("Element Found -> By LinkText")

        elementByPartialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, "COURSE")
        if elementByPartialLinkText is not None:
            print("Element Found -> By PartialLinkText")

run_tests = FindByLinkText()
run_tests.test()
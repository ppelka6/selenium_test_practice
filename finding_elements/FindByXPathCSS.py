from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from pages.CommonPage import CommonPage

class FindByXPathCSS():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = self.get_driver()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByXPath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if elementByXPath is not None:
            print("Element Found -> By XPath")

        elementByCSS = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if elementByCSS is not None:
            print("Element Found -> By CSS")

run_tests = FindByXPathCSS()
run_tests.test()
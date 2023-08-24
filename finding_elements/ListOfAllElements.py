from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from pages.CommonPage import CommonPage

class ListOfElements():

    @property
    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = self.get_driver
        driver.get(baseUrl)

        elementListByClassName = driver.find_elements(By.CLASS_NAME, "inputs")
        length1 = len(elementListByClassName)

        if elementListByClassName is not None:
            print("ClassName -> Size of the list is: " + str(length1))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("TagName -> Size of the list is: " + str(length2))


run_tests = ListOfElements()
run_tests.test()
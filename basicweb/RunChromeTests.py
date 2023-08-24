from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RunChrome():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = self.get_driver
        driver.get(baseUrl)
        driver.implicitly_wait(10)

testing = RunChrome()
testing.test()
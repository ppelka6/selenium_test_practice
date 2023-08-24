from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class DynamicXPathFormat():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test(self):
        baseURL = "https://www.letskodeit.com/home"
        # chrome_options = Options()
        # # incognito window
        # chrome_options.add_argument("--incognito")
        driver = self.get_driver()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
        email = driver.find_element(By.ID, "email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "login-password")
        password.send_keys("abcabc")
        driver.find_element(By.ID, "login").click()

        # searchBox = driver.find_element(By.ID, "search-courses")
        # searchBox.send_keys("JavaScript")
        #
        # course = driver.find_element(By.ID, "search-course")
        # searchBox.send_keys("JavaScript")
        #
        # # Select Course
        # _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        # _courseLocator = _course.format("JavaScript for beginners")
        #
        # courseElement = driver.find_element(By.XPATH, _courseLocator)
        # courseElement.click()

ff = DynamicXPathFormat()
ff.test()
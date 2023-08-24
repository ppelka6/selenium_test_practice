from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ScrollingElements():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = self.get_driver()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.execute_script("window.scrollBy(0, 700); ") #scroll down
        time.sleep(3)

        driver.execute_script("window.scrollBy(0, -1000); ") #scroll up
        time.sleep(3)

        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true); ", element) #scroll element into to view
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -150); ")

        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -1000); ") #native Way To Scroll Element Into View
        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))

ff = ScrollingElements()
ff.test()

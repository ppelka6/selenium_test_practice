from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class Sliders():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test1(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = self.get_driver()
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//*[@id='sidebar']/aside[2]/ul/li[11]/a")
        time.sleep(3)
        try:
            action = ActionChains(driver)
            action.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Sliding Element Successful")
            time.sleep(2)
        except:
            print("Sliding failed on element")


ff = Sliders()
ff.test1()
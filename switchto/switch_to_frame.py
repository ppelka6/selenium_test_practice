from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class SwitchToFrame():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = self.get_driver()
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 1000);")

        driver.switch_to.frame("courses-iframe")

        time.sleep(3)

        searchBox = driver.find_element(By.XPATH, "search")
        searchBox.send_keys("python")
        time.sleep(3)

        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, 1000);")

        searchBox = driver.find_element(By.ID, "search")
        searchBox.send_keys("Python")
        time.sleep(3)
        driver.find_element(By.ID, "name").send_keys("Test succesfull")


ff = SwitchToFrame()
ff.test()
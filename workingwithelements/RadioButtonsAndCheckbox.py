import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class RadioButtonAndCheckboxes():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        # chrome_options = Options()
        # # incognito window
        # chrome_options.add_argument("--incognito")
        driver = self.get_driver()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element(By.ID,'bmwradio')
        bmwRadioBtn.click()

        time.sleep(2)

        benzRadioBtn = driver.find_element(By.ID,'benzradio')
        benzRadioBtn.click()

        time.sleep(2)

        bmwCheckbox = driver.find_element(By.ID,'bmwcheck')
        bmwCheckbox.click()

        time.sleep(2)

        benzCheckbox = driver.find_element(By.ID,'benzcheck')
        benzCheckbox.click()

        time.sleep(2)

        print("BMW radio btn is selected? " + str(bmwRadioBtn.is_selected())) # True if is selected
        print("BENZ radio btn is selected? " + str(benzRadioBtn.is_selected()))
        print("BMW checkbox is selected? " + str(bmwCheckbox.is_selected()))
        print("BENZ checkbox is selected? " + str(benzCheckbox.is_selected()))



ff2 = RadioButtonAndCheckboxes()
ff2.test()


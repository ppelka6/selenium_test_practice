from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WorkingWithElementsList():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def testListOfElements(self):
        baseURL = "https://www.letskodeit.com/practice"
        # chrome_options = Options()
        # # incognito window
        # chrome_options.add_argument("--incognito")
        driver = self.get_driver()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)

        radioButtonList = driver.find_elements(By.XPATH, "//input[contains(@type,'radio') and contains(@name, 'cars')]")
        size = len(radioButtonList)
        print("Size of the list: " + str(size))

        for radioButton in radioButtonList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(5)

ff = WorkingWithElementsList()
ff.testListOfElements()
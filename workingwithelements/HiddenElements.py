from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class HiddenElements():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def testLetsKodeIt(self):
        baseURL = "https://www.letskodeit.com/practice"
        # chrome_options = Options()
        # # incognito window
        # chrome_options.add_argument("--incognito")
        driver = self.get_driver()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        textBoxElement = driver.find_element(By.ID, "displayed-text")
        textBoxState = textBoxElement.is_displayed() # True if visible, False if hidden
        print("Text is visible?" + str(textBoxState))
        time.sleep(2)

        driver.find_element(By.ID, "hide-textbox").click()

        textBoxState = textBoxElement.is_displayed()
        print("Text is visible?" + str(textBoxState))
        time.sleep(2)


        driver.find_element(By.ID, "show-textbox").click()
        textBoxState = textBoxElement.is_displayed()  # True if visible, False if hidden
        print("Text is visible?" + str(textBoxState))
        time.sleep(2)

        driver.quit()

    def testExpedia(self):
        baseURL = "https://www.expedia.com/"
        # chrome_options = Options()
        # # incognito window
        # chrome_options.add_argument("--incognito")
        driver = self.get_driver()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)


        drpdwnElement = driver.find_element(By.XPATH, "//span[contains(text(),'Flights')]")
        print("Element visible?" + str(drpdwnElement.is_displayed()))


ff = HiddenElements()
ff.testLetsKodeIt()
ff.testExpedia()






        
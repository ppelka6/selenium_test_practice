import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class ClickAndSendKeys():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def test(self):
        baseURL = "https://letskodeit.teachable.com"
        chrome_options = Options()
        # incognito window
        chrome_options.add_argument("--incognito")
        driver = self.get_driver()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)


        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()
        emailField = driver.find_elements(By.ID, "email")
        emailField.send_keys("test")
        passwordField = driver.find_elements(By.ID, "password")
        passwordField.send_keys("test")

        time.sleep(3)

        emailField.clear()

        time.sleep(3)
        emailField.send_keys("test")

test2 = ClickAndSendKeys()
test2.test()

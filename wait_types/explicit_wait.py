from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ExplicitWaitDemo():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test(self):
        baseURL = "https://www.letskodeit.com/home"
        # chrome_options = Options()
        # # incognito window
        # chrome_options.add_argument("--incognito")
        driver = self.get_driver()
        # driver.get(baseURL)
        driver.maximize_window()

        driver.execute_script("window.location = 'https://www.letskodeit.com/home';")
        driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()

        wait = WebDriverWait(driver, timeout=20, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                                       ElementNotVisibleException,
                                                                                       ElementNotVisibleException])

        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Sign In')]")))
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo()
ff.test()
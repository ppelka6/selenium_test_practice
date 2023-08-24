from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class CalendarSelection():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test1(self):
        baseURL = "https://www.expedia.com/"
        # chrome_options = Options()
        # # incognito window
        # chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome()
        driver = self.get_driver()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.find_element(By.XPATH, "//span[contains(text(),'Hotels & homes')]").click()

        driver.find_element(By.CLASS_NAME, "uitk-faux-input uitk-form-field-trigger").click()

        departingField = driver.find_element(By.CSS_SELECTOR('button[aria-label="Aug 29, 2023"]'))

        departingField.click()

        time.sleep(5)
        driver.quit()

    def test2(self):
        baseURL = "https://www.expedia.com/"
        # chrome_options = Options()
        # # incognito window
        # chrome_options.add_argument("--incognito")
        driver = self.get_driver()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # # Click flights tab
        # driver.find_element(By.XPATH, "//span[contains(text(),'Hotels & homes')]").click()
        # # Click departing field
        driver.find_element_by_id("flight-departing").click()
        # Expedia website has changed the DOM after the lecture was made
        # Updated new xpath
        calMonth = driver.find_element(By.XPATH, "(//div[@class='datepicker-cal-month'])[1]")
        allValidDates = calMonth.find_elements(By.TAG_NAME, "button")

        time.sleep(2)

        for date in allValidDates:
            if date.text == "30":
                date.click()
                break

ff = CalendarSelection()
ff.test2()




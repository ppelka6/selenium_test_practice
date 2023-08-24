from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class SwitchToWindow():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = self.get_driver()
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)


        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switch to window: " + handle)
                searchBox = driver.find_element(By.XPATH, "search")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break

                # Switch back to the parent handle
            driver.switch_to.window(parentHandle)
            driver.find_element(By.ID, "alert-example-div").send_keys("Test Successful")

ff = SwitchToWindow()
ff.test()
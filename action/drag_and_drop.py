from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class DragAndDrop():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test1(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = self.get_driver()
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)

        driver.switch_to.frame(0)

        fromElement = driver.find_element(By.ID, "draggable")
        toElement = driver.find_element(By.ID, "droppable")
        time.sleep(3)

        try:
            action = ActionChains()
            # action.drag_and_drop(fromElement, toElement).perform()
            action.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag and Drop Element Successful")
            time.sleep(3)
        except:
            print("Drag and Drop failed on Element")




ff = DragAndDrop()
ff.test1()
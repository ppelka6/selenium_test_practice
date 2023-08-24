from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://www.plupload.com/examples")
driver.find_element(By.ID, "uploader_browse").click()
time.sleep(5)

keyboard = Controller()

keyboard.type("C:\\Users\\48730\\Desktop\\sheep.avif")

keyboard.press()

keyboard.release()
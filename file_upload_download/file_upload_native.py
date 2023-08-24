from selenium import webdriver
from selenium.webdriver.common.by import By


# webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome()
# driver.implicitly_wait(3)
# driver.maximize_window()
# driver.get("https://www.plupload.com/examples")
# # element = driver.find_element(By.ID, "uploader_browse")
# element = driver.find_element(By.XPATH, "//div[@id='uploader_buttons']/div/input")
# element.send_keys("C:\\Users\\48730\\Desktop\\sheep.avif")

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://imgbb.com/upload")
element = driver.find_element(By.ID, "anywhere-upload-input")
element.send_keys("C:\\Users\\48730\\Desktop\\sheep.avif")
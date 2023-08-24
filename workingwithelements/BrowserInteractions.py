from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BrowserInteractions():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test(self):
        driver = self.get_driver()
        baseUrl = "https://courses.letskodeit.com/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # Window maximize
        driver.maximize_window()
        # Open the baseUrl
        driver.get(baseUrl)
        # Get Title
        title = driver.title
        print("Title of tis web page is: " + title)
        # Get Current Url
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        # Browser refresh
        driver.refresh()
        print("Browser refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")
        # Open another Url
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?reset_purchase_session=1")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        # Browser Back
        driver.back()
        print("Go one step back in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)
        # Get Page Source
        pageSource = driver.page_source
        print(pageSource)
        # Browser Close / Quit
        # driver.close()
        driver.quit()

ff = BrowserInteractions()
ff.test()




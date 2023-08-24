import unittest
from selenium.common import NoSuchElementException
from common import browser
from PropertyReader import PropertyReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonPage(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.driver = browser.get_driver()
        self.config = PropertyReader()

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def find(self, by, selector):
        try:
            return self.driver.find_element(by, selector)
        except NoSuchElementException as ex:
            raise Exception(f'Not able to find element: {selector} by: {by} with message: {ex.msg}') from ex

    def wait_for_element_present(self, by, selector, wait_time=10):
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.presence_of_element_located((by, selector)))

    def quit_browser(self):
        self.driver.quit()
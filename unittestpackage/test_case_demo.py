import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestCaseDemo(unittest.TestCase):

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def setUp(self):
        print("I will run once before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Runnin method B")


    def tearDown(self):
        print("I will run after every test")

if __name__ == '__main__':
    unittest.main(verbosity=2)
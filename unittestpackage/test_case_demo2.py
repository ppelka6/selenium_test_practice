import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestCaseDemo2(unittest.TestCase):

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    @classmethod
    def setUpClass(self):
        print("*#" * 30)
        print("I will run only once before all tests")
        print("*#" * 30)

    def setUp(self):
        print("I will run only once before all tests")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Runnin method B")

    def tearDown(self):
        print("I will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("I will run only once after all tests")
        print("*#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)

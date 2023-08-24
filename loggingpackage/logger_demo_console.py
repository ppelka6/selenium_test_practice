"""
Logger Demo
"""
import logging
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class LoggerDemoConsole():

    def get_driver(self):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def testLog(self):
        #create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        #create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)
        #create formatter
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
        #add formatter to console handler -> ch
        chandler.setFormatter(formatter)
        #add console handler to logger
        logger.addHandler(chandler)
        #loggin messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConsole()
demo.testLog()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import *


class DriverConfig:

    @staticmethod
    def set_driver(test_browser, webdriver):

        test_driver = None

        if test_browser == 'chrome':
            test_driver = webdriver.Chrome()

        elif test_browser == 'chrome-headless':
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            test_driver = webdriver.Chrome(options=chrome_options)

        return test_driver

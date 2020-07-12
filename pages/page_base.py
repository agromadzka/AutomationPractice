from helpers.webdriver_extensions import WebdriverExtensions


class PageBase(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver_extensions = WebdriverExtensions(self.driver)

    def navigate(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

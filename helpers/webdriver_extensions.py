import requests

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class WebdriverExtensions(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_until_visible(self, locator):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(
                ec.visibility_of_element_located(locator)
            )
            return element
        except NoSuchElementException:
            print("No visible element.")

    def click_visible(self, selector):
        try:
            self.wait_until_visible(selector)
            self.driver.find_element(*selector).click()
        except:
            print("No such elements.")

    def fill_input(self, input_locator, text):
        self.wait_until_visible(input_locator)
        self.driver.find_element(*input_locator).clear()
        self.driver.find_element(*input_locator).send_keys(text)

    def hover_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def elements_text(self, locator):
        self.wait_until_visible(locator)
        return self.driver.find_element(*locator).text

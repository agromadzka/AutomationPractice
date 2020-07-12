from selenium import webdriver

import pytest
from config import test_browser
from config import screenshot_path
from driver_config import DriverConfig
from helpers.screenshot_helper import ScreenshotHelper
from helpers.browser_console_helper import BrowserConsoleHelper


@pytest.fixture()
def driver(request):
    driver = DriverConfig.set_driver(test_browser, webdriver)
    driver.maximize_window()

    def finalize():
        driver.quit()

    request.addfinalizer(finalize)
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs['driver']
        BrowserConsoleHelper.print_browser_console_log(driver)
        BrowserConsoleHelper.print_browser_console_errors(driver)

        if report.failed:
            ScreenshotHelper.save_screenshot(driver, report.head_line, screenshot_path)

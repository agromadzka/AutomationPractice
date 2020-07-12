import os

from datetime import datetime


class ScreenshotHelper(object):

    @classmethod
    def save_screenshot(cls, driver, test_id, screenshot_path):
        current_date = datetime.now().strftime('%Y-%m-%d')
        current_screenshots_directory = os.path.join(screenshot_path, current_date)

        if not os.path.exists(current_screenshots_directory):
            os.makedirs(current_screenshots_directory)

        current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = current_datetime + '_' + test_id + '.png'
        file_path = os.path.join(current_screenshots_directory, file_name)

        driver.get_screenshot_as_file(file_path)

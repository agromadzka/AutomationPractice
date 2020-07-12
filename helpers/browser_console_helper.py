import logging


class BrowserConsoleHelper(object):

    @classmethod
    def get_browser_console_log(cls, driver):
        try:
            return driver.get_log('browser')
        except Exception as e:
            logging.exception(e)

    @classmethod
    def print_browser_console_log(cls, driver):
        log = cls.get_browser_console_log(driver)
        print("\n Console Log: ", log)

    @classmethod
    def print_browser_console_errors(cls, driver):
        severe_log_entries = []

        log = cls.get_browser_console_log(driver)
        for entry in log:
            if entry['level'] == 'SEVERE':
                severe_log_entries.append('\n' + entry['message'])

        if len(severe_log_entries) > 0:
            print(" \n \n Browser console error:%s" %
                  ('\n '.join(severe_log_entries)))

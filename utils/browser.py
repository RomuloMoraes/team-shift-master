from selenium.webdriver import Firefox, FirefoxOptions
from settings import SYSTEM_TYPE


class FirefoxBrowser:
    def __init__(self):
        self.options = FirefoxOptions()
        self.options.headless = False

        self.driver_path = f'../driver/geckodriver_{SYSTEM_TYPE}.exe'
        self.driver = Firefox(executable_path=self.driver_path, options=self.options)
        self.driver.set_page_load_timeout(60)

    def get_driver(self):
        return self.driver

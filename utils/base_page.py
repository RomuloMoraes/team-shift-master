from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class BasePageElements:
    def click_on_object(self, object):
        el = WebDriverWait(self.driver, 60).until(
            ec.element_to_be_clickable(object)
        )
        el.click()

    def type(self, object, value):
        el = WebDriverWait(self.driver, 60).until(
            ec.element_to_be_clickable(object)
        )
        el.clear()
        el.send_keys(value)

    def wait_for_object_to_be_visible(self, object):
        el = WebDriverWait(self.driver, 60).until(
            ec.visibility_of_element_located(object)
        )
        return el


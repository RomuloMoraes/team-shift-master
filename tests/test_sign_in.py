import unittest

from page_object.home_page import HomePageLocators
from page_object.main_page import MainPage, MainPageLocators
from settings import USER_EMAIL, USER_PASSWORD
from utils.browser import FirefoxBrowser


class TestSignInPage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = FirefoxBrowser().get_driver()
        self.driver.get(MainPageLocators.URL)
        self.main_page = MainPage(self.driver)

    def test_successful_logging_on_teamshift_using_email_and_password(self):

        self.main_page.login(email=USER_EMAIL, password=USER_PASSWORD)
        user_menu = self.main_page.wait_for_object_to_be_visible(HomePageLocators.USER_MENU)
        self.assertTrue(user_menu)

    def tearDown(self) -> None:
        self.driver.quit()

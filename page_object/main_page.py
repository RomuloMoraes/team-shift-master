from selenium.webdriver.common.by import By

from utils.base_page import BasePage, BasePageElements


class MainPageLocators:
    URL = 'https://teamshift-qa.crossknowledge.com/'
    LOGIN_BUTTON = (By.CLASS_NAME, 'js-login-member-button')
    EMAIL_INPUT = (By.ID, 'login-form__login')
    PASSWORD_INPUT = (By.ID, 'login-form__password')
    NEXT_BUTTON = (By.CLASS_NAME, 'js-login-form-submit')


class MainPage(BasePage, BasePageElements):

    def login(self, email, password):
        self.click_on_object(MainPageLocators.LOGIN_BUTTON)
        self.type(MainPageLocators.EMAIL_INPUT, email)
        self.click_on_object(MainPageLocators.NEXT_BUTTON)
        self.type(MainPageLocators.PASSWORD_INPUT, password)
        self.click_on_object(MainPageLocators.NEXT_BUTTON)


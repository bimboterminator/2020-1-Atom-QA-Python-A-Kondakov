from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from ui.locators.basic_locators import LoginPageLocators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def auth_with_text(self, email, passwd):
        self.click(self.locators.SIGNBUTTON)
        self.enter_text(self.locators.EMAILFIELD, email)
        self.enter_text(self.locators.PASSWDFIELD, passwd)
        self.click(self.locators.AUTHBUTTON)
        self.wait(10)

    def email_isdisplayed(self):
        try:
            namewrap = self.find(self.locators.LOGINSHOW)
            return namewrap.text
        except TimeoutException:
            return 'Invalid'

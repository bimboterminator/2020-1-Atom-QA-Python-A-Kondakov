from ui.pages.base_page import BasePage
from ui.locators.basic_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    locators = MainPageLocators()

    def go_to_campaigncreation(self):
        self.click(self.locators.STARTCREATE)

    def go_to_audience(self):
        self.click(self.locators.AUDIENCE)

    def is_present(self, name):
        namelocator = (By.XPATH, f'//a[@title="{name}"]')
        try:
            self.find(namelocator)
            return True
        except TimeoutException:
            return False


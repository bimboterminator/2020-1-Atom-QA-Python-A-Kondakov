import os
from ui.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from ui.locators.basic_locators import NewSegmentLocators
from selenium.webdriver.common.by import By


class SegmentPage(BasePage):
    locators = NewSegmentLocators()

    def delete_segment(self, name):
        namelocator = (By.XPATH, f'//a[@title="{name}"]')
        element = self.find(namelocator)
        id = element.get_attribute('href')
        id = os.path.basename(os.path.normpath(id))
        checkbox = (By.XPATH, f'//span[contains(text(), "{id}")]/parent::div/input')
        self.click(checkbox)
        self.click(self.locators.ACTIONS, timeout=10)

        self.click(self.locators.DELETE)

    def is_present(self, name):
        namelocator = (By.XPATH, f'//a[@title="{name}"]')
        try:
            self.find(namelocator)
            return True
        except TimeoutException:
            return False

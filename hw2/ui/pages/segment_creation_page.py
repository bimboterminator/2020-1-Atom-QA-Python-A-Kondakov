from selenium.common.exceptions import TimeoutException
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import NewSegmentLocators
import time


class NewSegment(BasePage):
    locators = NewSegmentLocators()

    def create_segment(self):

        try:
            self.click(self.locators.STARTCREATE_02)
        except TimeoutException:
            self.click(self.locators.STARTCREATE_01)

        self.click(self.locators.SEGMENT)
        self.click(self.locators.MAINCHECK)
        self.click(self.locators.ADD)

        textfield = self.find(self.locators.NAMEINPUT)
        textfield.clear()
        name = f'segment {time.ctime()}'
        textfield.send_keys(name)

        self.click(self.locators.STARTCREATE_02)

        return name

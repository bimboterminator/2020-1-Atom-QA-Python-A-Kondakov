from ui.pages.base_page import BasePage
import os
import time
from ui.locators.basic_locators import MainPageLocators
from ui.locators.basic_locators import CreatingCampaignLocators
from random import randint

class CreatingCampaign(BasePage):
    locators = CreatingCampaignLocators()

    def create(self):

        self.click(self.locators.TYPE, timeout=10)
        self.enter_text(self.locators.INPUTURL, 'app.com')
        self.click(self.locators.CLEAR)

        name = f'campaign {time.ctime()}'
        self.enter_text(self.locators.NAMEINPUT, name)

        self.click(self.locators.BANNER)

        path_photo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "new.jpg")
        path_photo = os.path.normpath(path_photo)

        self.find(self.locators.LOADIMAGE).send_keys(path_photo)
        time.sleep(5)
        self.click(self.locators.CREATECAMPAIGN, timeout=10)

        return name

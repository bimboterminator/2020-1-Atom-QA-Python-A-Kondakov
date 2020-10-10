import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from tests.base import BaseCase


class Test(BaseCase):
    @pytest.mark.skip(reason='no need')
    def test_auth(self, userconfig):
        email = userconfig['email']
        passwd = userconfig['passwd']
        self.login_page.auth_with_text(email, passwd)
        text = self.login_page.email_isdisplayed()
        assert email == text.lower()

    @pytest.mark.skip(reason='no need')
    def test_auth_negative(self):
        self.login_page.auth_with_text('email@mail.ru', 'rfpfyjdf')
        text = self.login_page.email_isdisplayed()
        assert text == 'Invalid'

    def test_creating_company(self):
        self.login_page.auth_with_text('condackow.aleck@yandex.ru', 'rfpfyjdf192168')
        self.creator_page.create()

        #namelocator = (By.XPATH, f'//a[@class="campaigns-tbl-cell__campaign-name" and @title="{name}"]')
        #assert self.creator_page.find(namelocator,timeout=10).is_displayed()


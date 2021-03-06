import pytest
from selenium.webdriver.common.by import By

from tests.base import BaseCase


class Test(BaseCase):


    @pytest.mark.UI
    def test_auth(self, config):
        email = config['email']
        passwd = config['passwd']
        self.login_page.auth_with_text(email, passwd)

        assert self.login_page.email_isDisplayed()


    @pytest.mark.UI
    def test_auth_negative(self):
        self.login_page.auth_with_text('email@mail.ru', 'rfpfyjdf')
        assert not self.login_page.email_isDisplayed()


    @pytest.mark.UI
    def test_creating_campaign(self, authorize):
        main_page = authorize
        main_page.go_to_campaigncreation()
        name = self.creator_page.create()
        assert main_page.is_present(name)


    @pytest.mark.UI
    def test_creating_segment(self, authorize):
        main_page = authorize
        main_page.go_to_audience()
        name = self.newsegment_page.create_segment()
        assert self.segment_page.is_present(name)

    
    @pytest.mark.UI
    def test_deleting_segment(self, authorize):
        main_page = authorize
        main_page.go_to_audience()
        name = self.newsegment_page.create_segment()
        self.segment_page.delete_segment(name)
        assert not self.segment_page.is_present(name)

import os

import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.company_creation_page import CreatingCampaign
from ui.pages.segment_creation_page import NewSegment
from ui.pages.segment_page import SegmentPage

class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.creator_page: CreatingCampaign = request.getfixturevalue('creator_page')
        self.newsegment_page: NewSegment = request.getfixturevalue('segment_page_new')
        self.segment_page: SegmentPage = request.getfixturevalue('segment_page_table')

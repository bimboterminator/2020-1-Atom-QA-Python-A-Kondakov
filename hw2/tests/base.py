import os

import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.company_creation_page import CreatingCampaign

class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, userconfig, request: FixtureRequest):
        self.driver = driver
        self.config = userconfig

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.creator_page: CreatingCampaign = request.getfixturevalue('creator_page')

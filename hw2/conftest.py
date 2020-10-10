import pytest
from selenium import webdriver

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.company_creation_page import CreatingCampaign

@pytest.fixture(scope='session')
def userconfig():
    url = 'https://target.my.com/'
    email = 'condackow.aleck@yandex.ru'
    password = 'rfpfyjdf192168'
    return {'url': url, 'email': email, 'passwd': password}

@pytest.fixture(scope='function')
def driver(userconfig):
    url = userconfig['url']
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def creator_page(driver):
    return CreatingCampaign(driver=driver)



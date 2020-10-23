import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.company_creation_page import CreatingCampaign
from ui.pages.main_page import MainPage
from ui.pages.segment_creation_page import NewSegment
from ui.pages.segment_page import SegmentPage


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=None)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')
    email = 'condackow.aleck@yandex.ru'
    password = 'rfpfyjdf192168'
    return {'browser': browser, 'version': version, 'url': url, 'selenoid': selenoid, 'email': email, 'passwd': password}

@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    selenoid = config['selenoid']
    if not selenoid:
        manager = ChromeDriverManager(version=version)
        driver = webdriver.Chrome(executable_path=manager.install())
        #driver = webdriver.Chrome(executable_path='C:\\Users\\BIMBO\\Documents\\Homeworks\\chromedriver.exe')
    else:
        options = ChromeOptions()
        capabilities = {'acceptInsecureCerts': True,
                        'browserName': 'chrome',
                        'version': '80.0'}
        driver = webdriver.Remote(command_executor=selenoid,
                                  options=options,
                                  desired_capabilities=capabilities)
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


@pytest.fixture
def segment_page_new(driver):
    return NewSegment(driver=driver)


@pytest.fixture
def segment_page_table(driver):
    return SegmentPage(driver=driver)


@pytest.fixture(scope='function', autouse=False)
def authorize(login_page, config):
    login_page.auth_with_text(config['email'], config['passwd'])
    return MainPage(driver=login_page.driver)



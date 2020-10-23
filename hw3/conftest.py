from dataclasses import dataclass
from api.target_client import TargetClient
import pytest


@dataclass
class Settings:
    URL: str = None
    email: str = None
    passwd: str = None


@pytest.fixture(scope='session')
def config() -> Settings:
    settings = Settings(URL='https://target.my.com', email='condackow.aleck@yandex.ru', passwd='rfpfyjdf192168')
    return settings


@pytest.fixture(scope='function')
def api_client(config):
    return TargetClient(config.email, config.passwd)
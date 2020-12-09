from urllib.parse import urljoin

APP_HOST, APP_PORT = '127.0.0.1', 1050
APP_URL = f'http://{APP_HOST}:{APP_PORT}'

MOCK_HOST, MOCK_PORT = '127.0.0.1', 1052
MOCK_URL = f'http://{MOCK_HOST}:{MOCK_PORT}'

USD_URL = 'https://api.exchangerate-api.com/v4/latest/USD'


MOCK_USD_URL = urljoin(MOCK_URL, 'usd')
MOCK_EUR_URL = urljoin(MOCK_URL, 'eur')
MOCK_GET_URL = urljoin(MOCK_URL, 'hist')
MOCK_TIME = urljoin(MOCK_URL, 'timeout')
MOCK_ERROR = urljoin(MOCK_URL, 'ok')
USD = 'usd'

APP_POST_URL = urljoin(APP_URL, 'send')
APP_GET_URL = urljoin(APP_URL, 'history')
APP_SHUTDOWN_URL = urljoin(APP_URL, 'shutdown')

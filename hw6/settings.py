from urllib.parse import urljoin

APP_HOST, APP_PORT = '127.0.0.1', 1050
APP_URL = f'http://{APP_HOST}:{APP_PORT}'

MOCK_HOST, MOCK_PORT = '127.0.0.1', 1052
MOCK_URL = f'http://{MOCK_HOST}:{MOCK_PORT}'

USD_URL = 'https://api.exchangerate-api.com/v4/latest/USD'
APP_SHUTDOWN_URL = urljoin(APP_URL, 'shutdown')
MOCK_USD_URL = urljoin(MOCK_URL, 'usd')
MOCK_EUR_URL = urljoin(MOCK_URL, 'eur')
USD = 'usd'
APP_POST_URL = urljoin(APP_URL, 'send')
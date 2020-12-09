from mock_server.http_mock import MockHTTPServer
from application import converter
from sock.client_socket import SocketClient
import pytest
import requests
import json
from settings import APP_SHUTDOWN_URL, MOCK_HOST, MOCK_PORT, USD, APP_PORT,APP_HOST


class TestMockServer:

    @pytest.fixture(scope='session')
    def mock_server(self):
        server = MockHTTPServer(MOCK_HOST, MOCK_PORT)
        server.start()
        yield server
        server.stop()

    @pytest.fixture(scope='session')
    def app(self):
        converter.run_app()
        yield
        requests.get(APP_SHUTDOWN_URL)

    @pytest.fixture(scope='session')
    def client_app(self):
        socket = SocketClient(APP_HOST, APP_PORT)
        return socket

    @pytest.fixture(scope='session')
    def client_mock(self):
        socket = SocketClient(MOCK_HOST, MOCK_PORT)
        return socket

    '''Пользовательские тесты'''

    def test_app_convert(self, app, mock_server, client_app):
        test_trans = {'id': 0,
            'county':'USA',
            'emitent_curr':'USD',
            'emit_card':111111111111,
            'recieve_card':2222222222,
            'reciever_curr':'EUR',
            'amount': 200}
        response = client_app.postRequest(test_trans, 'send')
        status = json.loads(response[-1])['status']
        trans = json.loads(response[-1])['transaction']
        assert status == 'ok' and test_trans['amount'] != trans['amount']

    def test_app_no_convert(self, app, mock_server, client_app):
        test_trans = {'id': 0,
                      'county': 'USA',
                      'emitent_curr': 'USD',
                      'emit_card': 111111111111,
                      'recieve_card': 2222222222,
                      'reciever_curr': 'USD',
                      'amount': 200}
        response = client_app.postRequest(test_trans, 'send')
        trans = json.loads(response[-1])['transaction']
        assert test_trans == trans

    def test_app_neg(self, app, mock_server, client_app):
        test_trans = {'id': 0,
                      'county': 'USA',
                      'emitent_curr': 'USD',
                      'emit_card': 111111111111,
                      'recieve_card': 2222222222,
                      'reciever_curr': 'RUB',
                      'amount': 200}
        response = client_app.postRequest(test_trans, 'send')
        status = json.loads(response[-1])['status']
        assert status == 'wrong reciever currency'
         
    '''Предложенные Ярославом тесты'''

    def test_app_to_inactive_mock(self, app, mock_server, client_app):
        response = client_app.getRequest('mockdown')
        assert '"Mock is down"' in response

    def test_app_mock_timeout(self, app, mock_server, client_app):
        response = client_app.getRequest('timeout')
        assert '"Timeout error"' in response

    def test_app_mock_internal(self, app, mock_server, client_app):
        response = client_app.getRequest('bank')
        assert '"Internal server error"' in response

    def test_app_auth_ok(self, app, mock_server, client_app):
        response = client_app.getRequest('history', 'clementine')
        status = int(response[0].split(' ')[1])
        assert status == 200

    def test_app_auth_neg(self, app, mock_server, client_app):
        response = client_app.getRequest('history', 'Sara')
        assert '"Wrong username"' in response

    def test_app_auth_no_header(self, app, mock_server, client_app):
        response = client_app.getRequest('history')
        assert '"No auth header"' in response


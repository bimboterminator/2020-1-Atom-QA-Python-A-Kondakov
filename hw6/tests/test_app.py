from mock_server.http_mock import MockHTTPServer
from application import converter
from sock.client_socket import SocketClient
import pytest
import requests
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

    @pytest.fixture(scope='function')
    def client_mock(self):
        socket = SocketClient(MOCK_HOST, MOCK_PORT)
        return socket

    @pytest.fixture(scope='function')
    def client_app(self):
        socket = SocketClient(APP_HOST, APP_PORT)
        return socket

    def test_mock_post_ok(self, app, mock_server, client_app):
        test_trans = {'id': 0,
            'county':'USA',
            'emitent_curr':'USD',
            'emit_card':111111111111,
            'recieve_card':2222222222,
            'reciever_curr':'EUR',
            'amount': 200}
        response = client_app.postRequest(test_trans, 'send')
        print(response)
        assert test_trans in response

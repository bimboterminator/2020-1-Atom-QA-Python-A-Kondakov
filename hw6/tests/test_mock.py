from mock_server.http_mock import MockHTTPServer
from sock.client_socket import SocketClient
import pytest


MOCK_HOST, MOCK_PORT = '127.0.0.1', 1050


class TestMockServer:

    @pytest.fixture(scope='session')
    def mock_server(self):
        server = MockHTTPServer(MOCK_HOST, MOCK_PORT)
        server.start()
        yield server
        server.stop()

    @pytest.fixture(scope='session')
    def client(self):
        socket = SocketClient(MOCK_HOST, MOCK_PORT)
        return socket

    def test_mock_post_ok(self, mock_server, client):
        test_trans = {'id': 0, 'county': 'USA', 'currency': 'USD', 'sum': 200}
        response = client.postRequest(test_trans, 'usd')
        assert test_trans in response[-2]

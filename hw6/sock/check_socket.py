from mock_server.http_mock import MockHTTPServer
from sock.client_socket import SocketClient
import json

target_host = "127.0.0.1"
target_port = 1050
testdata = {'id': 0,
            'text': 'test task'}

data = json.dumps(testdata)

server = MockHTTPServer(target_host, target_port)
server.start()
client = SocketClient(target_host, target_port)
test_trans = {'id': 0, 'county': 'USA', 'currency': 'USD', 'sum': 200}
response = client.postRequest(test_trans, 'usd')
server.stop()
print(response)
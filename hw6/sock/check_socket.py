from mock_server.http_mock import MockHTTPServer
from sock.client_socket import SocketClient
import json
import requests
from application import converter
import settings
target_host = "127.0.0.1"
target_port = 1050
testdata = {'id': 0,
            'text': 'test task'}

data = json.dumps(testdata)
converter.run_app()
server = MockHTTPServer(target_host, 1052)
server.start()
client = SocketClient(target_host, 1050)
test_trans = {'id': 0,
            'county': 'USA',
            'emitent_curr': 'USD',
            'emit_card': 111111111111,
            'recieve_card': 2222222222,
            'reciever_curr': 'EUR',
            'amount': 200}

#requests.post(settings.APP_POST_URL, json=test_trans)

response = client.postRequest(test_trans, 'send')

server.stop()
requests.get(settings.APP_SHUTDOWN_URL)
print(response)
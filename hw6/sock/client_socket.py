import socket
import json


class SocketClient:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def getRequest(self, params=''):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))
        client.settimeout(0.3)
        request = f'GET /{params} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'
        client.send(request.encode())
        total_data = []
        while True:
            # читаем данные из сокета до тех пор пока они там есть
            data = client.recv(1024)
            if data:
                total_data.append(data.decode())
            else:
                break
        client.close()
        return ''.join(total_data).splitlines()

    def postRequest(self, data, params=''):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))
        client.settimeout(0.3)
        post_data = json.dumps(data)
        request = f'POST /{params} HTTP/1.1\r\nHost:{self.host}\r\nContent-Type: application/json\r\nContent-Length:{len(post_data.encode())}\r\n\r\n{post_data}'
        client.send((request.encode()))
        total_data = []
        while True:

            data = client.recv(1024)
            if data:
                total_data.append(data.decode())
            else:
                break
        client.close()
        return ''.join(total_data).splitlines()


import socket
import json


class SocketClient:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = None

    def getRequest(self, params='', user=None):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.client.settimeout(2)
        if user:
            request = f'GET /{params} HTTP/1.1\r\nHost:{self.host}\r\nAuthorization: {user}\r\n\r\n'
        else:
            request = f'GET /{params} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'
        self.client.send(request.encode())
        total_data = []
        try:
            while True:
            # читаем данные из сокета до тех пор пока они там есть
                data = self.client.recv(1024)
                if data:
                    total_data.append(data.decode())
                else:
                    break
            answ = ''.join(total_data).splitlines()
            self.client.close()
            return answ
        except socket.timeout:
            self.client.close()
            return {'status': '408 request timeout'}



    def postRequest(self, data, params=''):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.client.settimeout(0.5)
        post_data = json.dumps(data)
        request = f'POST /{params} HTTP/1.1\r\nHost:{self.host}\r\nContent-Type: application/json\r\nContent-Length:{len(post_data.encode())}\r\n\r\n{post_data}'
        self.client.send((request.encode()))
        total_data = []
        try:
            while True:
                # читаем данные из сокета до тех пор пока они там есть
                data = self.client.recv(1024)
                if data:
                    total_data.append(data.decode())
                else:
                    break
            answ = ''.join(total_data).splitlines()
            self.client.close()
            return answ
        except socket.timeout:
            self.client.close()
            return {'status': '408 request timeout'}


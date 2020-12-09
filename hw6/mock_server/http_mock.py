import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import time

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    usd = []
    eur = []
    users = ['clementine', 'dunkan']

    def _set_headers(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/timeout':
            time.sleep(1)
        if self.path == '/ok':
            self.send_response(500)
            self._set_headers()
        if self.path == '/hist':
            login = self.headers['Authorization']
            if login:
                if str(login) in self.users:
                    self.send_response(200)
                    self.send_header('Authorization', f'{login}')
                    self._set_headers()
                    self.wfile.write(json.dumps({'usd': self.usd, 'eur': self.eur}).encode())
                else:
                    self.send_response(403)
                    self._set_headers()
            else:
                self.send_response(400)
                self._set_headers()



    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        trans = json.loads(post_data.decode())
        if trans['reciever_curr'] == 'EUR' and self.path == '/usd':
            self.send_response(403)
            self.wfile.write(json.dumps({'Invalid currency': trans['reciever_curr'], 'received': 'no'}).encode())

        if self.path == '/usd' and trans['reciever_curr'] == 'USD':
            self.send_response(200)
            self.usd.append(trans)
        if self.path == '/eur' and trans['reciever_curr'] == 'EUR':
            self.send_response(200)
            self.eur.append(trans)

        self.send_response(200)
        self._set_headers()

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        trans = json.loads(put_data.decode())
        if self.path != '/usd' or self.path != '/eur':
            self.send_response(405)
            self.wfile.write("Method not allowed".encode())

        elif self.path == '/usd':
            self.send_response(200)
            self.usd.clear()
            self.usd.append(trans)
            self._set_headers()
        elif self.path == '/eur':
            self.send_response(200)
            self.eur.clear()
            self.eur.append(trans)
            self._set_headers()
        self.wfile.write(json.dumps({'usd': self.usd, 'eur': self.eur}).encode())


class MockHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = SimpleHTTPRequestHandler
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever, daemon=True)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()



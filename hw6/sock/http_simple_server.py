import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    data = None

    def _set_headers(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.data:
            self.wfile.write(self.data)
        else:
            self.wfile.write('Nothing new'.encode())

    def do_POST(self):
        self._set_headers()
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        self.data = body
        print(self.path)

class SimpleHTTPServer:
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



import socketserver
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from examples2 import allFunc

PORT = 80

class Request_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        population_argument = query_components["population"]
        second_argument = query_components["b"]
        third_argument = query_components["c"]

        allFunc(population_argument, second_argument, third_argument)

        self.wfile.write(bytes(message, "utf8"))
        return

class Server():
    def __init__(self):
        pass

    def run(self):
        with socketserver.TCPServer(("", PORT), Request_handler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()

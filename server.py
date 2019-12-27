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
        
        try:
            query = str(urlparse(self.path).query)
            query_components = dict(qc.split("=") for qc in query.split("&"))
        except Exception as e:
            return

        population_argument = int(query_components["population"])
        second_argument = int(query_components["b"])
        third_argument = float(query_components["c"])

        # print(query_components)

        allFuncDic = dict()
        allFuncDic = allFunc(population_argument, second_argument, third_argument)

        for val in allFuncDic.values():
            print(val)
            # return val

        self.wfile.write(bytes(str(allFuncDic), "utf8"))
        return


class Server():
    def __init__(self):
        pass

    def run(self):
        with socketserver.TCPServer(("", PORT), Request_handler) as httpd:
            print("serving a port", PORT)
            httpd.serve_forever()

import socketserver
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from examples import allFunc

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
        neighbors_argument = int(query_components["neighbors"])
        probability_argument = float(query_components["probability"])
        algorithm_argument = str(query_components["algorithm"])

        allFuncDic = dict()
        allFuncDic = allFunc(population_argument, neighbors_argument, probability_argument)


        self.wfile.write(bytes(str(allFuncDic[algorithm_argument]), "utf8"))
        return


class Server():
    def __init__(self):
        pass

    def run(self):
        with socketserver.TCPServer(("", PORT), Request_handler) as httpd:
            print("serving a port", PORT)
            httpd.serve_forever()

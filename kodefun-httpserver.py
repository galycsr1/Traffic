

#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

import os

def getFrames(text_http):
    return text_http

#Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
 
    #handle GET command
    def do_GET(self):    
        try:     
            params = parse_qs(urlparse(self.path).query)
            func = ROUTES.get(params.route, 'unknown_route')
            response = func(params.input)

            #send code 200 response
            self.send_response(200)

            #send header first
            self.send_header('Content-type','text-html')
            self.end_headers()
            #print(self)
            #print(self.path)
            #print(str(self.rfile()))
            #send file content to client
            #data = foo(str(self.rfile()))
            #self.wfile.write(data, "utf8")
            self.wfile.write(reponse, "utf8")
            return
            
        except IOError:
            self.send_error(404, 'file not found')
    
def run():
    print('http server is starting...')

    #ip and port of servr
    #by default http server port is 80
    server_address = ('132.73.198.188', 8080)
    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()

ROUTES = { 'getFrames': getFrames }

if __name__ == '__main__':
    run()
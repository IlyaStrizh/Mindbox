from http.server import BaseHTTPRequestHandler, HTTPServer
from socket import gethostname
import os
import uuid

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/hostname':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            hostname = os.environ.get('HOSTNAME', str(gethostname()))
            self.wfile.write(bytes(hostname, "utf-8"))
            
        elif self.path == '/author':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            author = os.environ.get('AUTHOR', 'Ilya')
            self.wfile.write(bytes(author, "utf-8"))
            
        elif self.path == '/id':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            uid = os.environ.get('UUID', str(uuid.uuid4()))
            self.wfile.write(bytes(uid, "utf-8"))
            
        else:
            self.send_error(404, 'Not Found')

def run():
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, MyServer)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

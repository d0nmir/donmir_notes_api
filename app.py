import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello! Welcome to Notes API.")
            
        elif self.path == '/healthz':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"OK")
            
        elif self.path == '/notes':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            notes = [
                {"id": 1, "title": "First note"},
                {"id": 2, "title": "Second note"}
            ]
            self.wfile.write(json.dumps(notes).encode('utf-8'))
            
        else:
            self.send_response(404)
            self.end_headers()

def run():
    port = int(os.environ.get('PORT', 8080))
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
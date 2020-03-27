import http.server
import socketserver

PORT = 8080
HOST = "0.0.0.0"
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

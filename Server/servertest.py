from http.server import HTTPServer, BaseHTTPRequestHandler 
# import ssl
from OpenSSL import SSL
print(SSL._CERTIFICATE_PATH_LOCATIONS)
# httpd = HTTPServer(('localhost', 4443), BaseHTTPRequestHandler)
# httpd.socket = ssl.wrap_socket(
#     httpd.socket,
#     keyfile="path/to/key.pem",
#     certfile='path/to/cert.pem',
#     server_side=True)
# httpd.serve_forever()
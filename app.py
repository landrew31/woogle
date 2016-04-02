import socket
import ssl

HOST = "www.wikipedia.org"

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname=HOST)
ssl_sock.connect((HOST, 443))
packet = "GET / HTTP/1.1\nHost: " + HOST + "\n\n"
ssl_sock.send(packet.encode())

print(ssl_sock.recv(1024))
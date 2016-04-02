import socket
import ssl

# SET VARIABLES
HOST, PORT = 'www.wikipedia.org', 443
packet, reply = "GET / HTTP/1.1\nHost: " + HOST + "\n", ""


# CREATE SOCKET
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(8)

# WRAP SOCKET

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

wrappedSocket = context.wrap_socket(sock, server_hostname=HOST)

# CONNECT AND PRINT REPLY
wrappedSocket.connect((HOST, PORT))
wrappedSocket.send(packet)
print wrappedSocket.recv(1280)

# CLOSE SOCKET CONNECTION
wrappedSocket.close()
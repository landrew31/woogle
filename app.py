import socket
import ssl
import re

HOST = "ru.wikipedia.org"

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
ssl_sock = context.wrap_socket(s, server_hostname=HOST)
ssl_sock.connect((HOST, 443))
packet = "GET /wiki/%D0%9A%D0%B0%D0%BB HTTP/1.1\nHost: " + HOST + "\n\n"
ssl_sock.send(packet)
End='</html>'
def recv_end(the_socket):
    total_data=[];data=''
    while True:
            data=the_socket.recv(8192)
            if End in data:
                total_data.append(data)
                break
            total_data.append(data)
            if len(total_data)>1:
                #check if end_of_data was split
                last_pair=total_data[-2]+total_data[-1]
                if End in last_pair:
                    total_data[-2]=last_pair[:last_pair.find(End)]
                    total_data.pop()
                    break
    return ''.join(total_data)
res = recv_end(ssl_sock)    
print len(re.findall('href="(/wiki[^\"]*)"', res))
s.close()


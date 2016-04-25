import socket
import ssl
import re

HOST = "en.wikipedia.org"
End = '</html>'



def create_connection():
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10) 
    ssl_sock = context.wrap_socket(s, server_hostname=HOST)
    ssl_sock.connect((HOST, 443))
    return ssl_sock

def recv_end(the_socket):
    total_data=[];data=''
    while True:
            data=the_socket.recv(4096)
            data = re.sub("^[0-9abcdef]{1,4}"+ chr(13)+"\n", '', data)
            data = re.sub("\r\n", '', data)
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


def getHtml(socket, url):
    packet = "GET " + url + " HTTP/1.1\nHost: " + HOST + "\n\n"   
    try: 
        socket.send(packet) 
        res = recv_end(socket)
    except:
        socket.close()
        raise Exception('Lost connection')  

    return res

def getUrls(html):
    return list(set(re.findall('href="(/wiki/[^\":#]*)"', html)))

  
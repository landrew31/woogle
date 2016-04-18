import socket
import ssl
import re

HOST = "en.wikipedia.org"
End = '</html>'





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


def getHtml(url):
    packet = "GET " + url + " HTTP/1.1\nHost: " + HOST + "\n\n"   
    try: 
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.verify_mode = ssl.CERT_REQUIRED
        context.check_hostname = True
        context.load_default_certs()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "create"
        s.settimeout(10) 
        ssl_sock = context.wrap_socket(s, server_hostname=HOST)
        print "wrap"
        ssl_sock.connect((HOST, 443))
        print "connect"
        ssl_sock.send(packet) 
        print "send" 
        res = recv_end(ssl_sock)
        s.close()
        context.remove()
    except:
        res = 'not found'    

    return res

def getUrls(html):
    return list(set(re.findall('href="(/wiki/[^\":#]*)"', html)))

  
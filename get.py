import socket
import ssl
from urllib.parse import urlparse
def get(url):
    
    p = urlparse(url)
    #print(p.path)
    if p.scheme=="https":
        if p.port:
            port=p.port
        else:
            port = 443
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((p.hostname,port))
        context = ssl.create_default_context()
        connection = context.wrap_socket(sock,server_hostname=p.hostname)
        path = p.path or "/"
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {p.hostname}\r\n"
            "Connection: close\r\n"
            "\r\n"
        )
        response = b""
        connection.sendall(request.encode())
        while True:
            data = connection.recv(4096)
            if not data:
                break
            response = response+data
        print(response.decode())
        connection.close()
    elif p.scheme=="http":
        if p.port:
            port = p.port
        else:
            port = 80
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((p.hostname,port))
        connection=sock
        path = p.path or "/"
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {p.hostname}\r\n"
            "Connection: close\r\n"
            "\r\n"
        )
        response = b""
        connection.sendall(request.encode())
        while True:
            data = connection.recv(4096)
            if not data:
                break
            response = response+data
        print(response.decode())
        connection.close()
    elif p.scheme=="":
        raise ValueError("No scheme provided, expected http or https")
    else:
        raise ValueError("Invalid or unexpected scheme")

get("https://example.com/") 

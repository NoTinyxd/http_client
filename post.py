import socket
import ssl
from urllib.parse import urlparse
def post(url,body,header):
    
    p = urlparse(url)
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

        body = body.encode()
        request = (
            f"POST {path} HTTP/1.1\r\n"
            f"Host: {p.hostname}\r\n"
        )
        for header_name,header_value in header.items():
            request=request+f"{header_name}: {header_value}\r\n"
        request = request + (
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n"
        "\r\n")

        request=request.encode()+body
        response = b""
        connection.sendall(request)
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
        body = body.encode()
        request = (
            f"POST {path} HTTP/1.1\r\n"
            f"Host: {p.hostname}\r\n"
        )
        for header_name,header_value in header.items():
            request=request+f"{header_name}: {header_value}\r\n"
        request = request + (
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n"
        "\r\n")

        request=request.encode()+body
        response = b""
        connection.sendall(request)
        

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

import socket
import ssl
from urllib.parse import urlparse
def get(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://"+url #for now supports only https
    p = urlparse(url)

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((p.hostname,443))
    context = ssl.create_default_context()

    s = context.wrap_socket(sock,server_hostname=p.hostname)
    request = (
        f"GET / HTTP/1.1\r\n"
        f"Host: {p.hostname}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    s.sendall(request.encode())
    response = b""
    while True:
        data=s.recv(4096)
        if not data:
            break
        response = response+data
    print(response.decode())
    s.close()
get("google.com") # Default to HTTPS if no protocol is specified (HTTP not yet supported).

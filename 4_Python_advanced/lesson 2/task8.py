import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def custom_connect(data, url="example.com", method="GET / HTTP/1.1"):

    sock.connect((url, 80))
    request = method + "\n" + data
    print('--- HTTP MESSAGE ---')
    print(request)
    print('--- END OF MESSAGE ---')

    sock.send(request.encode())

    result = sock.recv(10024)

    print(result.decode())

content_items = 'Host: example.com\nConnection: keep-alive\nAccept: text/html\n\n'

#custom_connect(data=content_items)

my_url = input("Enter url: ")
custom_connect(data=content_items, url=my_url)

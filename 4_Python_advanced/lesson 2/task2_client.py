import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(b'1863MSI', ('127.0.0.1', 8888))
import os
import socket

SERVER_FILE = 'unix_server.sock'
CLIENT_FILE = 'unix_client.sock'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(SERVER_FILE):
    os.remove(SERVER_FILE)

sock.bind(SERVER_FILE)

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        numbers = (result.decode('utf-8')).split(',')
        integers = map(int, numbers)
        message = str(sum(integers))
        sock.sendto(str.encode(message), CLIENT_FILE)

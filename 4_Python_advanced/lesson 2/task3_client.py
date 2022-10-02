import socket
import os

SERVER_FILE = 'unix_server.sock'
CLIENT_FILE = 'unix_client.sock'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(CLIENT_FILE):
    os.remove(CLIENT_FILE)

sock.bind(CLIENT_FILE)

sock.sendto(b'2,3', SERVER_FILE)

result = sock.recv(1024)
sock.close()
print("The SUM is:", result.decode('utf-8'))

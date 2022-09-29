import time, socket, sys

print("Chat Server v0.01")

sock = socket.socket()
guest = socket.gethostname()
ip = socket.gethostbyname(guest)
print(guest, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("Enter your name: "))
port = 8888
print("Trying to connect...\n")
sock.connect((host, port))
print("Connected...\n")

sock.send(name.encode())
s_name = sock.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter 'exit' to exit chat room\n")

while True:
    message = sock.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me : "))
    if message.lower() == "exit":
        message = "Left chat room!"
        sock.send(message.encode())
        print("\n")
        break
    sock.send(message.encode())
import socket

print("Chat Server v0.01")

sock = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 8888
sock.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))

sock.listen(1)
print("Waiting for incoming connections...\n")
client, addr = sock.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

client_name = client.recv(1024)
client_name = client_name.decode()
print(client_name, "has connected to the chat room\nEnter 'exit' to exit chat room\n")
client.send(name.encode())

while True:
    message = input(str("Me : "))
    if message.lower() == "exit":
        message = "Left chat room!"
        client.send(message.encode())
        print("\n")
        break
    client.send(message.encode())
    message = client.recv(1024)
    message = message.decode()
    print("<" + client_name + "> " + message)

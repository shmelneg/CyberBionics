import asyncio
import socket


async def handle_client(client):
    loop = asyncio.get_event_loop()
    while True:
        new_id = (await loop.sock_recv(client, 255)).decode('utf8')
        print("I've got a new ID")
        response = 'I confirm that I have received your ID'
        await loop.sock_sendall(client, response.encode('utf8'))
        if new_id == "exit":
            break
    client.close()


async def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8888))
    print('Server started and waiting for new IDs...')
    server.listen(8)
    server.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))


asyncio.run(run_server())

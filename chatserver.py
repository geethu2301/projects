import socket
import threading
host = '127.0.0.1'
port = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen(5)
clients = []
nicknames = []
def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            clients.remove(client)
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} left the chat!'.encode('utf-8'))
                clients.remove(client)
                nicknames.remove(nickname)
            break
def receive_connections():
    print("Server running...")
    while True:
        client, addr = server.accept()
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        clients.append(client)
        nicknames.append(nickname)
        print(f"{nickname} connected from {addr}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
receive_connections()

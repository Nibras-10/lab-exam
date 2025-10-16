import socket
import threading

HOST, PORT = '127.0.0.1', 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

print(f"Server started on {HOST}:{PORT}")

# Send message to all connected clients
def broadcast(msg, sender=None):
    for c in clients:
        if c != sender:
            try:
                c.send(msg)
            except:
                pass

# Handle individual client
def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            broadcast(msg, sender=client)
        except:
            break

    # Remove disconnected client
    if client in clients:
        idx = clients.index(client)
        uname = usernames[idx]
        print(f"{uname} disconnected.")
        broadcast(f"{uname} left the chat.".encode())
        clients.remove(client)
        usernames.remove(uname)
        client.close()

# Accept new clients
def accept_clients():
    while True:
        client, addr = server.accept()
        print(f"Connected with {addr}")

        client.send("USERNAME".encode())
        uname = client.recv(1024).decode()

        usernames.append(uname)
        clients.append(client)

        print(f"{uname} joined the chat.")
        broadcast(f"{uname} joined the chat.".encode())
        client.send("Connected to the chat server!".encode())

        threading.Thread(target=handle, args=(client,), daemon=True).start()

accept_clients()

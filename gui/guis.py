import socket
import threading

HOST='127.0.0.1'
PORT=8080

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print(f'Server is running on {HOST}:{PORT}')

clients=[]
usernames=[]

def broadcast(msg,sender=None):
    for c in clients:
        if c!=sender:
            try:
                c.send(msg)
            except:
                pass

def handle(client):
    while True:
        try:
            msg=client.recv(1024)
            if not msg:
                break
            broadcast(msg,sender=client)
        except:
            break
    
    if client in clients:
        idx=clients.index(client)
        uname=usernames[idx]
        print(f'{uname} is disconnected')
        broadcast(f'{uname} has left the chat'.encode())
        clients.remove(client)
        usernames.remove(uname)
        client.close()

def accept_clients():
    while True:
        client,addr=server.accept()
        print(f'connected with {addr}')

        client.send('USERNAME'.encode())
        uname=client.recv(1024).decode()

        usernames.append(uname)
        clients.append(client)

        print(f'{uname} joined the chat')
        broadcast(f'{uname} has joined the chat'.encode())
        client.send(f'{uname}has joined the chat'.encode())
        threading.Thread(target=handle,daemon=True,args=(client,)).start()

accept_clients()



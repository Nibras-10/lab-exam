import socket

HOST='127.0.0.1'
PORT=8080

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print(f'Server listening on {HOST}:{PORT}')

conn,addr=server.accept()
print(f'Connected by {addr}')

while True:
    msg=conn.recv(1024).decode()
    if not msg:
        break
    
    print(f'client: {msg}')
    reply=input('server: ')
    conn.send(reply.encode())

conn.close()
server.close()


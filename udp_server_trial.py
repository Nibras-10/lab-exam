import socket

HOST='127.0.0.1'
PORT=8080

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((HOST,PORT))
print(f'Server started at {HOST}: {PORT}')
while True:
    data,addr=server_socket.recvfrom(1024)
    message=data.decode()
    print(f'Client says: {message}')
    if not message or message.lower()=='exit':
        print('Shutting down server')
        break
    reply=input('Server: ')
    server_socket.sendto(reply.encode(),addr)



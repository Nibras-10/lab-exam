import socket

IP='127.0.0.1'
PORT=8080
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((IP,PORT))
print(f'server started at {IP}: {PORT}')
while True:
    data,addr=server_socket.recvfrom(1024)
    message=data.decode()
    print('Client:',message)
    if message.lower()=='exit':
        print('Server exiting...')
        server_socket.sendto('Server shutting down...'.encode(),addr)
        break
    reply=input('Your reply: ')
    server_socket.sendto(reply.encode(),addr)
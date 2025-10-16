import socket

HOST='127.0.0.1'
PORT=8080

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
    while True:
        message=input('Client: ')
        if not message or message.lower()=='exit':
            print('Client shutting down')
            break
        client_socket.sendto(message.encode(),(HOST,PORT))
        ass,server_message=client_socket.recvfrom(1024)
        print(f'Server says: {ass.decode()}')
finally:
    client_socket.close()


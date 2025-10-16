import socket

IP = '127.0.0.1'
PORT = 8080

client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        message=input('You: ')
        client_socket.sendto(message.encode(),(IP,PORT))
        data,addr=client_socket.recvfrom(1024)
        print('Server:',data.decode())
        if message.lower()=='exit':
            break
finally:
    client_socket.close()


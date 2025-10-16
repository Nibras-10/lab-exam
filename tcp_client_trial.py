import socket

HOST='127.0.0.1'
PORT=8080

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print(f'Client connected at {HOST}: {PORT}')
    while True:
        message=input('Client: ')
        if not message or message.lower()=='exit':
            s.sendall(b'Client exited')
            break
        s.sendall(message.encode())
        data=s.recv(1024)
        print(f'Server says: {data.decode()}')
print('Client shutdown correctly.......')
import socket

HOST='127.0.0.1'
PORT=8080

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print(f'Server is listening on {HOST}: {PORT}')
    conn,addr=s.accept()
    with conn:
        print(f'connected with {addr}')
        while True:
            data=conn.recv(1024)
            message=data.decode()
            if not message or message.lower()=='exit':
                print('server shutting down')
                break
            print(f'Client says: {message}')
            reply=input('Server: ')
            if not reply or reply.lower()=='exit':
                conn.sendall(b'exit')
                print('Server shutting down....')
                break
            conn.sendall(reply.encode())
print('Server shutdown succesfully')

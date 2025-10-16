import socket

HOST = '127.0.0.1'  # Server address
PORT = 65432        # Server port


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to TCP server at {HOST}:{PORT}")
    while True:
        message = input("Client: Enter message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            s.sendall(b'exit')
            break
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Server: {data.decode()}")
print("Connection closed.")

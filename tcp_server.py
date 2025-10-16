import socket

HOST = '127.0.0.1'  # Listen on localhost
PORT = 65432        # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"TCP server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data or data.decode().lower() == 'exit':
                print("Client disconnected.")
                break
            print(f"Client: {data.decode()}")
            reply = input("Server: Enter message to send to client (or 'exit' to quit): ")
            if reply.lower() == 'exit':
                conn.sendall(b'exit')
                print("Server disconnected.")
                break
            conn.sendall(reply.encode())
print("Server connection closed.")

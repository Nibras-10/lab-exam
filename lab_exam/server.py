from pyspark import SparkContext
import socket

HOST = '127.0.0.1'
PORT = 65432

# Start Spark
sc = SparkContext("local", "PalindromeServer")

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server started at {HOST}:{PORT}")

conn, addr = server.accept()
print(f"Connected with {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'exit':
        print("Client disconnected.")
        break

    print(f"Received text: {data}")

    # Split text and find palindromes using Spark RDD
    words = data.split()
    rdd = sc.parallelize(words)
    palindromes = rdd.filter(lambda w: w.lower() == w[::-1].lower()).collect()

    response = f"Palindrome count: {len(palindromes)}\nWords: {', '.join(palindromes) if palindromes else 'None'}"
    conn.send(response.encode())

conn.close()
server.close()

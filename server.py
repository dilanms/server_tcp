import socket
import os

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST, PORT = "0.0.0.0", 8081
server_sock.bind((HOST, PORT))
server_sock.listen(5)
while True:
    sock, addr = server_sock.accept()
    data = sock.recv(1024)  # Receive
    data = data.upper()  # Process bytes
    sock.sendall(data)  # Send


import socket

HOST = '0.0.0.0'
#HOST = socket.gethostbyname('socket-server_dns_name')
PORT = 5052


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Server Started")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print("Client sent: ", data)
            if not data:
                break
            conn.sendall(data)
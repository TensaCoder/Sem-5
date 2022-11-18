import socket

host = socket.gethostname()
port = 5000

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
conn, address = server_socket.accept()
print("Connection from: " + str(address))

while True:

    data = conn.recv(1024).decode()
    if not data:

        break
    print("From client: " + str(data))
    data = input('Server: ')
    conn.send(data.encode())

conn.close()

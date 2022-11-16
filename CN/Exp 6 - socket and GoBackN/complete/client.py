import socket


host = socket.gethostname()
port = 5000

client_socket = socket.socket()
client_socket.connect((host, port))

message = input("Client: ")  # take input

while message.lower().strip() != 'bye':
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from server: ' + data)  # show in terminal

    message = input("Client: ")

client_socket.close()  # close the connection

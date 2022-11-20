# Receiver.py
import time
import socket
import sys
import random

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
# host = input(str("Enter server address: "))
host = "localhost"
# name = input(str("\nEnter your name: "))
name = "recv"
port = 5554
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

while True:

    m = s.recv(1024)
    m = m.decode()

    lenOfMessage = s.recv(1024)
    lenOfMessage = lenOfMessage.decode()
    lenOfMessage = int(lenOfMessage)

    lenOfWindow = s.recv(1024)
    lenOfWindow = lenOfWindow.decode()
    print("Window size : ", lenOfWindow)
    lenOfWindow = int(lenOfWindow[0])

    print("Message : ", m)
    print("Length of message : ", lenOfMessage)
    print("Length of window : ", lenOfWindow)

    receiverFrame = 0           #Current frame for which ACK hasnt been sent
    lastReceivedFrame = 0       # Last frame of the window
    a = ""
    b = ""
    # f = random.randint(0, 1)
    message = ""
    while lastReceivedFrame != lenOfMessage:

        # receive the first window content
        if lastReceivedFrame == 0:
            time.sleep(1)
            for j in range(0, lenOfWindow):
                if lastReceivedFrame == lenOfMessage:
                    break
                print("line 62")
                message = s.recv(1024)
                message = message.decode()
                a = a + message
                lastReceivedFrame = lastReceivedFrame + 1
                time.sleep(1)
                print("Receiving the first window content : frame ", j)
            print("Received message : ", a)


        f = random.randint(receiverFrame, lastReceivedFrame)
        b = "ACK "+str(f)
        s.send(b.encode())
        receiverFrame = f+1
        
        time.sleep(1)
        message = s.recv(1024)
        message = message.decode()
        print("Received frame : ", message)

        if message == "[e]":
            print("\n")
            break
        # f = random.randint(0, 1)
        # if (f == 0):
        #     b = "ACK Lost"
        #     # message = s.recv(1024)
        #     # message = message.decode()
        #     s.send(b.encode())

        # elif (f == 1):
        #     b = "ACK "+str(i)
        #     message = s.recv(1024)
        #     message = message.decode()

        #     s.send(b.encode())
        #     a = a+message
        #     i = i+1

    print("The message received is :", m)
    print("The message received after decoding is :", a)

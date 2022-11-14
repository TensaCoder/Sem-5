import socket 
import time
from random import *
import timeit
HOST = 'localhost'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)


connection, addr = s.accept()
s.settimeout(10.0)
print('Connection established.')
m = int(input("Enter the size of sliding window: "))
Sw = 2**m-1
Sf = 0
Sn = 0
total_frames = int(input("Enter number of frames to be sent: "))
seq = [str(i) for i in range(total_frames)]
connection.send(bytes(str(m), "utf-8"))
# m = bytes(str(m))
# connection.send(m.encode())
ack = connection.recv(512).decode("utf-8")
# ack = connection.recv(512)
# ack = ack.decode()


while True:
    if Sf == total_frames:
        connection.send(bytes("End", "utf-8"))
        print("All Frames transmitted")
        break
    sent = randint(0, 1)
    if Sn-Sf < Sw and Sn < total_frames:
        if sent == 1:
            start = timeit.default_timer()
            connection.send(bytes(seq[Sn], "utf-8"))
            print("Frame", int(seq[Sn]) % (Sw+1), "Sent")
            Sn += 1
            ack = connection.recv(512).decode("utf-8")
            if ack != "Lost ACK" and ack != "No ACK":
                if int(ack) > Sf and int(ack) <= Sn: 
                    print("Ack", int(ack) % (Sw + 1), "received")
                    while Sf < int(ack):
                        Sf += 1
            stop = timeit.default_timer()
            print("Transmission Time: "+str(stop-start)+' ms')
        else:
            connection.send(bytes("Frame Lost", "utf-8"))
            print("Frame", int(seq[Sn]) % (Sw + 1), "Lost")
            Sn += 1
    else:
        print("Timeout!Resending the frames again")
        for i in range(Sf, Sn):
            print("Frame", int(seq[i]) % (Sw + 1), "resent")
            connection.send(bytes("R"+seq[Sf], "utf-8"))
            Sf += 1
            ack = connection.recv(512).decode("utf-8")
            if ack != "No ACK":
                print("Ack", int(ack) % (Sw + 1), "received")
                while Sf < int(ack):
                    Sf += 1
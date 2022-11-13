import socket
import time
from random import *

HOST = 'localhost'
PORT = 9999
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.settimeout(10.0)
m= int(s.recv(512).decode("utf-8"))
# m = s.recv(512)
# m = int(m.decode())
# print("Size of sliding window: ", m)
window=2**m
s.send(bytes("Got m", "utf-8"))
Rn=0
while True:
    try:
        msg= s.recv(512).decode("utf-8")
    except:
        msg=""
        print("Sender didn't send frame")
    if msg=="End":
        print("All Frames received")
        break
    if not (msg == "Frame Lost" or msg == ""):
        if msg[0]=="R":
            msg=msg[1:]
            ack=1 
        else:
            ack=randint(0,1)
        if msg==str(Rn):
            print("Frame ",int(msg)%window,"received")
            Rn+=1
            if ack==1:
                print("Ack Sent")
                s.send(bytes(str(Rn),"utf-8"))
            else:
                print("Ack Lost")
                s.send(bytes("Lost ACK", "utf-8"))
        else:
            s.send(bytes("No ACK", "utf-8"))
            print("Frame ", int(msg)%window,"received but discarded since out of order")
            # print("Frame received but discarded since out of order")

            time.sleep(1)
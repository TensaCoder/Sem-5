import socket
import random
import time

def sendAcknowledgment(k):
    print("\nSending ACK for ", k)
    ack = input("Enter 1 to send ACK\nEnter 2 to not send ACK\n")
    # ack = str(random.randint(1,2))
    # if ack == '1':
    #     ack = '2'
    # else:
    #     ack = '1'
    # ack = "1"

    s.send(ack.encode())
    time.sleep(1)
    if ack == '2':
        print("Discarded Remaining Frames!\n\n")
        return k
    elif ack == '1':
        k = k+1
        return k
    else:
        return k


host = 'localhost'
# host = '10.0.4.236'
port = 4444


s = socket.socket()
s.connect((host, port))


window_size = s.recv(1024)
N = s.recv(1024)

k = 0

while True:
    frame = s.recv(1024)
    if frame.decode() == "Request":
        k = sendAcknowledgment(k)
        continue
    if frame.decode() == "All Sent":
        s.close()
        break
    if frame.decode().find("Request") == -1:
        print("Receiving frame ", frame.decode())
        print()

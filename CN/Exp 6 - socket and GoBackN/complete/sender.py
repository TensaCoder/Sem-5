import socket
import time


def waitingforAcknowlegment(i):
    ACK = "Request"
    print("Waiting for ACK for frame", i)
    print("\n\n")
    c.send(ACK.encode())
    ack = c.recv(1024)
    if ack.decode() == '1':
        return (1, k+1)
    else:
        return (0, k)


def sendFrames(k, n):
    for i in range(int(k), int(n)):
        if i < int(N):
            print("Sending frame ", i)
            print()
            c.send(str(i).encode())
            time.sleep(1)


def sendNextFrames(k):
    print("Sending frame ", k)
    print()
    c.send(str(k).encode())


def discardedFrames(k, n):
    for i in range(int(k), int(n)):
        if i < int(N):
            print("Discarded frame ", i)
            print()


host = 'localhost'
# host = '10.0.4.236'
port = 4444

msg = "All Sent"

s = socket.socket()
s.bind((host, port))
s.listen(1)
c, addr = s.accept()
print("Connection Established:", str(addr))


k = 0
N = input("Enter the no of frames: ")
window_size = input("Enter the window size: ")

c.send(str(window_size).encode())
c.send(str(N).encode())

sendFrames(k, window_size)

while True:

    (ack, k) = waitingforAcknowlegment(k)

    if ack == 0:
        print("Discarded Frames\n\n")
        discardedFrames(k, k+int(window_size))
        print("Re-Sending Frames\n\n")
        sendFrames(k, k+int(window_size))
    else:

        if (k+int(window_size)-1) < int(N):
            sendNextFrames(k+int(window_size)-1)
    if k == int(N):
        c.send(str(msg).encode())
        print("\n\nAll Frames are Transmitted Successfully")
        break

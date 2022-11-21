# Sender.py
import time
import socket
import sys


def decimalToBinary(n):
    return n.replace("0b", "")

def grouping(a):
    sendingBitsArray = []
    for i in range(0, len(a), 8):
        sendingBitsArray.append(a[i:i+8])
    return sendingBitsArray


def binarycode(s):
    a_byte_array = bytearray(s, "utf8")

    print(a_byte_array)
    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(decimalToBinary(binary_representation))

    # print(byte_list)
    # a = ""
    # for i in byte_list:
    #     a = a+i
    # return grouping(a)
    return byte_list

# message = input(str("Me : "))
# message = binarycode(input(str("Enter string : ")))
# print("Message : ", message)



print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 5554
s.bind((host, port))
print(host, "(", ip, ")\n")
# name = input(str("Enter your name: "))
name = 'send'

s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())

while True:
    message = input(str("Me : "))
    conn.send(message.encode())

    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break

    message = binarycode(message)
    print("Message : ", message)
    lenOfMessage = str(len(message))
    conn.send(lenOfMessage.encode())

    i = 0
    ackFrame = 0
    lenOfWindow = 0
    lenOfWindow = int(input("Enter the window size -> "))
    conn.send(str(lenOfWindow).encode())

    b = ""

    lenOfSenderWindow = lenOfWindow-1
    lenOfMessage = int(lenOfMessage)
    k = lenOfSenderWindow
    while i != lenOfMessage:

        #send the first window content
        for j in range(0, lenOfSenderWindow+1):
            if j == lenOfMessage:
                break
            b = message[j]
            conn.send(b.encode())
            print("Sent frame : ", j)
            i = i+1
            time.sleep(1)
        
        print("here")
        
        while (i != (lenOfMessage-lenOfSenderWindow)):
            print("here1")
            # time.sleep(1)
            # print("Message sent : ", message[i])
            # conn.send(str(message[i]).encode())
            b = conn.recv(1024)
            b = b.decode()
            print("Line 94 : ",b)

            b = int(b.replace("ACK ", ""))
            if b == 0:
                time.sleep(1)
                print("Acknowledgement Received! The sliding window is in the range " +
                      (str(i+1))+" to "+str(k+1)+" Now sending the next packet")
                i = i+1
                k = k+1
                conn.send(str(message[i]).encode())
                time.sleep(1)
                continue

            # for any value of b that is not 0
            time.sleep(1)
            print("Acknowledgement Received! The sliding window is in the range " +
                    (str(i+b))+" to "+str(k+b)+" Now sending the next packet")
            i = i+b
            k = k+b
            if i == lenOfMessage:
                break
            conn.send(str(message[i]).encode())
            time.sleep(1)

        while (i != lenOfMessage):
            b = conn.recv(1024)
            b = b.decode()
            print("Line 114 : ",b)
            b= int(b.replace("ACK ", ""))
            time.sleep(1)
            print("Acknowledgement Received! The sliding window is in the range " + (str(i+b)) + " to " + str(k+b) + " Now sending the next packet")
            i = i+b
            k = k+b
            if i >= lenOfMessage:
                break
            conn.send(str(message[i]).encode())
            time.sleep(1)







        #     if (b != "ACK Lost"):
        #         time.sleep(1)
        #         print("Acknowledgement Received! The sliding window is in the range " +
        #               (str(i+1))+" to "+str(k+1)+" Now sending the next packet")
        #         i = i+1
        #         k = k+1
        #         conn.send(str(message[i]).encode())
        #         time.sleep(1)
        #     else:
        #         time.sleep(1)
        #         print("Acknowledgement of the data bit is LOST! The sliding window remains in the range " +
        #               (str(i+1))+" to "+str(k+1)+" Now Resending the same packet")
        #         time.sleep(1)
            
            

        # while (i != lenOfMessage):
        #     # conn.send(message[i].encode())
        #     b = conn.recv(1024)
        #     b = b.decode()
        #     print("Line 112 : ",b)
        #     if (b != "ACK Lost"):
        #         time.sleep(1)
        #         print("Acknowledgement Received! The sliding window is in the range " +
        #               (str(i+1))+" to "+str(k)+" Now sending the next packet")
        #         i = i+1
        #         conn.send(str(message[i]).encode())
        #         time.sleep(1)
        #     else:
        #         time.sleep(1)
        #         print("Acknowledgement of the data bit is LOST! The sliding window remains in the range " +
        #               (str(i+1))+" to "+str(k)+" Now Resending the same packet")
        #         time.sleep(1)

print("Value of i : ", i)

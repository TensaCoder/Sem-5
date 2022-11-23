# first of all import the socket library
import socket			
# import numpy as np
import time

# next create a socket object
s = socket.socket()		
# print ("Socket successfully created")

# reserve a port on your computer in our case it is 12345 but it can be anything
port = 12344			

# Next bind to the port we have not typed any ip in the ip field instead we have inputted an empty string this makes the server listen to requests coming from other computers on the network
s.bind(('', port))		
print ("Socket bound :  %s" %(port))

# put the socket into listening mode
s.listen(5)	
print ("Listening...")		

# a forever loop until we interrupt it or an error occurs

# Establish connection with client.
c, addr = s.accept()	
print ('Connection received from : ', addr )

# send a thank you msg to the client. encoding to send byte type.
c.send('Connection established'.encode())

while True:
    # msg = input("Sender Msg : ")
    time.sleep(1)
    msg = "herschel menezes"
    c.send(msg.encode())

    if msg == "e":
        msg = "Server is ending the connection"
        c.send(msg.encode())
        print("\n")
        break

    f = str(len(msg))
    # c.send(f.encode())
   
    i=0
    window_size= 7 # The size of the window
    
    b=""
   
    window_size=window_size-1
    f=int(f)
    k=window_size

    while i!=f:
        c.send(msg[i].encode())
        b=c.recv(1024)
        b=b.decode()
        print("\n",b)
        if(b!="ACK Lost"):
            # time.sleep(1)
            split = b.split(" ")
            next = int(split[1])
            print("Acknowledgement Received! The sliding window is in the range "+(str(i+1))+" to "+str(k+next)+" Now sending the next packet")
            prev = i
            i=next
            k = k+(i-prev-1)
            # time.sleep(1)
        else:
            # time.sleep(1)
            print("Acknowledgement of the data bit is LOST! The sliding window remains in the range"+(str(i+1))+" to "+str(k))
            # time.sleep(1)
            i+=1
       
    print("\n")
        
    # Breaking once connection closed
    break

# Close the connection with the client
c.close()
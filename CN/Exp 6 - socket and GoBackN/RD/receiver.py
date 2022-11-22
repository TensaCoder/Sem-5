# Import socket module
import socket	
import random		

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 12344			

# connect to the server on local computer
s.connect(('127.0.0.1', port))

print (s.recv(1024).decode())   
# receive data from the server and decoding to get the string.

while True:
   m=s.recv(1024)
   m=m.decode()
   k=int(len(m))
   i=0
   ans=""
   b=""
   f=random.randint(0,1)
   message=""
   ack = 0

   while i!=k:
       
      # Acknowledgment sent for 3 and greater than 5
      if(i==3 or i>=5):
         b="ACK "+str(i)
         message = s.recv(1024)
         message = message.decode()
         print("Received Frame : ", i)
         
         s.send(b.encode())
         ans=ans+message
         # print("Received message :- ",ans)
         i=i+1
         print("Sending ACK for frame ", i)
         print()
      else:
         b="ACK Lost"
         message = s.recv(1024)
         message = message.decode()
         print("Received Frame : ", i)

         ans=ans+message
         # print("Received message :- ",ans)
         s.send(b.encode())
         i=i+1
         print("ACK Lost : ", i)
         print()
             
   print("The message received is :", m)
   break

 # f=random.randint(0,1)
      # if(f==0):
      #    b="ACK Lost"
      #    message = s.recv(1024)
      #    message = message.decode()
      #    s.send(b.encode())
         
      # elif(f==1):
      #    b="ACK "+str(i)
      #    message = s.recv(1024)
      #    message = message.decode()
         
      #    s.send(b.encode())
      #    a=a+message
      #    i=i+1

# close the connection
s.close()	
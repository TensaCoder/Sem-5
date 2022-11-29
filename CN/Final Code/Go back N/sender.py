import socket
import sys
import time

def prepare_frames(s: str, m: int):
    x = list(enumerate([*s]))
    y = [(b, str(a), str(a%(2**m))) for a, b in x]
    return y

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)

PORT = 1234
s.bind((host, PORT))

print(host, f"({ip})")

_NAME = "SENDER"
           
s.listen(1)
print("Listening for incoming connections...")
conn, addr = s.accept()
print(f"Received connection from {addr[0]} ({addr[1]})")

server_name = conn.recv(1024).decode()
print(f"CONNECTED TO {server_name}")

conn.send(_NAME.encode())
# m = int(input("Enter m: "))
m =3
windowSize = 2**m - 1

# message = input(str("Type a message: "))
message = "1234567890234"
f = len(message)

if message == "/exit":
    sys.exit(500)

frames = prepare_frames(message, m)

# Position of sliding window
i = 0

while i < f:
    
    # Print sliding window.
    print(' '.join([*(message[0:i] + '[' + message[i:i+windowSize] + ']' + message[i+windowSize:])]))
    
    # Send all frames in current window
    for j in range(windowSize):
        if i+j < f:
            to_send = f'{frames[i+j][0]}:{frames[i+j][1]}:{frames[i+j][2]}'
            conn.send(to_send.encode())
            time.sleep(1.5)
    
    # Listen for ACK
    last_ack = ''
    for j in range(windowSize):
        # Set timeout to 10s
        try:
            conn.settimeout(10.0)
            ack = conn.recv(4).decode()[-4:]
            if ack and (last_ack != ack):
                last_ack = ack
            conn.settimeout(None)
        except:
            pass

    # last_ack = ACK1
    last_ack = last_ack.replace("ACK", "")
    
    # If no ACK recieved.
    if last_ack == '': 
        print(f'Last ACK = ACK{last_ack}')
        continue
    
    try: 
        last_ack = int(last_ack)
    except ValueError: 
        print('Error')
        sys.exit()

    print(f'Last ACK = ACK{last_ack}\n')

    # Calculating how far ahead
    i += (last_ack - (i%windowSize))%windowSize + 1
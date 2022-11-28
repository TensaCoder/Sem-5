import time, socket, random

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)

PORT = 1234
_NAME = "RECIEVER"

print(host, f"({ip})")
s.connect((host, PORT))
s.send(_NAME.encode())

client_name = s.recv(1024)
client_name = client_name.decode()
print(f"CONNECTED TO {client_name}")

message = ''
last_frame = -1
transmissionStarted = False
try:
   while True:
      s.settimeout(40)
      frame = s.recv(5).decode().split(':')
      s.settimeout(None)

      time.sleep(1)
      if(int(frame[1]) == 0): transmissionStarted = True

      # Intolerant of lost frames.
      # If current frame > 0 and current frame number is not next expected frame number.
      if transmissionStarted and (int(frame[1]) != last_frame + 1):
         # If recieved frame is previously recieved already, retransmit ACK.
         if (int(frame[1]) <= last_frame):
            # 40% chance of ACK LOST
            if random.random() < 0.8:
               s.send(('ACK'+frame[2]).encode())
               print(f'ACK{frame[2]} SENT')
            else:
               print(f'ACK{frame[2]} LOST')
         continue

      print(f"'{frame[0]}' - [{frame[1]}]")
      message += frame[0]
      last_frame = int(frame[1])

      # 40% chance of ACK LOST
      if random.random() < 0.8:
         s.send(('ACK'+frame[2]).encode())
         print(f'ACK{frame[2]} SENT')
      else:
         print(f'ACK{frame[2]} LOST')
      
      time.sleep(1)

except:
   print(f'Recieved message: {message}')
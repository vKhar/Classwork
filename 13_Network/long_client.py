from socket import socket
import time 

f = open("HAMLET.txt", "r")
s = socket()
s.connect( ('127.0.0.1',1234)  )
print("Start of File Transfer")
for l,line in enumerate(f):
    s.sendall(line.encode())
    time.sleep(1)
    if l == 20:
        break
f.close()
s.sendall(chr(0).encode())

while True: ## wait for acknowledgement
    rec_msg = s.recv(1024)
    if rec_msg == b"OK":
        s.close()
        break
print("End of File Transfer")
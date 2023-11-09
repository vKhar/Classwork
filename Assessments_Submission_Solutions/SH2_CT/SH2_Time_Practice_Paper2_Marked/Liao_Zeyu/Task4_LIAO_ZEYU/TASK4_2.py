import socket

s=socket.socket()
s.bind(("127.0.0.1", 9999))
s.listen()
s.accept()
while True:
    rec=s.recv(4096).decode()
    print(rec)
'''
[1]
'''
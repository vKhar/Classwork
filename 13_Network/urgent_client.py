from socket import socket

s = socket()
#s.bind( ('127.0.0.99',9003))
s.connect(('127.0.0.1',1234))
s.send(b"VERY URGENT MESSAGE" + chr(0).encode())
s.close()
print("VERY Urgent message sent -- whew!")

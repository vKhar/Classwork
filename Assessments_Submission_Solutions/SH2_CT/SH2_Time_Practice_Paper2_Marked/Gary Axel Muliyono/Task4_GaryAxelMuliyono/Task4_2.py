from socket import socket

ls_socket = socket()
ls_socket.bind(('127.0.0.1',9999))
ls_socket.listen()
s,address = ls_socket.accept()
msg = ""
while True:
    msg += s.recv(4096).decode()
    if '\n' in tmp:
        msg = msg.replace('\n','')
        break

msg = msg.split(',')
h2 = {'A':20,'B':17.5,'C':15,'D':12.5,'E':10,'S':5,'U':0}
h1 = {'A':10,'B':8.75,'C':7.5,'D':6.25,'E':5,'S':2.5,'U':0}
try:
    gp = msg[0]
    pw = msg[1]
    h21 = msg[2]
    h22 = msg[3]
    h23 = msg[4]
    hextra = msg[5]
    data = h1[gp] + h1[pw] + h2[h21] + h2[h22] + h2[h23] + h1[hextra]
    data = str(data)
except:
    data = ""

s.send(data.encode())
ls_socket.close()

'''
typo line 10
[3]
'''

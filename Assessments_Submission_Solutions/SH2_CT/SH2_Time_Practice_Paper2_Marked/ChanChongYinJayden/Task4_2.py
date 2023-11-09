from socket import socket

s = socket()
s.bind(("127.0.0.1",9999))
s.listen()

while True:
    client, _ = s.accept()
    msg = ""
    while b"\n" not in chunk:
        chunk = client.recv(2048).decode()
        msg += chunk
    grades = msg[:-1].split(",")
    uas = sum([float(i) for i in grades])
    s.sendall(uas.encode())
    client.close()
    
s.close()

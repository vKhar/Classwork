import socket

g2rp = {
    "A": 10,
    "B": 8.75,
    "C": 7.5,
    "D": 6.25,
    "E": 5,
    "S": 2.5,
    "U": 0
}    

s = socket.socket()
s.bind(("127.0.0.1", 9999))
s.listen()

while True:
    client, ip = s.accept()
    data = client.recv(4096).decode()
    data = data.strip().split(",")
    res = g2rp[data[0]] + g2rp[data[1]] + g2rp[data[5]] + 2*(g2rp[data[2]] + g2rp[data[3]] + g2rp[data[4]])
    res = str(res).encode()
    client.sendall(res)
    client.close()

## [4]
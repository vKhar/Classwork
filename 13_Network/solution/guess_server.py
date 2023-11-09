import socket
import random

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 9999))
listen_socket.listen()

s, addr = listen_socket.accept()
answer = random.randint(1, 100)
guessed = False
for i in range(5):
    s.sendall(b'GUESS\n')
    data = b''
    while b'\n' not in data:
        data += s.recv(1024)
    guess = int(data)
    print("received", guess)
    if guess < answer:
        s.sendall(b'LOW\n')
    elif guess > answer:
        s.sendall(b'HIGH\n')
    else:
        guessed = True
        break
if guessed:
    s.sendall(b'WIN\n')
else:
    s.sendall(b'GAMEOVER\n')

s.close()
listen_socket.close()

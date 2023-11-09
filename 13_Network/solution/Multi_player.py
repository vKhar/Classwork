import socket
import random
from threading import Thread

class Guess_number(Thread):
    def __init__(self, client_sock):
        Thread.__init__(self)
        self.client_sock = client_sock
    def run(self):
        s = self.client_sock
        answer = random.randint(1, 100)
        guessed = False
        for i in range(5):
            s.sendall(b'GUESS\n')
            data = b''
            while b'\n' not in data:
                data += s.recv(1024)
            guess = int(data)
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


listen_socket = socket.socket()
listen_socket.bind(('', 9999))
listen_socket.listen()
while True:
    s, addr = listen_socket.accept()
    print(f"Playing with {addr}")
    guess_t = Guess_number(s)
    guess_t.start()

listen_socket.close()

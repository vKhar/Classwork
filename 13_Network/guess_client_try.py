import socket, time

s = socket.socket()
s.connect(('127.0.0.1', 9999))

correct = False
while not correct :
    raw = s.recv(4096)
    print(f"Received {raw}")

    received = raw.decode().split("\n")
    
    for code in received:
        if code == 'Low':
            print('Your guess is too low.')
        elif code== 'High':
            print('Your guess is too high.')
        elif code == 'GUESS':
            guess = input('Enter guess (1-100): ')
            s.send(guess.encode())
        elif code == 'Correct':
            print('You guessed correct!')
            correct = True
            break
    time.sleep(0.1)
s.close()

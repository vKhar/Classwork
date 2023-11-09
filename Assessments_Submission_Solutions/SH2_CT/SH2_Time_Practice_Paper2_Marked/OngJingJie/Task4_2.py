import socket

listen_socket= socket.socket()
listen_socket.bind(("127.0.0.1", 9999))
listen_socket.listen()
print("socket is listening")
while True:
    client_socket, remote_address = listen_socket.accept()
    msg = ''
    while "\n" not in msg:
        msg+=client_socket.recv(1024).decode()
    if msg == "N,N,N,N,N,N\n":
        client_socket.close()
        break
    scores = msg.strip().split(",")
    h1 = scores[:2]+[scores[-1]]
    h2 = scores[2:-1]
    grades = ["A", "B", "C", "D"]
    lower_grades = ["E", "S", "U"]
    score = 0
    for grade in h1:
        if grade in grades:
            score += 10-1.25*grades.index(grade)
        else:
            score += 5-2.5*lower_grades.index(grade)
    for grade in h2:
        if grade in grades:
            score += 20-2.5*grades.index(grade)
        else:
            score += 10-5*lower_grades.index(grade)
    client_socket.sendall(str(score).encode())
    client_socket.close()
listen_socket.close()
print("server off")

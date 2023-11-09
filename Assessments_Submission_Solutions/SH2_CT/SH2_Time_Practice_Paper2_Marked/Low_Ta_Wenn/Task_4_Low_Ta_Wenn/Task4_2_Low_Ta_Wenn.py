#from socket import Socket
#listen_socket = Socket()

listen_socket.bind(("127.0.0.1", 9999))
listen_socket.listen()
while True:
    client, ret = listen_socket.accept()
    grades = client.recv(4096)
    grades = grades.decode()[:"/n"].split(",")
    h2 = {"A":20, "B":17.5, "C":15, "D":12.5, "E":10, "S":5, "U":0}
    h1 = {"A":10, "B":8.75, "C":7.5, "D":6.25, "E":5, "S":2.5, "U":0}
    score = h1[grades[0]] + h1[grades[1]] + h2[grades[2]] + h2[grades[3]] + h2[grades[4]] + h1[grades[5]]
    client.send(score.encode() + b"\n")
listen_socket.close()

'''
line 1, 2 syntax : use the ref guide
line 9 : do you know what slicing is ?!!!
line 13: how can you encode() on an int ?!!
[1]
'''

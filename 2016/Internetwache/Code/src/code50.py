import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('188.166.133.53',11027))
    
data = s.recv(2048)
print data


data = s.recv(2048)
question = data.split(' ')
print question

if question[3] == "-":
    s.send(str(int(question[4]) + int(question[6])) + "\n")
elif question[3] == "+":
    s.send(str(int(question[6]) - int(question[4])) + "\n")
elif question[3] == "*":
    s.send(str(int(question[6]) / int(question[4])) + "\n")
elif question[3] == "/":
    s.send(str(int(question[6]) * int(question[4])) + "\n")

for x in range(0, 200):
    data = s.recv(19)
    print data
    data = s.recv(512)
    question = data.split(' ')
    print question

    if question[3] == "-":
        s.send(str(int(question[4]) + int(question[6])) + "\n")
    elif question[3] == "+":
        s.send(str(int(question[6]) - int(question[4])) + "\n")
    elif question[3] == "*":
        s.send(str(int(question[6]) / int(question[4])) + "\n")
    elif question[3] == "/":
        s.send(str(int(question[6]) * int(question[4])) + "\n")

data = s.recv(2048)
print data

#s.send(str(20) + "\n")

s.close()


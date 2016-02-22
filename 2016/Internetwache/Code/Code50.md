# Internetwache 2016 : Code (50)

**Category:** code |
**Points:** 50 |
**Name:** A numbers game |
**Solves:** 407 |
**Description:**

> People either love or hate math. Do you love it? Prove it! You just need to solve a bunch of equations without a mistake.
>
> Service: 188.166.133.53:11027

___

## Write-up

### Part Zero
We were given a service which we connect using python sockets.

```
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('188.166.133.53',11027))
data = s.recv(2048)
print data
```

And we get the first part
```
Hi, I heard that you're good in math. Prove it!
Level 1.: x - 2 = 6
```

### Part One

Using a if else for each of + - / *, solving the math equation is easy.
```
if question[3] == "-":
        s.send(str(int(question[4]) + int(question[6])) + "\n")
    elif question[3] == "+":
        s.send(str(int(question[6]) - int(question[4])) + "\n")
    elif question[3] == "*":
        s.send(str(int(question[6]) / int(question[4])) + "\n")
    elif question[3] == "/":
        s.send(str(int(question[6]) * int(question[4])) + "\n")
```

We get the flag after 100 solves we get the flag:
```
IW{M4TH_1S_34SY}
```

[See full script here](src/code50.py)
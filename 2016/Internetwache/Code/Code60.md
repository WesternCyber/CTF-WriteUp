# Internetwache 2016 : It's Prime Time! (60)

**Category:** code |
**Points:** 60 |
**Name:** It's Prime Time! |
**Solves:** 388 |
**Description:**

> We all know that prime numbers are quite important in cryptography. Can you help me to find some?
>
> Service: 188.166.133.53:11059

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
Hi, you know that prime numbers are important, don't you? Help me calculating the next prime!
Level 1.: Find the next prime number after 8:
```

### Part One
The quesion is split by spaces, so it seemed easiest to use .split on the string to convert it to an array.
```
data = s.recv(2048)
question = data.split(' ')
print question
```

### Part Two

Using Bertrand's postulate for finding the next prime number, it solves easily
```
x = int(question[8][:1])
y = 2
for x in range(int(question[8][:-2]) + 1, 2 * int(question[8][:-2])):
    if x % 2 != 0:
        for y in range(2, x / 2 + 1):
            if x % y == 0:
                break
        if x % y == 0:
            continue
        else:
            print "Sending " + str(x)
            s.send(str(x) + "\n")
            break
```

We get the flag after 100 solves we get the flag:
```
IW{Pr1m3s_4r3_!mp0rt4nt}
```

[See full script here](src/code60.py)
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

```

### Part One


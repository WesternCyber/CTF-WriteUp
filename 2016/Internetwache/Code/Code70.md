# Internetwache 2016 : Code (70)

**Category:** Code |
**Points:** 70 |
**Name:** A numbers game II |
**Solves:** 230 |
**Description:**

> Math is used in cryptography, but someone got this wrong. Can you still solve the equations? Hint: You need to encode your answers.
>
>Attachment: code70.zip
>
>Service: 188.166.133.53:11071

___

## Write-up
Download the zip. The file looks like this:
```python
def encode(eq):
    out = []
    for c in eq:
        q = bin(ord(c)^(2<<4)).lstrip("0b")
        q = "0" * ((2<<2)-len(q)) + q
        out.append(q)
    b = ''.join(out)
    pr = []
    for x in range(0,len(b),2):
        c = chr(int(b[x:x+2],2)+51)
        pr.append(c)
    s = '.'.join(pr)
    return s
```
I replace the self.\_xor to ^ since I don't want a class.

The first loop is to transfer the result of the xor of ASCII value of any character in the equation and 32 to a 8-bit binary code.

The second loop is to transfer every two dit to a number then plused to 3.

So what we need to do is easy.

Just reverse the process.

1. First minus 3 then transfer to 2-digit binary code.
2. put them together then split into 8-digit groups.
3. Transfer the 8-digit binary code to int then do the xor again. (hint: a^b^b=a)
4. get the equation, use the function in Code50 to calculate the result.
5. encode the result and send to server.

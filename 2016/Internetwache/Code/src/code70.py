import socket

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

#encode("abcdefghijklmnopqrstuvwxyz0123456789")

def reverseOperator(opt):
    if opt=='+':
        return '-'
    if opt=='-':
        return '+'
    if opt=='*':
        return '/'
    else:
        return '*'


s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

s.connect(('188.166.133.53',11071))

data = s.recv(512)

print data
while True:
    print "hohohohoh"
    datas=data.split("\n")
    print len(datas)
    if len(datas)>2:
        code=datas[1]
    else:
        code=s.recv(512)
    print code

    nums=code.replace("\n","").split(':')[1].strip().split('.')
    print len(nums)
    b=""
    print chr(51)
    for num in nums:
        prefix=bin(ord(num)-51).lstrip("0b")
        prefix="0" * (2-len(prefix)) + prefix
        b+=prefix
    print b
    print len(b)
    eq=""

    for i in range(0,len(b),8):
        binCode=b[i:i+8]
        charValue=int(binCode,2)
        eq+=chr(charValue^(2<<4))
    print eq

    equ=eq
    equs=equ.split("=")
    result=equs[1]
    equs=equs[0].replace("\n","").strip().split(" ")
    print equs
    newEqu=result+reverseOperator(equs[1])+equs[2]
    print newEqu
    x=eval(newEqu)
    print x
    s.send(encode(str(x))+"\n")
    data=s.recv(512)
    print data

s.close()


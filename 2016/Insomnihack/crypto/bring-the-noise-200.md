Our solution code can be found [here](https://github.com/nomoonx/insomnihack/blob/master/Bring%20the%20noise/crack.py).

After reading the [server code](https://github.com/nomoonx/insomnihack/blob/master/Bring%20the%20noise/server-bd6a6586808ab28325de37276aa99357.py), it's a python socket server. We can see at the end of the function Handler, there's one line output the FLAG.
```python
put('%s\n' % FLAG)
```
So, we need to beat the function Handler. We can seperate it into two parts.

### Part One
```python
challenge = hexlify(os.urandom(1+POWLEN/2))[:POWLEN]
put('Challenge = %s\n' % challenge)
response = self.rfile.readline()[:-1]
print response#I added for debugging
responsehash = hashlib.md5(response).hexdigest().strip()
if responsehash[:POWLEN] != challenge:
    put('Wrong\n')
    return
```
The variable POWLEN is 5 here.

It generated a random 5-characters string called challenge and will tell the client what challenge is. After get a response from client, compute the md5 of that response and compare the first 5 characters with challenge. So our problem became 'To generated a string whose md5 value has the same prefix as a given string'. Since md5 is a 32-digit hexadecimal number and the probabilities of each value is almost even, we can calculate the least time we need to try is 16^5=1048576 to get the same prefix value.
So, we come up an idea is to check the md5 value of integer to see if it fits.
```python
for i in range(1048976):
    responsehash = hashlib.md5(str(i)).hexdigest().strip()
    if responsehash[:5] == challenge:
        request=i
        break
```
After test, the hit rate is almost 1/3 which is acceptable. Of course, if we increase the range, the hit rate can be increased. But we need to balance the hit rate and the running time. So, it's good for now.

### Part Two
```python
equations, solution = learn_with_vibrations()
for equation in equations:
  put(equation + '\n')

print 'solution'
print solution

put('Enter solution as "1, 2, 3, 4, 5, 6"\n')

print 'receving'
sol = self.rfile.readline().strip()
print sol
if sol != str(solution)[1:-1]:
  put('Wrong\n')
  return
```
All the print lines are added by us to do debugging.

So there's a function to generate equations and solution called `learn_with_vibrations`. The equations will be sent to client and the client should return a solution called sol here to be compared with that solution. Therefore, the problem became 'how to generate a solution from the equations'.

Let's see the `learn_with_vibrations` function.
```python
def learn_with_vibrations():
    q, n, eqs = 8, 6, 40
    solution = [randint(q) for i in range(n)]
    equations = []
    for i in range(eqs):
        coefs = [randint(q) for i in range(n)]
        result = sum([solution[i]*coefs[i] for i in range(n)]) % q
        vibration = randint(3) - 1
        result = (result + q + vibration) % q
        equations.append('%s, %d' % (str(coefs)[1:-1], result))
    return equations, solution
```
The solution is a randomly generated 6 digit array.
Each row in equations is a randomly generated 6 digit array and a result calculated by itself and solution.
Since we can know every equation, the only thing we need to do is brutal force all 6 digit array and use a reverse rule to check if that's the solution.
```python
def solve(equations):
    q, n, eqs = 8, 6, 40
    a=[1,2,3,4,5,6]
    for a[0] in range(q):
        for a[1] in range(q):
            for a[2] in range(q):
                for a[3] in range(q):
                    for a[4] in range(q):
                        for a[5] in range(q):
                            flag=True
                            for equation in equations:
                                eq=equation.split(',')
                                result = sum([a[i]*int(eq[i]) for i in range(n)]) % q
                                tempFlag=False
                                for i in range(3):
                                    if(result+q+i-1)%q==int(eq[-1]):
                                        tempFlag=True
                                        break
                                if not tempFlag:
                                    flag=False
                                    break
                            if flag:
                                return a
```
We should write it in a better way. But just 6 digit, so we used a brutal way to write it.

# CSAW CTF 2016 : LosT Code (200)

**Category:** bruteforce |
**Points:** 50 |
**Name:** LosT Code|
**Solves:** ? |
**Description:**
___

## Write-up

We were given an executable file. It requested a 32 length string containing characters from a-f and 0-9 and outputted a 32 length binary string. It would return 1 at the location where your input string matched the flag answer.

We wrote a bruteforce python program that initially inputted a random string into the program and kept the characters that we guess right.
After running our program for a minute, we got the flag. 

```
import subprocess
import os
import random
import string

found = 0
string1="abcdef0123456789"
array1=[]
location = 0
while found == 0:

	string2 = ''.join(random.choice(string1) for _ in range(32))
	
	temp = list(string2)
	for item in array1:
		tempnum = item[0]
		tempchar = item[1]
		temp[tempnum] = tempchar
	string2 = ''.join(temp)
	p = subprocess.Popen("wine LosT.exe -b " + string2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
		print string2
		print line
	retval = p.wait()
	string3 = line

	array1=[]

	for i in range (0,32):
		if string3[i] is '1':
			array1.append([i,string2[i]])
```
 
 The resulting flag was '616dc3888a99170c5b8aa721d925ac68'
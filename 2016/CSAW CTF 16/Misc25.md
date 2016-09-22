# Insomnihack 2016 : Misc (25)

**Category:** misc |
**Points:** 25 |
**Name:** coinslot |
**Solves:** ? |
**Description:**

>Coinslot

>#Hope #Change #Obama2008

___

## Write-up

Our solution code can be found [here](https://github.com/zxie43/coinslot/blob/master/misc.py).

When we connected to the challenge, it gave us a money value and asked us to make change with various $ bills.
You had to enter the amount of bills starting from $10,000 bills counting down.
 e.g:

>$0.06
>$10,000 bills: 0
>$5,000 bills: 0
>$1,000 bills: 0
>$500 bills: 0
>$100 bills: 0
>$50 bills: 0
>$20 bills: 0
>$10 bills: 0
>$5 bills: 0
>$1 bills: 0
>$100 bills: 0
>half-dollars (50c): 0
>quarters (25c): 0
>dimes (10c): 0
>nickels (5c): 1
>pennies (1c): 1
>correct!
>$0.05
>$10,000 bills: 0
>...

### Python script

We wrote a python script to automate the task of making change. 

We connected to the server using: 
```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('misc.chal.csaw.io',8000))

```

Then we parsed the $ amount from the received data and converted it to an int(and also multiplied by 100) to make life easier. 

```python
for x in range(0, 700):
	data = s.recv(100)
	print data
	list1 = list(data)
	numbers = re.findall(r"[-+]?\d*\.\d+|\d+", data)
	fl1 = numbers[0]
	print fl1
	fl1 = float(fl1)
	fl1 = fl1*100.00
	int1 = int(round(fl1))
	print int1
```
Then we ran the number through every bill amount from $10,000 to 1 cent to get the # of bills for each category and sent it to the server.

```python
	if int1 >= 1000000:
		value = int1 - 1000000
		s.send(str(int1/1000000) + "\n")
		int1 = int1 % 1000000
	else:
		s.send(str(0) + "\n")
	data = s.recv(recvnumber)
```

After we left the program to run for 5 minutes and 100+ different amounts, it spit out the flag.

The flag is: flag{started-from-the-bottom-now-my-whole-team-fucking-here}

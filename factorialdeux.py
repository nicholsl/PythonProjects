#factorial.py

def factorial(n):
	n = int(input('What would you like the factorial of?'))
	product = 1
	for taco in range (n,1,-1):
		product = product * taco
	print ('The factorial of', n , 'is', product,'!')

def type(n):
	n = float(input('What is your number?'))
	if n % 2 == 0:
		print (n, 'is even')
	elif n % 1 == 0:
		print (n, 'is odd')
	else:
		print (n, 'is very strange')
type(5)



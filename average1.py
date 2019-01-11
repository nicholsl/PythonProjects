#average1.py

def main():
	n = int(input ("How many numbers do you have?"))
	if n == type(int):
		sum = 0.0
		for i in range(n):
			x = input('Enter a number')
			sum = sum + int(x)
		print ("\nThe average of the numbers is",sum / n)
	else: print ('thats not an integer')	
	
main ()
'''factorial.py
		program to compute the factorial of a number
		illustrates for loop with accumulator
'''

def main():
	n = input("Please enter a whole number")
	fact = 1
	print (type(n), type(fact))
	print()
	for factor in range(2,(int(n)+1)):
		fact = fact * factor
	print ("The factorial of", n, "is", fact)

main()



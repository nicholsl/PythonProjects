#change.py

def main():

	price = 100*(float(input('How much does the item cost?')))
	tendered = 100*(float(input('How much was tendered?')))
	print()
	change = (round((tendered - price),2))
	print(change)
	list = [5000, 2000, 1000, 500, 100, 25, 10, 5, 1]
	for taco in list:
		if change >= taco:
			NumberOfFifties= change//taco
			change = change % taco
		else:
			NumberOfFifties= 0
		if change >= taco:
			NumberOfTwenties = change//taco
			change = change % taco
		else:
			NumberOfTwenties = 0
		if change >= taco:
			NumberOfTens = change//taco
			change = change % taco
		else:
			NumberOfTens = 0
		if change >= taco:
			NumberOfFives = change//5.00
			change = change % taco
		else:
			NumberOfFives=0
		if change >= taco:
			NumberOfOnes= change//taco
			change = change % taco
		else:
			NumberOfOnes = 0

	print(NumberOfFifties)
	print(NumberOfTwenties)
	print(NumberOfTens)
	print(NumberOfFives)
	print(NumberOfOnes)

main()
	
		
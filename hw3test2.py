#changedue.py
#Liz Nichols - 9/20/2016

def main():

	price = 100*(float(input('How much does the item cost? ')))
	tendered = 100*(float(input('How much was tendered? ')))
	print()
	change = (round((tendered - price),2))
	print('change due', (change/100))
	list = [5000, 2000, 1000, 500, 100, 25, 10, 5, 1]
	bill = []
	for taco in list:
		if change >=taco:
			bill.append(change//taco)
			change=change%taco
		else:
			bill.append(0)
	moneypl = ['fifties', 'twenties', 'tens', 'fives', 'ones', 'quarters', 'dimes', 'nickels', 'pennies']
	money= ['fifty','twenty','ten','five','one','quarter','dime','nickel','penny']
	k=0
	for value in bill:
		if int(value) == 1:
			print (int(value),money[k])
		else:
			print (int(value),moneypl[k])
		k = k+1
		 
main()
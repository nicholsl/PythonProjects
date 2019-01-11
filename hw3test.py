#change.py

def main():

	price = 100*(float(input('How much does the item cost?')))
	tendered = 100*(float(input('How much was tendered?')))
	print(price) 
	print(tendered)
	
	change = (round((tendered - price),2))
	print(change)
	
	list = [5000,2000,1000,500,100,25,10,5,1]
	for taco in list
		if change >= taco
main()

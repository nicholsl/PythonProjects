date = input('month/day/year')
print (date)
thingstocheck = [(date.split('/'))]

def checkdate(month,day)
    thirtyDayMonths = [9,4,6,11]
    if month in range(1,13):
        if day not in range(1,32):
            print("That's an invalid number of days!")
        elif month in thirtyDayMonths and day not in range(1,31):
            print ('Thirty days have September, April, June, and November')
        elif month == 2 and day not in range(1,29)
            print ('February is special.')
        else:
            print("That's a valid date!")
    else:
        print("I've never heard of that month!")

def checkyear(year)
    if year % 
            

            

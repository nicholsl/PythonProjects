'''weatherstats.py

Written by Danielle Eisen, Liz Nichols 10/08/2016

Analyzes msp-temperatures.txt weather-data file to display interesting statistical features
of the data. Takes file-name as a command line argument.
Theoretically could analyze other files in the same format. 
Otherwise program will give error message.
Capabilities are mean, standard deviation, and the minimum and maximum temperatures, as 
well as min and max standard deviation and mean for all years. Program also accounts
for instances of duplicate minimum/maximum temperatures, means, and standard deviations.'''

import sys

def loadWeatherData(fileName):
	file = open(fileName)

	alldatalist = []
	for line in file:
		temporarylist = []
		temporarylist = (line.split(','))
		for i in range(len(temporarylist)):
			temporarylist[i]=int(temporarylist[i])
		alldatalist.append(temporarylist)
	
	return (alldatalist)

def mean(listOfNumbers):
	sum=0
	for i in listOfNumbers:
		sum = sum + i
	meanValue = sum/(len(listOfNumbers))
	
	return(meanValue)

def standardDeviation(listOfNumbers):
	mu = mean(listOfNumbers)
	sumResidSquares = 0
	for i in listOfNumbers:
		residual = (i-mu)
		residualsquared = residual**2
		sumResidSquares = sumResidSquares + residualsquared
	radicand = sumResidSquares/len(listOfNumbers)
	stdev = radicand ** (1/2)
	
	return(stdev)

def extremetemps(listOfLists):	
	max = listOfLists[0][1]
	min = listOfLists[0][1]
	maxyear = []
	minyear = []
	for eachyear in listOfLists:
		for temperature in eachyear[1:]:
			if temperature > max:
				max = temperature
			elif temperature < min:
				min = temperature
	for eachyear in listOfLists:
		for temperature in eachyear[1:]:
			if temperature == max:
				maxyear.append(eachyear[0])
			elif temperature == min:
				minyear.append(eachyear[0])
						
	return (max, maxyear, min, minyear)

def displaydata(listOfLists):
	
	minmean = mean(listOfLists[0][1:])
	maxmean = mean(listOfLists[0][1:])
	
	minstdev = standardDeviation(listOfLists[0][1:])
	maxstdev = standardDeviation(listOfLists[0][1:])
	
	minmeanyear = []
	maxmeanyear = []
	
	minstdevyear = []
	maxstdevyear = []
	
	tolerance = .01
	
	''' although the minimum and maximum standard deviation and mean are distinct
	for this set of data, we included a tolerance to account for situations where 
	virturally equal means or standard deviations created double instances of a min or max
	stdev or mean'''
	
	for eachyear in listOfLists:
		
		year = eachyear[0]
		meanValue = mean(eachyear[1:])
		stdev = standardDeviation(eachyear[1:])	
		
		#prints data
		print('{0:5}{1:9.2f}{2:9.2f}'.format(year,meanValue,stdev))
		
		if meanValue < minmean:
			minmean = meanValue
		elif meanValue > maxmean:
			maxmean = meanValue
		if stdev < minstdev:
			minstdev = stdev
		elif stdev > maxstdev:
			maxstdev = stdev
			
	for eachyear in listOfLists:
		
		stdev = standardDeviation(eachyear[1:])	
		meanValue = mean(eachyear[1:])
		
		if abs(maxstdev - stdev) <= tolerance:
			maxstdevyear.append(eachyear[0])
		elif abs(minstdev - stdev) <= tolerance:
			minstdevyear.append(eachyear[0])
		if abs(maxmean - meanValue) <= tolerance:
			maxmeanyear.append(eachyear[0])
		elif abs(minmean - meanValue) <= tolerance:
			minmeanyear.append(eachyear[0])
	
	return (minmean, minmeanyear, maxmean, maxmeanyear, minstdev, minstdevyear, maxstdev, maxstdevyear)
			
def main():
	try:
		fileName = sys.argv[1]
		alldatalist = loadWeatherData(fileName)
		
		#prints headings
		print('\nHigh temperature data (Fahrenheit)')
		print('\n'+'{0:>5}{1:>8}{2:>12}'.format('Year', 'Mean','Std Dev'),'\n')
		
		max, maxyear, min, minyear = extremetemps(alldatalist)
		minmean, minmeanyear, maxmean, maxmeanyear, minstdev, minstdevyear, maxstdev, maxstdevyear = displaydata(alldatalist)	
		
		print ('\n'+'{0:}{1:.2f} {2:}'.format('Highest mean temperature:  ', maxmean, maxmeanyear))
		print ('{0:}{1:.2f} {2:}'.format('Lowest mean temperature:  ', minmean, minmeanyear))
		print ('\n'+'{0:}{1:.2f} {2:}'.format('Highest standard deviation:  ', maxstdev, maxstdevyear))
		print ('{0:}{1:.2f} {2:}'.format('Lowest standard deviation:  ', minstdev, minstdevyear))
		print ('\n'+'Highest temperature: ', max, maxyear)
		print ('Lowest temperature: ', min, minyear,'\n')
		 
	except FileNotFoundError:
		print("I can't find your file ;_;")
	except IndexError:
		print("Tell me what file you want to analyze in the command line.")
	except:
		print("Your file is hard to read.")

if __name__ == '__main__':
	main()
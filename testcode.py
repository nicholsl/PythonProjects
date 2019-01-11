
def loadweatherdata(filename):
	file = open(filename)

	alldatalist = []
	for line in file:
		temporarylist = []
		temporarylist = (line.split(','))
		for i in range(len(temporarylist)):
			temporarylist[i]=int(temporarylist[i])
		alldatalist.append(temporarylist)
	
	return (alldatalist)
#WHEN CALLING MEAN, REMEMBER TO CALL IT ON listOfNumbers[1:]
def mean(listOfNumbers):
	sum=0
	for i in listOfNumbers:
		sum = sum + i
	mean = sum/(len(listOfNumbers))
	
	return(mean)

#WHEN CALLING STANDARDDEVIATION, REMEMBER TO CALL IT ON listOfNumbers[1:0]
def standardDeviation(listOfNumbers):
	#print (mean(listOfNumbers))
	mu = mean(listOfNumbers)
	sumResidSquares = 0
	for i in listOfNumbers:
		residual = (i-mu)
		residualsquared = residual**2
		sumResidSquares = sumResidSquares + residualsquared
	radicand = sumResidSquares/len(listOfNumbers)
	stdev = radicand ** (1/2)
	
	return(stdev)

def main():
	filename = input('Please tell me the name of your file!')
	alldatalist = loadweatherdata(filename)
	for eachyear in alldatalist:
		print(eachyear[0],format(mean(eachyear[1:]),'.2f'), format(standardDeviation(eachyear[1:]),'.2f'))
main()

#yearlist = []
#for year in alldatalist:
	#yearlist.append(year[0])
		
#don't forget to format stdev to a certain number of sigfigs 	

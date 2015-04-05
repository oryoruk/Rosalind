#!usr/bin/python

def population(month,litterCapability):
	if month==1 or month ==2:
		return 1
	else:
		return population(month-1,litterCapability) + population(month-2,litterCapability)*litterCapability

datasetFile = open("rosalind_fib.txt","r")
answerFile  = open("rosalind_fib_answer.txt","w")

#print datasetFile.readline().strip().split()

month, litterCapability =  [int(element) for element in datasetFile.readline().strip().split()]

answerFile.write( str( population(month, litterCapability) ) )

datasetFile.close()
answerFile.close()

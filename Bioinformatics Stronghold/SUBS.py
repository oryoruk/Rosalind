#!usr/bin/python

#alt 1
"""
def substringLocations(inpSeq, subSeq): 
	locationList = []
	index = 0
	while index < len(inpSeq):
		location = inpSeq[index:].find(subSeq)
		if location != -1:
			location += index
			locationList.append( location )
			index = location + 1
		else:
			index = len(inpSeq)	
	return [i+1 for i in locationList]
"""
#alt 2
"""
def substringLocations(inpSeq, subSeq):
	locationList = []
	location = 0
	while location < len(inpSeq):
		location = inpSeq.find(subSeq,location)
		if location != -1:
			locationList.append(location)
			location += 1
		else: location = len(inpSeq)
	return locationList
"""
#alt 3
def substringLocations(inpSeq, subSeq):
	return [i for i in xrange(len(inpSeq)) if inpSeq[i:i+ len(subSeq)] == subSeq ]

datasetFile = open("rosalind_subs.txt","r")
answerFile  = open("rosalind_subs_answer.txt","w")

inputSeq,searchSeq = [line.strip() for line in  datasetFile.readlines()]
answerFile.write( " ".join( [str(i+1) for i in substringLocations(inputSeq,searchSeq)] ) )

datasetFile.close()
answerFile.close()

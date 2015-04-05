#!usr/bin/python

datasetFile = open("rosalind_gc.txt","r")
answerFile  = open("rosalind_gc_answer.txt","w")

#alt 1 
"""
lineList = [i.strip() for i in datasetFile.readlines()]

fastaDict = {}

index = 0
while index < len(lineList) :
	if lineList[index][0] == ">":
		key = lineList[index].strip(">")
		fastaDict[key] = ""
		relativeIndex = 1
		while index+relativeIndex<len(lineList) and lineList[index+relativeIndex][0]!=">":
			fastaDict[key] += lineList[index+relativeIndex]
			relativeIndex += 1
	index +=1

print fastaDict
highestGC_ID, highestGCvalue = "",0.0

for fastaID in fastaDict:
	sequence = fastaDict[fastaID]
	GCvalue = (sequence.count("G") + sequence.count("C") ) / float(len(sequence)) * 100
	if GCvalue > highestGCvalue:
		highestGCvalue = GCvalue
		highestGC_ID = fastaID

answerFile.write(highestGC_ID +"\n"+ str(highestGCvalue))

datasetFile.close()
answerFile.close()
"""

#alt 2
def extractFASTAdict(FASTAstring):
	blocks = FASTAstring.split(">")[1:]
	FASTAdict = {}
	for block in blocks:
		FASTAid,FASTAsequence = block.split("\n",1)
		FASTAdict[FASTAid] = FASTAsequence.replace("\n","")
	return FASTAdict

def GCcontent(sequence):
	return ( sequence.count("G") + sequence.count("C") ) / float(len(sequence)) * 100

def highestGC(FASTAdict):
	highestGCid, highestGCcontent = "",0.0
	for tempFASTAid in FASTAdict:
		tempSequence = FASTAdict[tempFASTAid]
		tempGCcontent= GCcontent(tempSequence)
		if tempGCcontent > highestGCcontent:
			highestGCcontent = tempGCcontent
			highestGCid = tempFASTAid
	return (highestGCid,highestGCcontent)

FASTAstring = datasetFile.read()
FASTAdict = extractFASTAdict(FASTAstring)
highestGCid, highestGCcontent = highestGC(FASTAdict)

#print highestGCid
#print highestGCcontent

answerFile.write( highestGCid + "\n" + str(highestGCcontent) )

datasetFile.close()
answerFile.close()

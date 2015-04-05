#!usr/bin/python

def profile(iD):	#inputDictionary
	zippedSeq = zip(*iD.values())
	pMD = {} 	#profileMatrixDictionary
	for nucleotide in "ACGT":
		pMD[nucleotide] = [i.count(nucleotide) for i in zippedSeq]
	#print	[i.count(nucleotide) for nucleotide in "ACGT" for i in zippedSeq] #nested list comprehension version
	return pMD

def consensus(pMD):
	cS = ""		#consensusString
	for i in range(len(pMD["A"])):
		m = max(pMD["A"][i],pMD["C"][i],pMD["G"][i],pMD["T"][i])
		for x in "ACGT":
			if pMD[x][i]==m: 
				cS+=x
				break
	return cS
	
datasetFile = open("rosalind_cons.txt","r")
answerFile  = open("rosalind_cons_answer.txt","w")

inputDict =  dict( [ ( block[:block.index("\n")],block[block.index("\n")+1:].replace("\n","") ) for block in datasetFile.read().split(">")[1:] ] )
profileMatrixDict = profile(inputDict)
consensusString = consensus(profileMatrixDict)

answerFile.write(consensusString+"\n")
for i in "ACGT": answerFile.write(i+": " + " ".join( [str(s) for s in profileMatrixDict[i]] ) +"\n" )

datasetFile.close()
answerFile.close()

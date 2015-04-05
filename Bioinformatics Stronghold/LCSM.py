#!usr/bin/python

def longestCommonSubstringOf(strings):
	lcsm = ''
	if len(strings) > 1 and len(strings[0]) > 0:
		for i in range(len(strings[0])):
			for j in range(len(strings[0])-i-1):
				if j > len(lcsm) and isSubstring(strings[0][i:i+j], strings):
					lcsm = strings[0][i:i+j]
	else:
		lcsm = strings[0]
	return lcsm

def isSubstring(candidateLcsm, strings):
    if len(strings) < 1 and len(candidateLcsm) < 1:
        return False
    for i in range(len(strings)):
        if candidateLcsm not in strings[i]:
            return False
    return True

datasetFile = open("rosalind_lcsm.txt","r")
answerFile  = open("rosalind_lcsm_answer.txt","w")

#one liner FASTA parser
seqDict = dict( [ (seqId, seqString.replace("\n","")) for seqId, seqString in [block.split("\n",1) for block in datasetFile.read().split(">")[1:]] ] )

answerFile.write( longestCommonSubstringOf(seqDict.values()) )

datasetFile.close()
answerFile.close()

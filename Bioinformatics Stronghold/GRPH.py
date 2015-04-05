#!usr/bin/python

datasetFile = open("rosalind_grph.txt","r")
answerFile  = open("rosalind_grph_answer.txt","w")

seqDict = {}

for entry in datasetFile.read().split(">")[1:]:
	seqId, seqString = entry.split("\n",1)
	seqDict[ seqId ] = seqString.replace("\n","")

for seq1key in seqDict:
	for seq2key in seqDict:
		if seqDict[seq1key][-3:]==seqDict[seq2key][:3] and seq1key != seq2key:
			answerFile.write(seq1key + " " + seq2key + "\n")

answerFile.close()
datasetFile.close()

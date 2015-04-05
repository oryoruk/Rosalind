#!usr/bin/python

#alt1
"""
def HAMMdistance(seq1,seq2):
	hd = 0
	for index in range( len( seq1 ) ):
		if seq1[index] != seq2[index]:
			hd += 1
	return hd
"""
#alt2
def HAMMdistance(seq1,seq2):return [a==b for (a,b) in zip(sequence1,sequence2)].count(False)

datasetFile = open("rosalind_hamm.txt","r")
answerFile  = open("rosalind_hamm_answer.txt","w")

sequence1 = datasetFile.readline()
sequence2 = datasetFile.readline()

answerFile.write( str( HAMMdistance(sequence1,sequence2) ) )

datasetFile.close()
answerFile.close()

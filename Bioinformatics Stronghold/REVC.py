#!usr/bin/python

datasetFile = open("rosalind_revc.txt","r")
answerFile  = open("rosalind_revc_answer.txt","w")

DNAstring = datasetFile.readline().strip()


#alt 1
"""
REVClist = list( reversed( list(DNAstring) ) )

for index in range(len(REVClist)):
	if REVClist[index] == "A":
		REVClist[index] = "T"
	elif REVClist[index] == "T":
		REVClist[index] = "A"
	elif REVClist[index] == "G":
		REVClist[index] = "C"
	else:
		REVClist[index] = "G"

answerFile.write( "".join(REVClist) )
"""

#alt 2
"""
complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
REVClist = [] 
for i in DNAstring[::-1]:
	REVClist.append(complement[i])

answerFile.write( "".join(REVClist) )
"""

#alt 3

complement = dict( zip("ATCG","TAGC") )
answerFile.write( "".join( complement[nucleotide] for nucleotide in reversed(DNAstring) ) )

datasetFile.close()
answerFile.close()

#!usr/bin/python

bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

def PROTsequence(RNAsequence):
	temp = "" 
	for i in range(0,len(RNAsequence),3):
		temp += codon_table.get(RNAsequence[i]+RNAsequence[i+1]+RNAsequence[i+2],"X")
	return temp.strip("*")

datasetFile = open("rosalind_splc.txt","r")
answerFile  = open("rosalind_splc_answer.txt","w")

sequences= [[block.split("\n",1)[0] , block.split("\n",1)[1].replace("\n","")] for block in datasetFile.read().split(">")[1:] ]

codingRegion=sequences[0][1]
for i in range(1,len( sequences)):
	codingRegion = codingRegion.replace(sequences[i][1],"")
codingRegion = codingRegion.replace("T","U")

prot = PROTsequence(codingRegion)
answerFile.write(prot)

datasetFile.close()
answerFile.close()

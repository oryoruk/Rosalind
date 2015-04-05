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

datasetFile = open("rosalind_prot.txt","r")
answerFile  = open("rosalind_prot_answer.txt","w")

RNAsequence = datasetFile.readline().strip()
answerFile.write( PROTsequence(RNAsequence) )

datasetFile.close()
answerFile.close()

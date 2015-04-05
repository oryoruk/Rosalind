#!usr/bin/python

datasetFile = open("rosalind_dna.txt","r")
answerFile = open("rosalind_dna_answer","w")

#nucleotideCounter = {}

DNAstring = datasetFile.readline()

#alt1
#for nucleotide in DNAstring:
#	nucleotideCounter[nucleotide] = nucleotideCounter.get(nucleotide,0)+1
#answerString = str(nucleotideCounter['A']) + " " + str(nucleotideCounter['C']) + " " + str(nucleotideCounter['G']) + " " + str(nucleotideCounter['T'])
#AnswerFile.write(answerString)

#alt2
#for nucleotide in "ACGT":
#	answerFile.write(str(DNAstring.count(nucleotide))+" ")

#alt3
answerFile.write( " ".join([str(DNAstring.count(nucleotide)) for nucleotide in "ACGT"]) )

datasetFile.close()
answerFile.close()

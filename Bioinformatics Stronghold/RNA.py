#!usr/bin/python

datasetFile = open("rosalind_rna.txt","r")
answerFile  = open("rosalind_rna_answer.txt","w")

DNAstring = datasetFile.readline()
RNAstring = DNAstring.replace("T","U")

answerFile.write(RNAstring)

datasetFile.close()
answerFile.close()

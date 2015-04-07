#!usr/bin/python

from Bio.Seq import Seq

datasetFile = open("rosalind_ini.txt","r")
answerFile  = open("rosalind_ini_answer.txt","w")

my_seq = Seq(datasetFile.read())
#first approach
#answerFile.write(str(my_seq.count("A"))+" "+str(my_seq.count("C"))+" "+\
#		str(my_seq.count("G"))+ " " + str(my_seq.count("T")))

#second approach
nucs = "ACGT"
counts = [str(my_seq.count(nuc)) for nuc in nucs]
answerFile.write(" ".join(counts))

datasetFile.close()
answerFile.close()


#!usr/bin/python

from Bio import ExPASy
from Bio import SwissProt
datasetFile = open("rosalind_dbpr.txt","r")
answerFile  = open("rosalind_dbpr_answer.txt","w")

uniProtId = datasetFile.read().strip()

handle = ExPASy.get_sprot_raw(uniProtId)
record = SwissProt.read(handle)

for i in record.cross_references:
    if i[0]=='GO' and  i[2][0]=='P': answerFile.write(i[2].strip("P:")+"\n")

datasetFile.close()
answerFile.close()

#!usr/bin/python

f = open("rosalind_ini5.txt","r")
a = open("rosalind_ini5_answer.txt","w")

lineCounter = 1
for line in f:
	if lineCounter % 2 is 0:
		a.write(line)
	lineCounter+=1

f.close()
a.close()


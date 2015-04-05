#!usr/bin/python

f = open("rosalind_ini6.txt","r")
a = open("rosalind_ini6_answer.txt","w")

wordCountDict = {}
listOfWords = f.read().split()
for word in listOfWords:
	if word not in wordCountDict:
		wordCountDict[word] = 1
	else:
		wordCountDict[word] += 1

for entry in wordCountDict:
	a.write(entry+" "+str(wordCountDict[entry])+"\n")

f.close()
a.close()

#!usr/bin/python

def doit(a,b):
	sum = 0
	for i in range(a,b+1):
		if i%2 is 1:
			sum +=i
	return sum

f = open("rosalind_ini4.txt","r")
a = open("rosalind_ini4_answer.txt","w")

x,y = (int(i) for i in f.readline().split())
a.write(str(doit(x,y)))


f.close()
a.close()

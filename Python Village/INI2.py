#!usr/bin/python

f = open("rosalind_ini2.txt","r")
a = open("rosalind_ini2_answer.txt","w")

#numberStringList = f.readline().split()
#x=int(numberStringList[0])
#y=int(numberStringList[1])

x,y = (int(x) for x in f.readline().split())

a.write(str(x**2+y**2))

f.close()
a.close()


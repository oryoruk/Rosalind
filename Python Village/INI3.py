#!usr/bin/python

f=open("rosalind_ini3.txt","r")
a=open("rosalind_ini3_answer.txt","w")

string = f.readline()
x,y,z,t = (int(i) for i in f.readline().split())

a.write(string[x:y+1]+" "+string[z:t+1])

f.close()
a.close()

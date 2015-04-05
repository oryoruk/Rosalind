#!usr/bin/python

def calculateDominantProb(k,m,n):
	total = k + m + n 
	return 1 - (  ( n/total * (n-1)/(total-1) ) + (m/total * n/(total-1) * 0.5 * 2) + (m/total * (m-1)/(total-1) * 0.25 ) ) 

datasetFile = open("rosalind_iprb.txt","r")
answerFile  = open("rosalind_iprb_answer.txt","w")

k,m,n = [float(i) for i in datasetFile.readline().split()]
answerFile.write( str( calculateDominantProb(k,m,n) ) )

datasetFile.close()
answerFile.close()

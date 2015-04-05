#!usr/bin/python

datasetFile = open("rosalind_iev.txt","r")
answerFile  = open("rosalind_iev_answer.txt","w")

XdomPhenOffs = 0.0

genotypeCoupleCounts = [ int(count) for count in datasetFile.read().strip().split() ]

XdomPhenOffs += 2.0 * genotypeCoupleCounts[0] 
XdomPhenOffs += 2.0 * genotypeCoupleCounts[1] 
XdomPhenOffs += 2.0 * genotypeCoupleCounts[2] 
XdomPhenOffs += 1.5 * genotypeCoupleCounts[3] 
XdomPhenOffs += 1.0 * genotypeCoupleCounts[4] 
XdomPhenOffs += 0.0 * genotypeCoupleCounts[5] 

answerFile.write( str( XdomPhenOffs ) )

datasetFile.close()
answerFile.close()

#!usr/bin/python

adults = [0,1]

def totalAdults(n,m):
	if n<2: return adults[n]
	else:
		total = 0
		
		#+ babies of last month = # adults of two months ago
		if adults[n-2]!=-1: total += adults[n-2]
		else: total += totalAdults(n-2,m)

		#+ all adults of last month
		if adults[n-1]!=-1: total += adults[n-1]
		else: total += totalAdults(n-1,m)

		#- the ones who pass away = the ones that were babies m months ago = # of adults n-m-1 months ago
		if n>m:#
			if adults[n-m-1] != -1: total -= adults[n-m-1]
			else: total -= totalAdults(n-m-1,m)
		elif n==m:#cannot go to month n-m-1, gets negative, so babies m months ago/at month 0: number of babies is 1
			total -= 1
		adults[n] = total
		return total

datasetFile = open("rosalind_fibd.txt","r")
answerFile  = open("rosalind_fibd_answer.txt","w")

n,m = [int(i) for i in datasetFile.readline().strip().split()]
n -= 1 # for python indexing / months start at 0 for convenience

for i in range(n-1):adults.append(-1)

answerFile.write( str(totalAdults(n,m)+totalAdults(n-1,m)) )

datasetFile.close()
answerFile.close()

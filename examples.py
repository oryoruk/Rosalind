#!usr/bin/python

#Python Examples
#+++++++++++++++

#STRINGS
stringA = "012345678"
listA = list(stringA)

print	"----Strings 1----"
print 	stringA
print	listA

print	"----Strings 2----"
print 	(stringA+"-")*3

print	"----Strings 3----"
print 	stringA[3:8]
print	stringA[8:0:-1]
print 	stringA[::-1]

print	"----Strings 4----"
print 	len(stringA)
print	stringA.count("0")

print	"----Strings 5----"
print	len(stringA + " ")
print	len( (stringA + " ").strip() )
print	len("+++" + stringA + "+")
print	len( ("+++" + stringA + "+").strip("+") )

print	"----Strings 6----"
print	"-".join(listA)

print	"----Strings 7----"
print 	stringA[0:3] + "-" + stringA[3:6] + "-" + stringA[6:10]
print 	(stringA[0:3] + "-" + stringA[3:6] + "-" + stringA[6:10]).split("-")

print	"----Strings 8----"
print	stringA[2]
print	listA[2]
print	stringA.index("2")

print	"----Strings 9----"
print 	stringA.replace("0","x")
print	stringA

assert stringA == "012345678"
pass
temp = raw_input("Please enter random input:")

#LISTS
listA[2]="x"
print	listA
listA[2] = "xx"
print listA
listA[2] = "2"
listA.append("9")
print listA
stringB = "".join(listA)
print stringB
listA.reverse()
print listA
listA.reverse()
print listA
for element in reversed(listA):
	print element,
print
print listA

seq = ("a","b","c")
print seq

"""


DICTIONARIES
d = {}
dictA = {"X":1,
del d['XYZ']
d.get("Key",0) #gets the value, if it does not exist it returns 0
dict(tuple list)

dict( zip("aoeu","ueoa") )

range(start,stop,step)
range(start,stop) #step=1
range(stop) #start = 0, step = 1
"""

#!/home/hashcon/Hacking-Kit/bin/python
import base64
import sys
import re

'''
What is a base64 string
'''

def isStringBase64():
	if(len(sys.argv) == 1):
		print("Not enough arguments provided")
		sys.exit(-1)

	#user might add more stuff
	numOfStrings = []
	for i in range(len(sys.argv)-1): #-1 for the name of the file
		numOfStrings.append(sys.argv[i+1])
	potentialBase64 = "".join(numOfStrings)
	print(potentialBase64)

	#The length of a base64 sting must be of multiple of 4
	if((len(potentialBase64)%4)!=0):
		print("Provided string is not off base64")
		return
	regexForBase64 = "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$"
	if(re.search(regexForBase64,potentialBase64)):
		print(base64.b64decode(potentialBase64).decode())
		return
	print("This is not a base64 string")


isStringBase64()
